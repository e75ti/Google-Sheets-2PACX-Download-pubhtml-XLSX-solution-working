import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-{your_url}/pubhtml'

tables = pd.read_html(url)
tables[0].to_excel('output.xlsx', index=False,header=True)
