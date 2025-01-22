import requests

def extract_data(api_url):
    try:
        # Send a GET request to the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        # Extract and print relevant data (customize as needed)
        for item in data.get('results', []):
            name = item.get('name')
            address = item.get('address', 'N/A')
            print(f"Name: {name}, Address: {address}")

        return data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example API endpoint
api_url = "https://api.example.com/data"
extracted_data = extract_data(api_url)