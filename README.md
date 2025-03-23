# Retrieving All Values from All Sheets from URL of 2PACX- of Web Published Google Spreadsheet using Python

This is a sample script for retrieving all values from all sheets from URL of 2PACX- of Web Published Google Spreadsheet using Python.

It avoids the old method of appending `/pub?output=xlsx` to the url.

Requirements of pip modules are **pandas**, **openpyxl** and **lxml**.

## Code:

```python
import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-{your_url}/pubhtml'

tables = pd.read_html(url)
tables[0].to_excel('output.xlsx', index=False,header=True)
```

## Result and venv notes

The output will be output.xlsx file which you can open with your preferred reader, Excel or Libreoffice Writer. If your system is a linux distro with externally-managed-environment for pip, you will need to set up venv.
To do that just use `python3 -m venv venv` and then `source ./bin/activate` and `pip3 install pandas openpyxl lxml`

Best of luck!
