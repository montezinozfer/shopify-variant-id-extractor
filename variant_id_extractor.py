import requests

# Shopify API credentials (Replace with your own credentials)
API_KEY = 'your_api_key'
PASSWORD = 'your_access_token'
SHOP_NAME = 'your_shop_name'  # e.g., 'myshop.myshopify.com'

# Shopify API URL to get products with the "all" tag
url = f"https://{SHOP_NAME}/admin/api/2023-04/products.json"

# Parameters to filter active products with the "all" tag
params = {
    "status": "active",  # Only active products
    "tag": "all"         # Only products with the "all" tag
}

# Headers for authentication with the Shopify API
headers = {
    "X-Shopify-Access-Token": PASSWORD
}

# Make the GET request to the Shopify API
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    products_data = response.json()

    # Extract Variant IDs from products that have the "all" tag
    # and omit products with "(OFFER)" in the title
    variant_ids = []
    for product in products_data['products']:
        # Check that the product has the "all" tag and does not contain "(OFFER)" in the title
        if 'all' in product['tags'] and '(OFFER)' not in product['title']:
            for variant in product['variants']:
                variant_ids.append(variant['id'])

    # Print the Variant IDs found
    print("Variant IDs of products with the 'all' tag and without '(OFFER)' in the title:")
    print(variant_ids)
else:
    print(f"Error in request: {response.status_code}")
