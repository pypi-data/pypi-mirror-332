def download_html(url):
    """
    Downloads and returns the HTML content of the given URL.

    Parameters:
    url (str): The URL from which to download the HTML content.

    Returns:
    str: The HTML content of the specified URL.
    """
    response = requests.get(url)
    html = response.text
    return html