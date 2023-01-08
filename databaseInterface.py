# This program handles all functionality related to storing and retrieving data from the database

import sqlite3
import pandas as pd
import sqlalchemy
from datetime import datetime
import os

current_file_path = os.getcwd()
path_to_database = os.path.join(current_file_path, "data", "SebaData.db")

# Create connection to SQL and an engine for SQLalchemy
connection = sqlite3.connect(r'{}'.format(path_to_database))
cursor = connection.cursor()
engine = sqlalchemy.create_engine(r'sqlite:///{}'.format(path_to_database)).connect()

def createNewDataRow(asp_name,grade):
    # Get the current timestamp
    timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    # Store the new data into a dictionary
    new_data = {'asp_name': asp_name, 'timestamp': timestamp, 'grade': grade}
    # Create a new pandas dataframe using the new_data
    new_row = pd.DataFrame(new_data, index=[0])
    #Return the new_row
    return new_row

def getDataTable(engine,site_name):
    # Retrieve the data and store it into a pandas dataframe
    df = pd.read_sql_table(site_name, engine, index_col=0)
    return df

def sendToDatabase(df,engine,site_name):
    new_row = createNewDataRow("Acton01",86)

    # Appened the new row to the dataframe
    df = pd.concat([new_row,df], ignore_index=True)

    # Send the dataframe to the database
    df.to_sql('Franklin', engine, if_exists='replace', index=False)

