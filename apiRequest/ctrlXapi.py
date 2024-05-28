import requests
import json
import urllib3

# Disable warnings for self-signed certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Function to obtain the token
def get_token():
    url = "http://192.168.1.1/identity-manager/api/v1/auth/token"
    headers = {
        "content-type": "application/json"
    }
    payload = {
        "name": "boschrexroth",
        "password": "boschrexroth"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Extract the token from the response
    token = response.json().get('access_token')
    if not token:
        raise ValueError("Token not found in response")

    return token

# Function to browse the axes
def browse_axes(token):
    url = "https://192.168.1.1/automation/api/v1.0/motion/axs?type=browse"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json, text/plain, */*",
        "content-type": "application/json"
    }

    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()  # Raise an exception for HTTP errors

    return response.json()

# Function to get axis value
def get_axis_value(token, axis_name):
    url = f"https://192.168.1.1/automation/api/v1.0/motion/axs/{axis_name}/state/values/actual/pos/cm"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json, text/plain, */*",
        "content-type": "application/json"
    }

    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()  # Raise an exception for HTTP errors

    return response.json()

# Main execution
if __name__ == "__main__":
    try:
        token = get_token()
        print("Token obtained:", token)

        axis_data = browse_axes(token)
        print("Axis Data:", json.dumps(axis_data, indent=4))

        # Assuming axis_data['value'] contains the list of axis names
        axis_values = {}
        for axis in axis_data.get('value', []):
            axis_value = get_axis_value(token, axis)
            axis_values[axis] = axis_value
            print(f"Value for {axis}:", json.dumps(axis_value, indent=4))

        # Print all axis values
        print("All Axis Values:", json.dumps(axis_values, indent=4))

    except requests.exceptions.RequestException as e:
        print("HTTP Request failed:", e)
    except ValueError as e:
        print("Error:", e)
