import base64
import boto3
import json
import os

from data import users

from dotenv import load_dotenv

load_dotenv()

DECRYPTOR_AWS_ACCESS_KEY_ID = os.environ["DECRYPTOR_AWS_ACCESS_KEY_ID"]
DECRYPTOR_AWS_SECRET_ACCESS_KEY = os.environ["DECRYPTOR_AWS_SECRET_ACCESS_KEY"]
KEY_ID = os.environ["KEY_ID"]

decryptor_session = boto3.Session(
    aws_access_key_id=DECRYPTOR_AWS_ACCESS_KEY_ID,
    aws_secret_access_key=DECRYPTOR_AWS_SECRET_ACCESS_KEY,
)

client = decryptor_session.client("kms", region_name="us-east-2")
key_id = KEY_ID

print("Username: ")
username = input()
user_id = users.get_user_id(username)

if not user_id:
    raise Exception("No user found")

print(f"Hello {username}, please enter your message to decrypt: ")

base64_ciphertext_raw = input()
base64_ciphertext = base64_ciphertext_raw.strip()
base64_ciphertext_bytes = base64_ciphertext.encode("ascii")

ciphertext_blob = base64.b64decode(base64_ciphertext_bytes)

response = client.decrypt(
    CiphertextBlob=ciphertext_blob,
    EncryptionContext={"user_id": user_id},
    KeyId=key_id,
    EncryptionAlgorithm="SYMMETRIC_DEFAULT",
)

plaintext_bytes = response["Plaintext"]
plaintext = plaintext_bytes.decode("ascii")

print(f"Your decrypted message: {plaintext}")
