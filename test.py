import requests
from requests.auth import HTTPBasicAuth

# TestRail details
TESTRAIL_URL = "https://yourcompany.testrail.io"
EMAIL = "your_email@company.com"
API_KEY = "your_api_key"

# API endpoint
url = f"{TESTRAIL_URL}/index.php?/api/v2/get_projects"

try:
    response = requests.get(
        url,
        auth=HTTPBasicAuth(EMAIL, API_KEY),
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 200:
        projects = response.json()
        print("Projects in TestRail:")
        for project in projects:
            print(f"ID: {project['id']} | Name: {project['name']}")
    else:
        print("Failed to fetch projects")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

except Exception as e:
    print("Error:", str(e))
