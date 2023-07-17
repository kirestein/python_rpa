# Este código é um esqueleto para poder rodar a api do google.
from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from date_time import *
from quotation import value_usd, value_eur
from sheets import *


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = SHEETID # here I put the information code from my sheet
RANGE_DOLLAR = SHEETRANGEDOLAR
RANGE_EURO = SHEETRANGEEURO


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
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

        values_dollar = [
            [date, time, str(value_usd).replace('.', ',')],

        ]
        body_dollar = {
            'values': values_dollar
        }

        values_euro = [
            [date, time, str(value_eur).replace('.', ',')],
        ]
        body_euro = {
            'values': values_euro
        }

        # Call the Sheets API
        sheet = service.spreadsheets()
        #reading data
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=RANGE_DOLLAR).execute()
        insert_dollar = service.spreadsheets().values().append(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range=RANGE_DOLLAR,
            valueInputOption='USER_ENTERED',
            body=body_dollar
        ).execute()
        # print(result)
        output_values = result['values']
        [print(item) for item in output_values]
        print(values_dollar)
        print(body_dollar)

        insert_euro = service.spreadsheets().values().append(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range=RANGE_EURO,
            valueInputOption='USER_ENTERED',
            body=body_euro
        ).execute()

        print(values_euro)
        print(body_euro)

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()