# Example: google_autocomplete search engine
import pytest
import os
import serpapi

def test_search_google_autocomplete(client):
  data = client.search({
      'engine': 'google_autocomplete',
      'q': 'coffee',
  })
  assert data.get('error') is None
  assert data['suggestions']

# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
