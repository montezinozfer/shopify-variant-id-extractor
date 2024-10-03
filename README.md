# Shopify Variant ID Extractor

This Python script extracts the variant IDs of all active products in a Shopify store that have the tag `"all"`. Additionally, it excludes any products whose title contains `"(OFFER)"`.

## Features

- Fetches products from a Shopify store using the Shopify API.
- Filters products based on the tag `"all"` and status `"active"`.
- Excludes products that contain `"(OFFER)"` in the product title.
- Returns a list of `variant_ids` for the qualifying products.

## Requirements

- Python 3.x
- The `requests` library for Python (install with pip).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/shopify-variant-id-extractor.git
