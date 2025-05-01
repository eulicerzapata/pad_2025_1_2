import pandas as pd # Importing pandas for data manipulation
import requests # Importing requests for making HTTP requests
from bs4 import BeautifulSoup # Importing BeautifulSoup for web scraping
import datetime # Importing datetime for date manipulation

class Dataweb:
    def __init__(self):
        self.url = "https://es.finance.yahoo.com/quote/BTC-USD/history/" # URL of the dataweb
        
    def obtener_datos(self):
        # This method would contain the logic to scrape data from the URL
        try:
            # url, cabecera,
            headers = {
              'User-Agent': 'Mozilla/5.0' 
              }
            
            respuesta = requests.get(self.url, headers=headers) # Making a GET request to the URL  
            if respuesta.status_code != 200:
                  print("Error en la respuesta del servidor, url NO existe ") # Print error message if response is not 200
              
            # print(respuesta.text) # Print the status code of the response
            soup = BeautifulSoup(respuesta.text, 'html.parser') # Parse the response text using BeautifulSoup
            tabla = soup.select_one('div[data-testid="history-table"] table') # Select the table containing the data
            print(tabla) # Print the table element  
           
        except Exception as err:
            print("Error en la funcion obtener datos") # Print the error message
            
        
     
        
dw = Dataweb() # Dataweb object
# print(dw.url) # Print the URL of the dataweb
dw.obtener_datos() # Call the method to obtain data
     