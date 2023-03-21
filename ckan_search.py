import sys
import requests
from typing import Dict, NoReturn


def make_requests(query: str) -> Dict[str, object]:
    """Function to make API request and return json

    Args:
        query (str): query string  for search

    Raises:
        Exception: raised when API call is unsuccessful

    Returns:
        dict[str, object]: ckan response in json
    """

    payload = {
            'q': query,
            'rows': 20
        }
    response = requests.get(
        url='https://www.govdata.de/ckan/api/3/action/package_search',
        params=payload
        )
    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code)
        raise Exception("Error with API call")


def format_data(ckan_data: Dict[str, object]) -> NoReturn:
    """To format ckan data and print title

    Args:
        ckan_data (dict[str, object]): ckan response data in json

    Returns:
        NoReturn: returns no value
    """
    result_list = ckan_data['result']['results']

    for result in result_list:
        title = result['title']
        print(f"Title: {title}")


if __name__ == "__main__":
    try:
        query = sys.argv[1]
    except IndexError:
        query = input("Search parameter not added! try again: ")

    ckan_data = make_requests(query)

    no_of_results = ckan_data['result']['count']
    if no_of_results > 0:
        format_data(ckan_data)
    else:
        print("No match found!")
