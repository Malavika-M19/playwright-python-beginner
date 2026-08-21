from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    requests=p.request.new_context()
    response = requests.get("https://automationintesting.online/api/branding")
    response_json = response.json()
    response_code = response.status
    assert response_code == 200, f"Expected status code 200, but got {response_code}"
    assert response_json["name"] == "Shady Meadows B&B", f"Expected name 'Shady Meadows B&B', but got '{response_json['name']}'"
    requests.dispose()