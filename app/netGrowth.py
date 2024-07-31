import requests
from bs4 import BeautifulSoup
import re
import os
from dotenv import load_dotenv

load_dotenv() 

INVESTIDOR10_API_ACOES = os.getenv('INVESTIDOR10_API_ACOES')
INVESTIDOR10_API_NETGROWTH = os.getenv('INVESTIDOR10_API_NETGROWTH')

def fetch_company_id(stock_code):
    url = f'{INVESTIDOR10_API_ACOES}/{stock_code}/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        script_tags = soup.find_all('script')
        
        for script in script_tags:
            if 'getJsonPayoutIndicators' in script.text:
                match = re.search(r"const companyId = '(\d+)'", script.text)
                if match:
                    return match.group(1)

    return None 

def scrape_netGrowth(stock_code, period=3650):
    company_id = fetch_company_id(stock_code)
    if not company_id:
        raise ValueError(f"Company ID not found for stock code: {stock_code}")
    #call the api to get the history of network growth in the last 10 years (3650 days)
    url = f'{INVESTIDOR10_API_NETGROWTH}/{company_id}/{period}/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from {url}. Status code: {response.status_code}")
    data = response.json()
    return data

# stock_code = "kepl3"
# data = scrape_netGrowth(stock_code, period=3650)
# print(data)