from __future__ import print_function

from seach_cep import get_cep

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from sheets import *

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = SHEETID  # here I put the information code from my sheet
RANGE = SHEETRANGE

data = get_cep()
print(data)

address = {
    'CEP': data[0]['cep'],
    'street': data[0]['street'],
    'number': data[1],
    'comp': data[2],
    'neighbor': data[0]['district'],
    'city': data[0]['city'],
    'state': data[0]['uf']
}

[print(key, value) for key, value in address.items()]


def register():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/home/erik_proenca/Documentos/RPA/Python_RPA/quotation/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        values = [
            [
                address['CEP'],
                address['street'],
                address['number'],
                address['comp'],
                address['neighbor'],
                address['city'],
                address['state']
            ],
        ]

        body = {
            'values': values
        }

        sheet = service.spreadsheets()

        result = sheet.values().append(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range=RANGE,
            valueInputOption='USER_ENTERED',
            body=body
        ).execute()

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    register()
