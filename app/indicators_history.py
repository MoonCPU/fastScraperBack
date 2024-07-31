import requests
from .netGrowth import fetch_company_id
import os
from dotenv import load_dotenv

load_dotenv() 

INVESTIDOR10_API_HISTORICO = os.getenv('INVESTIDOR10_API_HISTORICO')

def fetch_lpa_data(stock_code, years=5):
    # Obtém o ID da empresa
    company_id = fetch_company_id(stock_code)
    if not company_id:
        raise ValueError(f"Company ID not found for stock code: {stock_code}")

    # Monta a URL com o company_id
    url = f'{INVESTIDOR10_API_HISTORICO}/{company_id}/{years}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from {url}. Status code: {response.status_code}")
    
    data = response.json()
    lpa_data = {}
    
    if 'LPA' in data:
        for item in data['LPA']:
            lpa_data[item['year']] = round(item['value'], 2)
    
    return lpa_data