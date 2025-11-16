import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = f"http://127.0.0.1:{os.getenv('PORT', 5000)}"

def test_get_base_content():
    """Tests the /base-content endpoint."""
    url = f"{BASE_URL}/base-content"
    print(f"--- Testing GET {url} ---")
    try:
        res = requests.get(url)
        print(f"Status Code: {res.status_code}")
        
        # Try to print JSON response, handle case where it might not be JSON
        try:
            response_json = res.json()
            print("Response JSON:")
            print(json.dumps(response_json, indent=2))
            
            # Assertions to check the structure
            assert isinstance(response_json, dict)
            assert 'type' in response_json
            assert response_json['type'] == 'contentSet'
            assert 'content' in response_json
            assert isinstance(response_json['content'], list)
            print("\\nAssertions passed: Response has the correct ContentSet structure.")
            
        except json.decoder.JSONDecodeError:
            print("Error: Response is not valid JSON.")
            print("Response Text:", res.text)
            
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
    print("-" * 50)


def test_post_submit_code():
    """Tests the /submit endpoint."""
    url = f"{BASE_URL}/submit"
    code = {
        'questionId': 'q1', 
        'files': [{
            'fileName': 'HelloWorld.java', 
            'content': '''public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}'''
        }]
    }
    print(f"--- Testing POST {url} ---")
    try:
        res = requests.post(url, json=code)
        print(f"Status Code: {res.status_code}")
        try:
            print("Response JSON:", res.json())
        except json.decoder.JSONDecodeError:
            print("Response: No JSON returned or not valid JSON.")
            print("Response Text:", res.text)
            
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
    print("-" * 50)


if __name__ == "__main__":
    # Before running this, make sure the backend server is running
    # and the database has been populated by running `python -m test.test_database`
    print("--- Starting API Endpoint Tests ---")
    print(f"Targeting base URL: {BASE_URL}")
    print("-" * 50)
    
    test_get_base_content()
    test_post_submit_code()
