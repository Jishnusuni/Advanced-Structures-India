import requests

def fetch_erpnext_data():
    # ERPNext API details
    api_url = "https://your-erpnext-instance.com/api/resource/Item"
    api_key = "your_api_key"
    api_secret = "your_api_secret"
    
    # Set authentication headers
    headers = {
        "Authorization": f"token {api_key}:{api_secret}"
    }
    
    # Make the GET request
    response = requests.get(api_url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        print("Data fetched successfully:")
        print(data)
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")

# Call the function
fetch_erpnext_data()
