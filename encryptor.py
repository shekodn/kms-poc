import base64
import boto3
import json
import os

from data import users

from dotenv import load_dotenv

load_dotenv()

ENCRYPTOR_AWS_ACCESS_KEY_ID = os.environ["ENCRYPTOR_AWS_ACCESS_KEY_ID"]
ENCRYPTOR_AWS_SECRET_ACCESS_KEY = os.environ["ENCRYPTOR_AWS_SECRET_ACCESS_KEY"]
KEY_ID = os.environ["KEY_ID"]

encryptor_session = boto3.Session(
    aws_access_key_id=ENCRYPTOR_AWS_ACCESS_KEY_ID,
    aws_secret_access_key=ENCRYPTOR_AWS_SECRET_ACCESS_KEY,
)

client = encryptor_session.client("kms", region_name="us-east-2")
key_id = KEY_ID

print("Username: ")
username = input()
user_id = users.get_user_id(username)

if not user_id:
    raise Exception("No user found")

print(f"Hello {username}, please enter your message to encrypt: ")

message = input()
message_bytes = message.encode("ascii")

response = client.encrypt(
    Plaintext=message_bytes,
    EncryptionContext={"user_id": user_id},
    KeyId=key_id,
    EncryptionAlgorithm="SYMMETRIC_DEFAULT",
)

ciphertext_blob = response["CiphertextBlob"]
base64_bytes = base64.b64encode(ciphertext_blob)
base64_message = base64_bytes.decode("ascii")

print(f"Your encrypted message base64 encoded: \n {base64_message}")
