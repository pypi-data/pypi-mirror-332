from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from Crypto.Cipher import AES
import argparse
import requests
import tempfile
import base64
import shutil
import boto3
import os
import subprocess

org_name = "securin"
cli_file_name = "securin-cli-win.exe"
api_host_name = "slresultapi.qa.securin.io"

def download_file_from_s3(aws_access_key, aws_secret_key, aws_session_token, bucket_name, s3_path):
    full_s3_path = f"{s3_path}/{cli_file_name}"
    try:
        # Create a session using the provided AWS credentials
        session = boto3.Session(
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            aws_session_token=aws_session_token
        )
        
        # Create an S3 client
        s3 = session.client('s3')
        
        # Get the temporary directory path
        temp_dir = tempfile.gettempdir()
        if os.path.exists(os.path.join(temp_dir, org_name)):
            shutil.rmtree(os.path.join(temp_dir, org_name))
        os.makedirs(os.path.join(temp_dir, org_name), exist_ok=True)
        destination_path = os.path.join(temp_dir, org_name,cli_file_name)
        # Download the file from S3
        s3.download_file(bucket_name, full_s3_path , destination_path)
        return destination_path
    except NoCredentialsError:
        print("Credentials not available")
        return None
    except PartialCredentialsError:
        print("Incomplete credentials provided")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def decrypt_keys(key, iv, value):
    try:
        key_bytes = bytes.fromhex(key)
        iv_bytes = bytes.fromhex(iv)
        value_bytes = base64.b64decode(value)
        
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
        decrypted = cipher.decrypt(value_bytes)
        
        # Remove padding
        pad = decrypted[-1]
        decrypted = decrypted[:-pad]
        
        return decrypted.decode('utf-8')
    except Exception as e:
        print(f"An error occurred during decryption: {e}")
        return None

def get_cli_details_from_s3(api_key, version=None):
    s3_url = f"https://{api_host_name}/resultapi/cli/version/s3/details"
    
    if version:
        s3_url = f"{s3_url}?version={version}"
    
    headers = {
        "X-ASPM-Auth-Key": api_key
    }
    
    response = requests.get(s3_url, headers=headers)
    
    if response.status_code != 200 or not response.text:
        return None, None
    
    enc_response = response.json()
    bucket_name = enc_response.get('bucket_name', '')
    bucket_path = enc_response.get('key_path', '')
    
    return bucket_name, bucket_path

def get_latest_enc_keys(api_key):
    enc_keys_url = f"https://{api_host_name}/resultapi/enc/keys"
    headers = {
        "X-ASPM-Auth-Key": api_key
    }
    
    response = requests.get(enc_keys_url, headers=headers)
    
    if response.status_code != 200 or not response.text:
        return None, None
    
    enc_response = response.json()
    enc_key = enc_response.get('KEY', '')
    enc_iv = enc_response.get('IV', '')

    if not enc_key or not enc_iv:
        return None, None
    
    return enc_key, enc_iv

def get_aws_credentials_from_aspm(api_key):
    aws_token_url = f"https://{api_host_name}/resultapi/cli/aws/accesstoken"
    headers = {
        "X-ASPM-Auth-Key": api_key
    }
    
    response = requests.get(aws_token_url, headers=headers)
    
    if response.status_code != 200 or not response.text:
        return None, None, None
    
    enc_response = response.json()
    access_key = enc_response.get('accessKey', '')
    secret_key = enc_response.get('secretKey', '')
    session_token = enc_response.get('sessionToken', '')
    
    if not access_key or not secret_key or not session_token:
        return None, None, None
    
    return access_key, secret_key, session_token

def main():
    global api_host_name
    parser = argparse.ArgumentParser(description="A basic Python library that takes command-line arguments.")

    parser.add_argument('--api_key', type=str, required=True, help='API key')
    parser.add_argument('--app_id', type=str, required=False, help='Application ID')
    parser.add_argument('--app_name', type=str, required=False, help='Application name')
    parser.add_argument('--branch_name', type=str, required=False, default='default', help='Branch name')
    parser.add_argument('--enable_color', action='store_true', help='Enable color in report')
    parser.add_argument('--format', type=str, required=False, help='Output format')
    parser.add_argument('--is_console_report', action='store_true', default=True, help='Console report')
    parser.add_argument('--is_debug', action='store_true', help='Enable debug logs')
    parser.add_argument('--output_file', type=str, required=False, help='Output file')
    parser.add_argument('--scan_types', type=str, required=False, help='Types of scans to be triggered')
    parser.add_argument('--severity', type=str, required=False, help='Severity')
    parser.add_argument('--skip_build_fail', action='store_true', help='Skip build fail')
    parser.add_argument('--source_dir', type=str, required=False, default=os.getcwd(), help='Source directory')
    parser.add_argument('--version', type=str,required=False, help='Which version of the CLI to use')
    parser.add_argument('--hostname', type=str, required=False, default=api_host_name, help='Hostname of the API Endpoint')

    args = parser.parse_args()

    if args.hostname:
        api_host_name = args.hostname.strip()

    bucket_name, bucket_path = get_cli_details_from_s3(args.api_key, args.version)

    if not bucket_name or not bucket_path:
        print("No bucket details found")
        return

    enc_key, enc_iv = get_latest_enc_keys(args.api_key)

    if not enc_key or not enc_iv:
        print("No encryption details found")
        return

    enc_access_key, enc_secret_key, enc_session_token = get_aws_credentials_from_aspm(args.api_key)

    if not enc_access_key or not enc_secret_key or not enc_session_token:
        print("No AWS credentials found")
        return
    
    aws_access_key = decrypt_keys(enc_key, enc_iv, enc_access_key)
    aws_secret_key = decrypt_keys(enc_key, enc_iv, enc_secret_key)
    aws_session_token = decrypt_keys(enc_key, enc_iv, enc_session_token)

    if not aws_access_key or not aws_secret_key or not aws_session_token:
        print("Error decrypting AWS credentials")
        return


    executable_path = download_file_from_s3(aws_access_key, aws_secret_key, aws_session_token, bucket_name, bucket_path)

    if not executable_path:
        print("Error downloading the executable")
        return
    
    cli_args = [executable_path]
    
    if args.api_key:
        cli_args.extend(['--api_key', args.api_key])
    if args.app_id:
        cli_args.extend(['--app_id', args.app_id])
    if args.app_name:
        cli_args.extend(['--app_name', args.app_name])
    if args.branch_name:
        cli_args.extend(['--branch_name', args.branch_name])
    if args.enable_color:
        cli_args.append('--enable_color')
    if args.format:
        cli_args.extend(['--format', args.format])
    if args.is_console_report:
        cli_args.append('--is_console_report')
    if args.is_debug:
        cli_args.append('--is_debug')
    if args.output_file:
        cli_args.extend(['--output_file', args.output_file])
    if args.scan_types:
        cli_args.extend(['--scanner_type', args.scan_types])
    if args.severity:
        cli_args.extend(['--severity', args.severity])
    if args.skip_build_fail:
        cli_args.append('--skip_build_fail')
    if args.source_dir:
        cli_args.extend(['--source_dir', args.source_dir])
    
    try:
        result = subprocess.run(cli_args, capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred while executing the CLI: {e}")

if __name__ == "__main__":
    main()
