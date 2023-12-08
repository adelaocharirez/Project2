def get_exchange_rate(source_currency: str, target_currency: str) -> float:
    """ function to simulate getting an exchange rate. """
    
    rates = {
        "USD": {"EUR": 0.85, "GBP": 0.75, "JPY": 110.0, "AUD": 1.30, "CAD": 1.25},
        "EUR": {"USD": 1.18, "GBP": 0.88, "JPY": 129.5, "AUD": 1.53, "CAD": 1.47},
        "GBP": {"USD": 1.34, "EUR": 1.14, "JPY": 147.0, "AUD": 1.74, "CAD": 1.67},
        "JPY": {"USD": 0.0091, "EUR": 0.0077, "GBP": 0.0068, "AUD": 0.012, "CAD": 0.011},
        "AUD": {"USD": 0.77, "EUR": 0.65, "GBP": 0.57, "JPY": 83.0, "CAD": 0.96},
        "CAD": {"USD": 0.80, "EUR": 0.68, "GBP": 0.60, "JPY": 86.5, "AUD": 1.04},
        
    }

    # Return the exchange rate, default to 1 if not found
    return rates.get(source_currency, {}).get(target_currency, 1)
