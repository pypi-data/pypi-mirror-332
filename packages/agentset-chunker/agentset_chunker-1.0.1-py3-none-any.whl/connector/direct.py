from ._common import download_file_to_temp


def direct(url:str)->str:
    """
    Downloads a file from the given URL to a temporary location.

    Args:
        url (str): The URL of the file to be downloaded.

    Returns:
        str: The path to the downloaded file in the temporary location.
    """
    return download_file_to_temp(url)






