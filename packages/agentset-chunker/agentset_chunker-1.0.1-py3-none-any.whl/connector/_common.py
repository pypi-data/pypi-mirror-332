import requests
import tempfile
import os
from tqdm import tqdm
from requests.exceptions import RequestException
from urllib.parse import urlparse
import mimetypes
from loguru import logger

def download_file_to_temp(url:str, chunk_size=8192)->str|None:
    """
        Download a file to a temporary folder with progress bar support for large files
        and appends the appropriate file extension.

        Args:
            url (str): URL of the file to download
            chunk_size (int): Size of chunks to download in bytes

        Returns:
            str: Path to the downloaded temporary file with extension
        """
    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        if response.status_code != 200:
            response = requests.get(url, stream=True, timeout=10)  # Fallback to GET

        response.raise_for_status()

        extension = None

        parsed_url = urlparse(url)
        path = parsed_url.path
        if '.' in path:
            extension = '.' + path.split('.')[-1].lower()

        if not extension or len(extension) > 6:
            content_type = response.headers.get('content-type', '')
            if content_type:
                ext = mimetypes.guess_extension(content_type.split(';')[0])
                if ext:
                    extension = ext

        if not extension:
            extension = ''

        with tempfile.NamedTemporaryFile(suffix=extension, delete=False) as temp_file:
            temp_path = temp_file.name

            if response.request.method == 'HEAD':
                response = requests.get(url, stream=True, timeout=10)
                response.raise_for_status()

            total_size = int(response.headers.get('content-length', 0))

            if total_size:
                with tqdm(total=total_size, unit='iB', unit_scale=True,
                          desc="Downloading") as pbar:
                    for chunk in response.iter_content(chunk_size=chunk_size):
                        if chunk:
                            temp_file.write(chunk)
                            pbar.update(len(chunk))
            else:
                logger.info("Downloading (size unknown)...")
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        temp_file.write(chunk)
            return temp_path

    except RequestException as e:
        logger.error(f"Error downloading file: {e}")
        if 'temp_path' in locals() and os.path.exists(temp_path):
            os.remove(temp_path)  # Clean up if download fails
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        if 'temp_path' in locals() and os.path.exists(temp_path):
            os.remove(temp_path)
        return None