import sqlite3

def city_kpi(city: str):
    """Calculates the average monthly spend for a given city securely."""
    conn = sqlite3.connect('data/db/analytics.db')
    cursor = conn.cursor()
    
    # Using parameterized SQL to prevent injection
    query = "SELECT AVG(monthly_spend) FROM customers_raw WHERE city = ?"
    cursor.execute(query, (city,))
    
    result = cursor.fetchone()[0]
    conn.close()
    return result

if __name__ == "__main__":
    print(f"Average Spend in Mumbai: {city_kpi('Mumbai')}")
    
    # Injection attempt: This will return None because no city matches this literal string
    print(f"Injection Attempt result: {city_kpi(\"Mumbai' OR 1=1 --\")}")