"""
Baidu Search Scraper: A Quick Start Example
See more at: https://apify.com/johnvc/apifybaidu?fpr=9n7kx3

This script demonstrates how to use the Baidu Search Scraper Actor
to search Baidu and retrieve structured search results.
"""

import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the ApifyClient with your API token
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Prepare the Actor input
run_input = {
    "query": "Baidu Scraper tutorial",
    "device": "desktop",
    "localization": 1,
    "page": 1,
    "num_results": 10,
    "max_pagination": 3,
}

# Run the Actor and wait for it to finish
run = client.actor("hDVd9ZQQHglV5LZ1A").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)