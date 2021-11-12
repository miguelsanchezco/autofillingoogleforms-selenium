from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Edita los siguientes 2 valores para ajustarlo a tus necesidades
GOOGLE_SHEET_NAME = "Daily-CONSOLIDADO"
CREDS_GOOGLE_CLOUD_FILE_PATH = './creds/credsGoogleCloud.json'
# ATENCION: dentro del archivo .json encontrarás un email,
# añade este email como usuario que puede modificar tu hoja de google sheets 
# de esta forma podrá acceder a ella y realizar la lectura de datos.

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_GOOGLE_CLOUD_FILE_PATH, scope)
client=gspread.authorize(creds)

def gsheets():
    # Dictionary
    dictionary = {}

    # data_sheet is used to access to the data
    sht = client.open(GOOGLE_SHEET_NAME)
    data_sheet = sht.get_worksheet(0)
    #data_sheet = client.open(GOOGLE_SHEET_NAME).sheet1
    # You should replace de name 'Daily-Infinity-CONSOLIDADO' for 
    # your own google sheets name file ***

    #Importing data from colum 1 - saving dates from sheet
    dates = data_sheet.col_values(1)

    # Actual date! 
    today = datetime.now()
    today = today.strftime("%d/%m/%Y")
    # Transformamos la fecha a nuestro formato dia/mes/año
    
    #serching for the coincident dates and saving data
    for index,date in enumerate(dates):
        
        if date == today:
            #date found! - saving row number
            row = index +1  
            #Daily text introduced by team members
            data_daily = data_sheet.cell(row,3)
            data_daily = str(data_daily.value)
            # title could be : Ayer? Hoy? Impedimientos
            title = data_sheet.cell(row,2)
            title = str(title.value)
            # assignments
            if title == 'Ayer?':
                dictionary['yesterday'] = data_daily

            elif title == 'Hoy?':
                dictionary['today'] = data_daily

            elif title == 'Impedimentos':
                dictionary['impediments'] = data_daily

    #print(dictionary)
    print('Google Sheets OK')
    return dictionary