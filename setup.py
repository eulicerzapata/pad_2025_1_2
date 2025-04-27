from setuptools import setup, find_packages

setup(
    name="edu.pad",
    version="0.0.1",
    author="Dawin Salazar Oviedo", 
    author_email="dawin.salazar@iudigital.edu.co",
    description = """Python Web Scraper & Data Extractor: a tool to automatically collect and parse web data
                    Utilizes requests, BeautifulSoup, and lxml for efficient HTTP requests and HTML parsing.
                    Supports configurable scraping rules, robust error handling, and dynamic content via Selenium.
                    Outputs structured data in JSON and CSV formats for seamless integration with data pipelines.
                    Modular architecture enables easy extension, scheduling, and integration into larger workflows.""",
    py_modules=["Actividad1", "Actividad2", "Actividad3", "Actividad4"],
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "beautifulsoup4"
    ]
    
  )