import pandas as pd  # Importing pandas for data manipulation
import requests  # Importing requests for making HTTP requests
from bs4 import BeautifulSoup  # Importing BeautifulSoup for web scraping
import datetime  # Importing datetime for date manipulation


class Dataweb:
    def __init__(self):
        self.url = "https://es.finance.yahoo.com/quote/BTC-USD/history/"  # URL of the dataweb

    def obtener_datos(self):
        # This method would contain the logic to scrape data from the URL
        try:
            # url, cabecera,
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }

            # Making a GET request to the URL
            respuesta = requests.get(self.url, headers=headers)
            if respuesta.status_code != 200:
                # Print error message if response is not 200
                print("Error en la respuesta del servidor, url NO existe ")

            # print(respuesta.text) # Print the status code of the response
            # Parse the response text using BeautifulSoup
            soup = BeautifulSoup(respuesta.text, 'html.parser')
            # Select the table containing the data
            tabla = soup.select_one('div[data-testid="history-table"] table')
            # print(tabla) # Print the table element

            nombre_columnas = [th.get_text(strip=True)
                               for th in tabla.thead.find_all('th')]
            # List to store column names

            filas = []  # List to store rows of data
            for tr in tabla.tbody.find_all('tr'):
                # List to store data of each row
                columnas = [td.get_text(strip=True)
                            for td in tr.find_all('td')]
                # Check if the number of columns matches the number of column names
                if len(columnas) == len(nombre_columnas):
                    # Append the row data to the list of rows
                    filas.append(columnas)

            df = pd.DataFrame(filas, columns=nombre_columnas).rename(columns={
                'Fecha': 'fecha',
                'Abrir': 'abrir',
                'Máx.': 'maximo',
                'Mín.': 'minimo',
                'CerrarPrecio de cierre ajustado para splits.': 'cerrar',
                'Cierre ajustadoPrecio de cierre ajustado para splits y distribuciones de dividendos o plusvalías.': 'cierre ajustado',
                'Volumen': 'volumen',
            })  # Create a DataFrame from the rows and column names
            # Save the DataFrame to an Excel file

            # Convert numeric columns to float
            df = self.convertir_numericos(df)

            df.to_excel('dataweb_limpio.xlsx')
            return df  # Return the DataFrame

        except Exception as err:
            # Print the error message
            print("Error en la funcion obtener datos")

            print(err)
            # Print the error message

    def convertir_numericos(self, df=pd.DataFrame()):
        df = df.copy()  # Create a copy of the DataFrame to avoid modifying the original one
        if len(df) > 0:
            for col in ('abrir', 'maximo', 'minimo',	'cerrar', 'cierre ajustado', 'volumen'):
                df[col] = (
                    df[col].str.replace(r'["\.", "" ]', '', regex=True)
                    # Remove non-numeric characters
                    .str.replace(r'[",", "." ]', '', regex=True)
                    .astype(float)  # Convert to float
                )
            return df  # Return the modified DataFrame


# if __name__ == "__main__":
