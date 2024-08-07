from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

def test_scrape_indicators_endpoint():
    stock_code = "cmig4"
    response = client.post(f"/scrape/indicators/{stock_code}")
    if response.status_code != 200:
        logging.error(f"Failed to fetch indicators for {stock_code}: {response.text}")
    assert response.status_code == 200

def test_scrape_netGrowth_endpoint():
    stock_code = "cmig4"
    response = client.post(f"/scrape/netGrowth/{stock_code}")
    if response.status_code != 200:
        logging.error(f"Failed to fetch net growth for {stock_code}: {response.text}")
    assert response.status_code == 200