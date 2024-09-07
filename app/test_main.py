from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

def test_scrape_indicators_endpoint():
    stock_code = "cmig4"
    response = client.get(f"/scrape/indicators/{stock_code}")
    
    assert response.status_code == 200
    
    response_json = response.json()
    assert "indicators" in response_json
    
    # Expected keys without stock code
    expected_key_patterns = {
        "Valor Ação", "P/L", "P/RECEITA (PSR)", "P/VP", "PAYOUT",
        "MARGEM LÍQUIDA", "MARGEM BRUTA", "MARGEM EBIT", "MARGEM EBITDA",
        "EV/EBITDA", "EV/EBIT", "P/EBITDA", "P/EBIT", "P/ATIVO", "P/CAP.GIRO",
        "P/ATIVO CIRC LIQ", "VPA", "LPA", "GIRO ATIVOS", "ROE", "ROIC", "ROA",
        "DÍVIDA LÍQUIDA / PATRIMÔNIO", "DÍVIDA LÍQUIDA / EBITDA", "DÍVIDA LÍQUIDA / EBIT",
        "DÍVIDA BRUTA / PATRIMÔNIO", "PATRIMÔNIO / ATIVOS", "PASSIVOS / ATIVOS", 
        "LIQUIDEZ CORRENTE", "CAGR RECEITAS 5 ANOS", "CAGR LUCROS 5 ANOS"
    }
    
    dividend_key_pattern = f"DIVIDEND YIELD - {stock_code.upper()}"
    
    expected_key_patterns.add(dividend_key_pattern)
    
    actual_keys = set(response_json["indicators"].keys())
    unexpected_keys = [key for key in actual_keys if key not in expected_key_patterns]

    assert not unexpected_keys, f"Unexpected keys found: {unexpected_keys}"

def test_scrape_netGrowth_endpoint():
    stock_code = "cmig4"
    response = client.get(f"/scrape/netGrowth/{stock_code}")
    
    assert response.status_code == 200
    
    response_json = response.json()
    assert "net_growth" in response_json
    
    required_keys = {
        "net_revenue", "net_profit", "net_worth", "year"
    }
    
    optional_keys = {
        "cost", "gross_profit", "ebitda", "ebit", "tax", "quarter"
    }
    
    net_growth_data = response_json["net_growth"]
    for entry in net_growth_data:
        actual_keys = set(entry.keys())
        missing_required_keys = required_keys - actual_keys
        unexpected_keys = actual_keys - (required_keys | optional_keys)

        assert not missing_required_keys, f"Missing required keys: {missing_required_keys}"
        assert not unexpected_keys, f"Unexpected keys: {unexpected_keys}"
        
        # Check that all optional keys exist if they are present
        for key in optional_keys:
            if key in entry:
                assert entry[key] is not None, f"Optional key {key} should not be None"