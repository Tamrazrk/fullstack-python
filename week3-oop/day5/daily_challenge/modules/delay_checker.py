import time
import requests


def calculate_load_time(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        if response.status_code == 200:
            load_time = end_time - start_time
            return load_time
        else:
            print(
                f"Error: Unable to fetch the webpage {url}. Status code: {response.status_code}"
            )
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    # Test the function with multiple sites
    sites = [
        "https://www.google.com",
        "https://www.ynet.co.il",
        "https://www.imdb.com",
        "http://learn.di-learning.com",
    ]

    for site in sites:
        load_time = calculate_load_time(site)
        if load_time is not None:
            print(f"Load time for {site}: {load_time:.2f} seconds")
