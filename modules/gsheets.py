from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name("./creds/sheets.json", scope)
client=gspread.authorize(creds)

def gsheets():
    # Dictionary
    dictionary = {}

    # data_sheet is used to access to the data
    data_sheet = client.open("Daily-Infinity-CONSOLIDADO").sheet1
    # You should replace de name 'Daily-Infinity-CONSOLIDADO' for 
    # your own google sheets name file ***

    #Importing data from colum 1 - saving dates from sheet
    dates = data_sheet.col_values(1)

    # Actual date! 
    today = datetime.now()
    today = today.strftime("%d/%m/%Y")
    

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

            if title == 'Ayer?':
                dictionary['yesterday'] = data_daily
            elif title == 'Hoy?':
                dictionary['today'] = data_daily
            elif title == 'Impedimentos':
                dictionary['impediments'] = data_daily

    #print(dictionary)
    print('Google Sheets OK')
    return dictionary