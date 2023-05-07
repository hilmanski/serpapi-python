
<div align="center">
<h1 align="center">SerpApi Python Library</h1>
  <img src="https://user-images.githubusercontent.com/78694043/233921372-bb57c347-9005-4b59-8f09-993698a87eb6.svg" width="600" alt="serpapi python library logo">

  <a href="https://badge.fury.io/py/serpapi-python">![Package](https://badge.fury.io/py/serpapi.svg)</a> 
  <a href="https://pepy.tech/project/serpapi-python">![Downloads](https://static.pepy.tech/personalized-badge/serpapi?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)</a> 
  <a href="https://github.com/serpapi/serpapi-python/actions/workflows/python-package.yml">![Buiild](https://github.com/serpapi/serpapi-python/actions/workflows/python-package.yml/badge.svg)</a>
</div>


Integrate search data into your Ruby application. This library is the official wrapper for SerpApi (https://serpapi.com).

SerpApi supports Google, Google Maps, Google Shopping, Baidu, Yandex, Yahoo, eBay, App Stores, and more.

## Installation
Python3 must be installed.

```sh
$ pip install serpapi
```

## Simple usage

```python
import serpapi
client = serpapi.Client({     
  'api_key': "secret_api_key", # set personal API key from serpapi.com/dashboard
  'engine': "google",          # set default search engine
})
results = client.search({
  q: "coffee",          # google query
  location: "Austin,TX" # force the location [optional]
})
print(results['organic_results'])
```

This example runs a search for "coffee" on Google. It then returns the results as a regular Ruby Hash. See the [playground](https://serpapi.com/playground) to generate your own code.

## Advanced Usage
### Search API

TODO update this specification

SerpApi Client uses urllib3 under the hood.
Optionally, rhe HTTP connection can be tuned:
  - timeout : connection timeout by default 60s
  - retries : attempt to reconnect if the connection failed by default: False. 
   serpapi is reliable at 99.99% but your company network might not be as stable.

  ```python
parameter = {
   retries: 5,
   timeout: 4.0,
   # extra user parameters
}
```

for more details: [URL LIB3 documentation]](https://urllib3.readthedocs.io/en/stable/user-guide.html)

## Basic example per search engines

### Search bing
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'bing',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'q': 'coffee',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['organic_results'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_bing_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_bing_test.py)
see: [https://serpapi.com/bing-search-api](https://serpapi.com/bing-search-api)

### Search baidu
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'baidu',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'q': 'coffee',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['organic_results'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_baidu_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_baidu_test.py)
see: [https://serpapi.com/baidu-search-api](https://serpapi.com/baidu-search-api)

### Search yahoo
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'yahoo',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'p': 'coffee',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['organic_results'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_yahoo_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_yahoo_test.py)
see: [https://serpapi.com/yahoo-search-api](https://serpapi.com/yahoo-search-api)

### Search youtube
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'youtube',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'search_query': 'coffee',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['video_results'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_youtube_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_youtube_test.py)
see: [https://serpapi.com/youtube-search-api](https://serpapi.com/youtube-search-api)

### Search walmart
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'walmart',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'query': 'coffee',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['organic_results'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_walmart_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_walmart_test.py)
see: [https://serpapi.com/walmart-search-api](https://serpapi.com/walmart-search-api)

### Search ebay
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'ebay',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'_nkw': 'coffee',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['organic_results'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_ebay_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_ebay_test.py)
see: [https://serpapi.com/ebay-search-api](https://serpapi.com/ebay-search-api)

### Search naver
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'naver',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'query': 'coffee',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['ads_results'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_naver_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_naver_test.py)
see: [https://serpapi.com/naver-search-api](https://serpapi.com/naver-search-api)

### Search home depot
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'home_depot',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'q': 'table',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['products'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_home_depot_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_home_depot_test.py)
see: [https://serpapi.com/home-depot-search-api](https://serpapi.com/home-depot-search-api)

### Search apple app store
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'apple_app_store',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'term': 'coffee',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['organic_results'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_apple_app_store_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_apple_app_store_test.py)
see: [https://serpapi.com/apple-app-store](https://serpapi.com/apple-app-store)

### Search duckduckgo
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'duckduckgo',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'q': 'coffee',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['organic_results'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_duckduckgo_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_duckduckgo_test.py)
see: [https://serpapi.com/duckduckgo-search-api](https://serpapi.com/duckduckgo-search-api)

### Search google
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'google',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'q': 'coffee',
'engine': 'google',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['organic_results'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_test.py)
see: [https://serpapi.com/search-api](https://serpapi.com/search-api)

### Search google scholar
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'google_scholar',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'q': 'coffee',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['organic_results'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_scholar_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_scholar_test.py)
see: [https://serpapi.com/google-scholar-api](https://serpapi.com/google-scholar-api)

### Search google autocomplete
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'google_autocomplete',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'q': 'coffee',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['suggestions'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_autocomplete_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_autocomplete_test.py)
see: [https://serpapi.com/google-autocomplete-api](https://serpapi.com/google-autocomplete-api)

### Search google product
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'google_product',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'q': 'coffee',
'product_id': '4172129135583325756',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['product_results'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_product_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_product_test.py)
see: [https://serpapi.com/google-product-api](https://serpapi.com/google-product-api)

### Search google reverse image
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'google_reverse_image',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'image_url': 'https://i.imgur.com/5bGzZi7.jpg',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['image_sizes'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_reverse_image_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_reverse_image_test.py)
see: [https://serpapi.com/google-reverse-image](https://serpapi.com/google-reverse-image)

### Search google events
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'google_events',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'q': 'coffee',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['events_results'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_events_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_events_test.py)
see: [https://serpapi.com/google-events-api](https://serpapi.com/google-events-api)

### Search google local services
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'google_local_services',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'q': 'Electrician',
'data_cid': 'ChIJOwg_06VPwokRYv534QaPC8g',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['local_ads'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_local_services_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_local_services_test.py)
see: [https://serpapi.com/google-local-services-api](https://serpapi.com/google-local-services-api)

### Search google maps
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'google_maps',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'q': 'pizza',
'll': '@40.7455096,-74.0083012,15.1z',
'type': 'search',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['local_results'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_maps_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_maps_test.py)
see: [https://serpapi.com/google-maps-api](https://serpapi.com/google-maps-api)

### Search google jobs
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'google_jobs',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'q': 'coffee',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['jobs_results'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_jobs_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_jobs_test.py)
see: [https://serpapi.com/google-jobs-api](https://serpapi.com/google-jobs-api)

### Search google play
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'google_play',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'q': 'kite',
'store': 'apps',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['organic_results'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_play_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_play_test.py)
see: [https://serpapi.com/google-play-api](https://serpapi.com/google-play-api)

### Search google images
```python
import serpapi
import pprint
import os

client = serpapi.Client({
'engine': 'google_images',
'api_key': os.getenv("API_KEY")
})
data = client.search({
'engine': 'google_images',
'tbm': 'isch',
'q': 'coffee',
})
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data['images_results'])
# os.getenv("API_KEY") is your secret API Key
# copy/paste from [http://serpapi.com/dashboard] to your bash
# ```export API_KEY="your_secure_api_key"```
```
 * test: [/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_images_test.py](/Users/victor/Project/serpapi/serpapi-python/tests/example_search_google_images_test.py)
see: [https://serpapi.com/images-results](https://serpapi.com/images-results)
    

# Developer Guide
TODO update this section
### Key goals
 - High code quality
 - KISS principles
 - Brand centric instead of search engine based
   - No hard coded logic per search engine
 - Simple HTTP client (lightweight, reduced dependency)
   - No magic default values
   - Thread safe
 - Easy to extends
 - Defensive code style (raise custom exception)
 - TDD
 - Best API coding pratice per platform

### Inspiration
The API design was inpired by the most popular Python packages.
 - urllib3 - https://github.com/urllib3/urllib3
 - Boto3 - https://github.com/boto/boto3

### Quality expectation
 - 0 lint issues using pylint `make lint`
 - 99% code coverage running `make test`
 - 100% test passing: `make test`
 
### Client design: Class diagram
```mermaid
classDiagram
  CustomClient *-- Client
  HttpClient <-- Client
  HttpClient *-- urllib3
  HttpClient *-- ObjectDecoder

  class Client {
    engine: String
    api_key: String
    parameter: Hash
    search()
    html()
    location()
    search_archive()
    account()
  }

  class HttpClient {
    start()
    decode()
  }

  class urllib3 {
    request()
  }
```

## JSON search() : Sequence diagram
```mermaid
sequenceDiagram
    Client->>SerpApi.com: search() : http request 
    SerpApi.com-->>SerpApi.com: query search engine
    SerpApi.com-->>SerpApi.com: parse HTML into JSON
    SerpApi.com-->>Client: JSON payload
    Client-->>Client: decode JSON into Dict
```

## Build flow

This project is automated using a good old Makefile.
To pipe-clean the project run this:
`make`

Open Makefile for more details.
