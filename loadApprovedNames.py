import csv
import openpyxl
import pandas as pd

def loadApprovedNames():
    file  = "approvedNames.xlsx"
    df = pd.read_excel(file)
    return df
