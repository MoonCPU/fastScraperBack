import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv() 

INVESTIDOR10_API_ACOES = os.getenv('INVESTIDOR10_API_ACOES')

def scrape_indicators(stock_code):
    url = f'{INVESTIDOR10_API_ACOES}/{stock_code}/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    stock_data = {}
    
    card_body = soup.find('div', class_='_card-body')
    if card_body:
        value_span = card_body.find('span', class_='value')
        if value_span:
            stock_data['Valor Ação'] = float(value_span.get_text(strip=True).replace('R$ ', '').replace(',', '.'))
        else:
            stock_data['Valor Ação'] = 'N/A'
    else:
        stock_data['Valor Ação'] = 'N/A'

    cells = soup.find_all('div', class_='cell')
    for cell in cells:
        indicator_name_elem = cell.find('span', class_='d-flex justify-content-between align-items-center')
        if indicator_name_elem:
            indicator_name = indicator_name_elem.get_text(strip=True)
            value_elem = cell.find('div', class_='value')
            if value_elem:
                value_span = value_elem.find('span')
                if value_span:
                    indicator_value = value_span.get_text(strip=True)
                    #we need to replace comma to dot because float type uses dot
                    indicator_value = indicator_value.replace(',', '.')
                else:
                    indicator_value = 'N/A'
                stock_data[indicator_name] = indicator_value
    
    return stock_data
