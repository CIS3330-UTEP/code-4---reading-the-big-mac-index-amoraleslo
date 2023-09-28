import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
   query_date = f"(date >= '{year}-01-01' and date <= '{year}-12-31' and iso_a3 == '{country_code.upper()}')"
   query_year = df.query(query_date)
   return round(query_year['dollar_price'].mean(),2)
   

def get_big_mac_price_by_country(country_code):
    query_country = f"(iso_a3 == '{country_code.upper()}')"
    query_ret = df.query(query_country)
    return round(query_ret['dollar_price'].mean(),2)

def get_the_cheapest_big_mac_price_by_year(year):
    query_date = f"(date >= '{year}-01-01' and date <= '{year}-12-31' and iso_a3 == 'ARG')"
    query_ind = df.query(query_date)
    query_min = query_ind['dollar_price'].idxmin()
    result = query_ind.loc[query_min]
    result_text = f"{result['name']}({result['iso_a3']}): {result['dollar_price']}"
    return result_text

    

def get_the_most_expensive_big_mac_price_by_year(year):
    query_date = f"(date >= '{year}-01-01' and date <= '{year}-12-31' and iso_a3 == 'ARG')"
    query_ind = df.query(query_date)
    query_max = query_ind['dollar_price'].idxmax()
    result = query_ind.loc[query_max]
    result_text = f"{result['name']}({result['iso_a3']}): {result['dollar_price']}"
    return result_text

if __name__ == "__main__":
    print(get_big_mac_price_by_year(2022,"arg"))
    print(get_big_mac_price_by_country('arg'))
    print(get_the_cheapest_big_mac_price_by_year(2012))
    print(get_the_most_expensive_big_mac_price_by_year(2012))