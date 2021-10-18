#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 08:31:55 2021

@author: jessicaspencer
"""
import requests
import pandas as pd
from pandas import json_normalize
import fiona

outfile_name = 'outfile.csv'

""" A class that can be used to represent api call and conversion to .csv """
class ApiCsv:
    def __init__(self):
        """ Initialize attributes needed """
        self.url = 'https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/MapServer/8/query?where=1%3D1&outFields=*&outSR=4326&f=json'
        
    def make_api_call(self):
        #Make an API call, print status code, store response in variable.
        url= self.url
        r = requests.get(url)
        print(f"Status code:{r.status_code}")
        #Store API in response variable
        self.dictr = r.json()
    
    def dictr_to_df(self):
        #Convert the features dict within the data to dataframe (normalize it)
        dictr = self.dictr
        recs = dictr['features']
        self.df = json_normalize(recs)
        #print df just for checking the normalization 
        print(self.df)
        
    def indexNames_to_cols(self):
        #The df has the col names in the index, this function places those names in the columns
        df = self.df 
        cols = [] #Making a list for just column names
        for column in df:
            #print(column) before adding column names to list
            cols.append(column)
        #Give cols to dataframe and drop the index
        df.columns=cols
        self.df =df.reset_index(drop=True)
        return self.df 
    
    def convert_to_three(self):
        #instead of the 25 columns in the data this gets lattitude,longitude,and attr for the offense for simplcity of smaller data
        df = self.df 
        # Create the pandas DataFrame
        df2 = pd.DataFrame(df, columns = ['attributes.LONGITUDE', 'attributes.LATITUDE','attributes.OFFENSE']).reset_index(drop=True)
        #rename columns
        df2 = df2.rename(columns={"attributes.LONGITUDE": "attributes_LONGITUDE", "attributes.LATITUDE": "attributes_LATITUDE",
                          "attributes.OFFENSE": "attributes_OFFENSE"}).reset_index(drop=True)
        self.df = df2
        return self.df
    
        
    def Execute(self):
        #Function that runs the functions and converts the df to .csv file within your dictory
        self.make_api_call()
        self.dictr_to_df()
        self.indexNames_to_cols()
        self.df =self.convert_to_three()
        #export to .csv
        self.df.to_csv('out.csv',encoding='utf-8', index=False)


####################################################################################

""" A class that can be used to represent .csv conversion with fiona to POINT Shapfile format """
class Csv_to_Shp:
    def __init__(self):
        """ import points from csv file """
        self.pointDf = pd.read_csv('out.csv',header=0)
        #print(self.pointDf.head())
    
    def schema(self):
        #DEFINE SCHEMA
        # define schema
        self.schema = {
            'geometry':'Point',
            'properties':[('Name','str')]
        }
    
    def to_shp(self):
        #Function to convert to POINT shp file with fiona
        #open a fiona object
        #CREATES THE .SHP FILE
        pointDf = self.pointDf
        pointShp = fiona.open('out.shp', mode='w', driver='ESRI Shapefile',
                  schema = self.schema, crs = "EPSG:4326")
        
        #iterate over each row in the dataframe and save record
        for index, row in pointDf.iterrows():
            rowDict = {
                'geometry' : {'type':'Point',
                             'coordinates': (row.attributes_LONGITUDE,row.attributes_LATITUDE)},
                'properties': {'Name' : row.attributes_OFFENSE},
            }
            pointShp.write(rowDict)
        #close fiona object
        pointShp.close()
        
    def Execute(self):
        self.schema()
        self.to_shp()
        
        
####################### Runs the class to convert to csv
a = ApiCsv()
a.Execute()
####################### Runs the class to convert to shp file 
b = Csv_to_Shp()
b.Execute()
