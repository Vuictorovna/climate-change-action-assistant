# WEB SCRAPER (PDF COLLECTOR)
import requests
from bs4 import BeautifulSoup
import os

# Define the Climate Change Consortium (CCC) publications URL
ccc_url = "https://www.theccc.org.uk/publications/"

# Send an HTTP GET request to the CCC website
response = requests.get(ccc_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup (soup)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find links to PDF publications on the page
    pdf_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.endswith('.pdf'):
            pdf_links.append(href)

    # Create a directory to store downloaded PDFs
    os.makedirs('pdfs', exist_ok=True)

    # Download PDFs and save them to the 'pdfs' directory
    for pdf_link in pdf_links:
        pdf_url = pdf_link
        pdf_filename = os.path.join('pdfs', pdf_url.split('/')[-1])

        # Send an HTTP GET request to download the PDF
        pdf_response = requests.get(pdf_url)
        with open(pdf_filename, 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)
        
        print(f"Downloaded: {pdf_filename}")
else:
    print("Failed to retrieve the CCC publications page.")
