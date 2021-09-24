import pandas as pd
import gspread
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

service_account_info={} # A credential that must be created in developoers.google.com . Please visit this link for more information: https://betterprogramming.pub/how-to-connect-to-google-sheets-with-python-83d0b96eeea6

credentials = service_account.Credentials.from_service_account_info(service_account_info)

scoped_credentials = credentials.with_scopes(
        ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
        )
def gdoc_to_df(sheet_id, sheet_name):
    

    gc = gspread.Client(auth=scoped_credentials)
    gc.session = AuthorizedSession(scoped_credentials)
    sheet = gc.open_by_key(sheet_id)
    g_doc=sheet.worksheet(sheet_name).get_all_values()
    header = g_doc.pop(0)
    df = pd.DataFrame(g_doc, columns=header)
    return df

    
    








