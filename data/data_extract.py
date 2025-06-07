"""
    Intel_Stock_History_from_1980_03_17.npy 데이터의 단위, 출처를 알 수 없어 데이터를 새로 다운로드 하였습니다.
    
    데이터 출처: https://finance.yahoo.com/quote/INTC/history/?period1=322185600&period2=1749281445 
    
    위 URL의 HTML에서 주가 데이터를 추출하여 CSV 파일로 변환 했고, 이 코드는 추출을 수행하는 코드입니다.
    
    이 코드는 Claude 3.7 Sonnet이 작성하였습니다.
"""

import os
import csv
from bs4 import BeautifulSoup
from datetime import datetime

def extract_stock_data():
    # Current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # HTML file path
    html_file_path = os.path.join(current_dir, 'Intel Corporation (INTC) Stock Historical Prices & Data - Yahoo Finance.html')
    
    # Output CSV file path
    csv_file_path = os.path.join(current_dir, 'intel_stock_data.csv')
    
    # Read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all rows with the specified class
    data_rows = soup.find_all('tr', class_='yf-1jecxey')
    
    # Prepare data for CSV
    header = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj_Close', 'Volume']
    data_entries = []
    
    # Extract data from each row
    for row in data_rows:
        columns = row.find_all('td', class_='yf-1jecxey')
        if len(columns) >= 7:  # Ensure we have all the required columns
            date = columns[0].text.strip()
            open_price = columns[1].text.strip()
            high_price = columns[2].text.strip()
            low_price = columns[3].text.strip()
            close_price = columns[4].text.strip()
            adj_close = columns[5].text.strip()
            volume = columns[6].text.strip()
            
            # Clean up the data (remove commas from numbers)
            open_price = open_price.replace(',', '')
            high_price = high_price.replace(',', '')
            low_price = low_price.replace(',', '')
            close_price = close_price.replace(',', '')
            adj_close = adj_close.replace(',', '')
            volume = volume.replace(',', '')
            
            # Parse date string into datetime object for sorting
            try:
                # Yahoo Finance format is typically "MMM DD, YYYY" (e.g., "Jun 24, 2022")
                date_obj = datetime.strptime(date, "%b %d, %Y")
                data_entries.append({
                    'date_obj': date_obj,
                    'data': [date, open_price, high_price, low_price, close_price, adj_close, volume]
                })
            except ValueError as e:
                print(f"Error parsing date {date}: {e}")
    
    # Sort data by date in ascending order (oldest first)
    data_entries.sort(key=lambda x: x['date_obj'])
    
    # Prepare final sorted data
    csv_data = [header]
    for entry in data_entries:
        csv_data.append(entry['data'])
    
    # Write the data to a CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)
    
    print(f"Data extracted and saved to {csv_file_path}")
    print(f"Total records: {len(csv_data) - 1}")  # Subtract 1 for the header
    print("Data is sorted in ascending chronological order (oldest first)")

if __name__ == "__main__":
    extract_stock_data()
