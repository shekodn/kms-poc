# A Little Bit of Action with AWS KMS

### TL;DR
Encryption as a Service PoC using Python and AWS KMS.

## Overview
![overview](./docs/diagram.png)

## Prerequisites
- Have an AWS account with enough privilages to run the Cloud Formation template.
- Change the `CLI_PROFILE` var in `./deploy.sh`

## Setup
Just run `./deploy.sh` and wait for a couple of minutes. If you see an output like the following, we are ready to go.
```
[
    {
        "ExportingStackId": "arn:aws:cloudformation:us-east-2:XXX:stack/kms-poc/a59778da-fe1b-11ea-adc1-0242ac120002",
        "Name": "DecryptorUserAccessKey",
        "Value": "AKIAXXXXXXXXXXXXXXXX"
    },
    {
        "ExportingStackId": "arn:aws:cloudformation:us-east-2:XXX:stack/kms-poc/a59778da-fe1b-11ea-adc1-0242ac120002",
        "Name": "DecryptorUserSecretAccessKey",
        "Value": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    },
    {
        "ExportingStackId": "arn:aws:cloudformation:us-east-2:XXX:stack/kms-poc/a59778da-fe1b-11ea-adc1-0242ac120002",
        "Name": "EncryptorUserAccessKey",
        "Value": "AKIAXXXXXXXXXXXXXXXX"
    },
    {
        "ExportingStackId": "arn:aws:cloudformation:us-east-2:XXX:stack/kms-poc/a59778da-fe1b-11ea-adc1-0242ac120002",
        "Name": "EncryptorUserSecretAccessKey",
        "Value": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    },
    {
        "ExportingStackId": "arn:aws:cloudformation:us-east-2:XXX:stack/kms-poc/a59778da-fe1b-11ea-adc1-0242ac120002",
        "Name": "theKeyAlias",
        "Value": "alias/kms-poc"
    },
    {
        "ExportingStackId": "arn:aws:cloudformation:us-east-2:XXX:stack/kms-poc/a59778da-fe1b-11ea-adc1-0242ac120002",
        "Name": "theKeyId",
        "Value": "a59778da-fe1b-11ea-adc1-0242ac120002"
    }
]
(END)

```
Create a `.env` file and use `env.example` for some inspiration. You should be able to get all the info you need from the previous output.

Note: For the `KEY_ID` env variable's value, we can use either `theKeyId`'s or the `theKeyAlias`'s value. 


## How to Encrypt
- Run `python3 encryptor.py`
- Use either `alice` or `bob` to "authenticate".
- Write a message to ecrypt.
- Hit Enter

You should see a base64 output like this:
```
 AQICAHhQUp2GIUg1Tf/r2I9nmNWsIJGDrRYieOviWRC0SLz/bwEXoiPmO1CgXGPhO5su0nhJAAAAbjBsBgkqhkiG9w0BBwagXzBdAgEAMFgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM9eb1WUEj8kK/WBjvAgEQgCs9K6dPBPgWZ+ZqKqXdIt1S/CUE1Xj9fcUq9vo95Mw/6XKv8yQkciWBnH55
```

## How to Decrypt

- Copy the output from the encryptor and proceed to run the decryptor by doing: `python3 decryptor.py`
- Use the same user you used to encrypt earlier during the process.
- Paste the base64 output 
- If everything went as planned, you should see something like:

```
Username: 
alice

Hello alice, please enter your message to decrypt: 
 AQICAHhQUp2GIUg1Tf/r2I9nmNWsIJGDrRYieOviWRC0SLz/bwEXoiPmO1CgXGPhO5su0nhJAAAAbjBsBgkqhkiG9w0BBwagXzBdAgEAMFgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM9eb1WUEj8kK/WBjvAgEQgCs9K6dPBPgWZ+ZqKqXdIt1S/CUE1Xj9fcUq9vo95Mw/6XKv8yQkciWBnH55

Your decrypted message: this is a secret
```
