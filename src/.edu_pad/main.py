
from dataweb import Dataweb  # Import the Dataweb class from dataweb module
import pandas as pd  # Import pandas for data manipulation


def main():
    dataweb = Dataweb()  # Create an instance of the Dataweb class
    
    df = dataweb.obtener_datos()  # Call the obtener_datos method to get data
    
    df.to_csv('data_web.csv', index=False)  # Save the DataFrame to a CSV file
    
if __name__ == "__main__":
        main()  # Call the main function when the script is run
   
    
        