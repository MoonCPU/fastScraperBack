from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app  # Adjust the import according to your project structure

client = TestClient(app)

@patch('main.scrape_indicators')
@patch('main.scrape_netGrowth')
def test_scrape_and_return_data(mock_scrape_indicators, mock_scrape_netGrowth):
    # Mock the return value of scrape_indicators and scrape_netGrowth
    mock_scrape_indicators.return_value = {"P/L": "4,38", "P/RECEITA (PSR)": "0,98"}
    mock_scrape_netGrowth.return_value = {"2021": "1000", "2020": "900"}

    response = client.post("/scrape/test_stock_code")
    assert response.status_code == 200
    assert response.json() == {
        "indicators": {
        "Valor Ação": 10.56,
        "P/L": "7.60",
        "P/RECEITA (PSR)": "1.17",
        "P/VP": "2.57",
        "DIVIDEND YIELD - KEPL3": "9.62%",
        "PAYOUT": "73.22%",
        "MARGEM LÍQUIDA": "15.46%",
        "MARGEM BRUTA": "29.93%",
        "MARGEM EBIT": "19.86%",
        "MARGEM EBITDA": "22.23%",
        "EV/EBITDA": "4.72",
        "EV/EBIT": "5.29",
        "P/EBITDA": "5.28",
        "P/EBIT": "5.91",
        "P/ATIVO": "1.25",
        "P/CAP.GIRO": "3.40",
        "P/ATIVO CIRC LIQ": "-4.00",
        "VPA": "4.11",
        "LPA": "1.39",
        "GIRO ATIVOS": "1.06",
        "ROE": "33.83%",
        "ROIC": "23.50%",
        "ROA": "16.45%",
        "DÍVIDA LÍQUIDA / PATRIMÔNIO": "-0.27",
        "DÍVIDA LÍQUIDA / EBITDA": "-0.56",
        "DÍVIDA LÍQUIDA / EBIT": "-0.63",
        "DÍVIDA BRUTA / PATRIMÔNIO": "0.42",
        "PATRIMÔNIO / ATIVOS": "0.49",
        "PASSIVOS / ATIVOS": "0.51",
        "LIQUIDEZ CORRENTE": "2.15",
        "CAGR RECEITAS 5 ANOS": "22.60%",
        "CAGR LUCROS 5 ANOS": "46.06%"
    },
        "net_growth": [
        {
            "net_revenue": 594762000,
            "cost": -432848000,
            "gross_profit": 161915008,
            "ebitda": 98300000,
            "ebit": 84120000,
            "tax": -16590000,
            "net_profit": 62100000,
            "net_worth": 364081984,
            "year": "2013",
            "quarter": "1"
        },
        {
            "net_revenue": 905841040,
            "cost": -687930000,
            "gross_profit": 217920000,
            "ebitda": 160970000,
            "ebit": 143440000,
            "tax": -2730000,
            "net_profit": 132690000,
            "net_worth": 508814016,
            "year": "2014",
            "quarter": "1"
        },
        {
            "net_revenue": 705979016,
            "cost": -615190000,
            "gross_profit": 90797000,
            "ebitda": 28820000,
            "ebit": 3700000,
            "tax": 11700000,
            "net_profit": 6240000,
            "net_worth": 491361984,
            "year": "2015",
            "quarter": "1"
        },
        {
            "net_revenue": 475298000,
            "cost": -442600000,
            "gross_profit": 32704000,
            "ebitda": -23340000,
            "ebit": -48630000,
            "tax": 16510000,
            "net_profit": -22120000,
            "net_worth": 468852000,
            "year": "2016",
            "quarter": "1"
        },
        {
            "net_revenue": 578374960,
            "cost": -529950000,
            "gross_profit": 48428000,
            "ebitda": -12750000,
            "ebit": -39410000,
            "tax": 2940000,
            "net_profit": -34252000,
            "net_worth": 435348992,
            "year": "2017",
            "quarter": "1"
        },
        {
            "net_revenue": 576300032,
            "cost": -492939000,
            "gross_profit": 83360000,
            "ebitda": 48420000,
            "ebit": 20990000,
            "tax": -7010000,
            "net_profit": 8280000,
            "net_worth": 441024992,
            "year": "2018",
            "quarter": "1"
        },
        {
            "net_revenue": 583462000,
            "cost": -438280000,
            "gross_profit": 145202000,
            "ebitda": 69640000,
            "ebit": 52430000,
            "tax": -9950000,
            "net_profit": 37570000,
            "net_worth": 467380000,
            "year": "2019",
            "quarter": "1"
        },
        {
            "net_revenue": 671240000,
            "cost": -508730000,
            "gross_profit": 162520000,
            "ebitda": 108750000,
            "ebit": 80430000,
            "tax": -21520000,
            "net_profit": 67660000,
            "net_worth": 517650000,
            "year": "2020",
            "quarter": "1"
        },
        {
            "net_revenue": 1226180000,
            "cost": -894700000,
            "gross_profit": 331480000,
            "ebitda": 236150000,
            "ebit": 204880000,
            "tax": -52340000,
            "net_profit": 154630000,
            "net_worth": 461630000,
            "year": "2021",
            "quarter": "1"
        },
        {
            "net_revenue": 1815398000,
            "cost": -1153215000,
            "gross_profit": 662183000,
            "ebitda": 416160000,
            "ebit": 518147000,
            "tax": -137260000,
            "net_profit": 382472000,
            "net_worth": 597270000,
            "year": "2022",
            "quarter": "1"
        },
        {
            "net_revenue": 1512134000,
            "cost": -1063286000,
            "gross_profit": 448848000,
            "ebitda": 336726000,
            "ebit": 301777000,
            "tax": -60502000,
            "net_profit": 245214000,
            "net_worth": 726203000,
            "year": "2023",
            "quarter": "1"
        },
        {
            "net_revenue": 1615978000,
            "net_profit": 249775000,
            "net_worth": 738241000,
            "year": "ÚLT 12M"
        }
    ]
    }

def test_scrape_and_return_data_missing_stock_code():
    response = client.post("/scrape/")
    assert response.status_code == 404

@patch('main.scrape_indicators', side_effect=Exception("Scraping failed"))
def test_scrape_and_return_data_scraping_exception(mock_scrape_indicators):
    response = client.post("/scrape/test_stock_code")
    assert response.status_code == 500
    assert response.json() == {"detail": "Scraping failed"}