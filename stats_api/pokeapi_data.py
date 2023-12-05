from django.core.cache import cache
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("EXTERNAL_API_URL")
CACHE_TIME = int(os.getenv("API_CACHE_TIME"))

def get_berry_data():
    cache_key = 'all_berry_data'
    berry_data = cache.get(cache_key)
    print(f'berry_data: {berry_data}')
    if berry_data is None:
        berry_data = fetch_berry_data_from_api()
        if berry_data:
            cache.set(cache_key, berry_data, CACHE_TIME)

    return berry_data


def fetch_berry_data_from_api():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        berry_names = {item['name']: item['url'] for item in data['results']}
        growth_times = {}
        for berry, url in berry_names.items():
            berry_cache_key = f'berry_detail_{berry}'
            berry_detail = cache.get(berry_cache_key)
            if not berry_detail:
                response = requests.get(url)
                if response.status_code == 200:
                    berry_detail = response.json().get("growth_time")
                    cache.set(berry_cache_key, berry_detail, CACHE_TIME)
            growth_times[berry] = berry_detail
        return growth_times
    except requests.RequestException as e:
        print(f"Error in fetching data from the API: {e}")
        return None
