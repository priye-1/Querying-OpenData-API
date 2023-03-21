# Querying OpenData APIs
Python script tool that can be used to query the [GovData.de](https://www.govdata.de/)  [CKAN](https://ckan.org/) API located at `https://www.govdata.de/ckan/api`.

### Work-flow
* The tool searches using the [package_search](https://docs.ckan.org/en/2.8/api/index.html#ckan.logic.action.get.package_search) action.
* The tool can be called like this: `python3 ckan_search.py <SEARCH_TERM>`. `SEARCH_TERM` is used as the `q` parameter of the query.
* The tool prints the `title` attribute of the *first 20* matches.
* The tool prints a message if no matches were found.

## Getting started   
### Installation

- Clone repository with HTTPS

    ```bash
     https://github.com/priye-1/Querying-OpenData-API.git
    ```

- Setup virtual environment with  python venv

    ```bash
    python -m venv .venv
    ```
- Activate the Virtual environment
    ```bash
    {path to desired directory} source .venv/bin/activate
    ```

- Install requirements

    ```terminal
    # use dev or production requirments depending on location
    pip install -r > requirements.txt
    ```

## Running Scripts
- To run the program, type command:

    ```terminal
    python ckan_search.py <SEARCH_TERM>
    ```
