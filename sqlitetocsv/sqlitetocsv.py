import sqlite3
import pandas as pd
import os
import logging
import csv

class exporttoCSV:

    def __init__(self, db_path):
        self.path = db_path

    def db_connect(self):
        con = sqlite3.connect(self.path)
        return con

    def execute_sql(self, query):

        con = self.db_connect()
        curr = con.cursor()
        # Select table and display
        curr.execute(query)

        # Fetches all the rows from the result of the query
        rows = curr.fetchall()

        # Gets the column names for the table
        colnames = [desc[0] for desc in curr.description]

        # Converts into readable pandas data frame
        df_result = pd.DataFrame(rows, columns=colnames)
        return df_result

    def csvwriter(self, df_data, filename):
        # writes the pandas data frame to csv file
        folder_name=self.path.strip('.db')
        try:
            os.mkdir(folder_name)
        except OSError:
            logging.info("Creation of the directory %s failed" % folder_name)
        logging.info("Successfully created the directory %s " % folder_name)
        file_name = folder_name + '/' + filename + '.csv'
        df_data.to_csv(file_name, quoting=csv.QUOTE_MINIMAL, encoding='utf-8', index=False)

    def alltables(self):
        # Export all the tables information to the csv files
        query = 'SELECT name FROM sqlite_master WHERE type = "table";'
        df_data = self.execute_sql(query)
        tablenames = df_data['name'].values.tolist()

        for i in tablenames:
            query = 'SELECT * FROM ' + i + ';'
            df_data = self.execute_sql(query)
            self.csvwriter(df_data, i)


    def singletable(self, tablename):
        # Export particular table information to the csv file
        query = 'SELECT * FROM ' + tablename + ';'
        df_data = self.execute_sql(query)
        self.csvwriter(df_data, tablename)
