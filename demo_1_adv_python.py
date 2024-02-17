import requests
from bs4 import BeautifulSoup

# Define login credentials
username = '910392'
password = 'Jai@83209320'

# Construct dictionary containing login credentials
login_data = {
    'username': username,
    'password': password,
    'submit': 'Log in'
}

# Define the login URL of the Moodle site
login_url = 'https://moodle.cestarcollege.com/moodle/login/index.php'

# Initialize session object
session = requests.Session()

# Send POST request to login URL with credentials
response = session.post(login_url, data=login_data)

# Check if login was successful (status code 200)
if response.status_code == 200:
    # Define URL of the page you want to scrape after login (e.g., site news)
    scrape_url = 'https://moodle.cestarcollege.com/moodle/?redirect=0'

    # Send GET request to access protected page after login
    page_response = session.get(scrape_url)

    # Parse HTML content of the page using BeautifulSoup
    if page_response.status_code == 200:
        soup = BeautifulSoup(page_response.text, 'html.parser')
        
        # Scraping code here...
    else:
        print("Failed to retrieve data from the Moodle site.")
else:
    print("Login failed. Please check your credentials.")
