import requests
import re
import os
from urllib.parse import urlparse
from .exceptions import TeraBoxError, LinkNotFoundError, DownloadError

class TeraBoxDownloader:
    """
    A class to download videos from TeraBox links. Supports multiple TeraBox link formats.
    
    Attributes:
        session (requests.Session): A session object for making HTTP requests.
        base_url (str): The base URL for TeraBox.
        supported_domains (list): List of supported TeraBox domains.
    """

    def __init__(self, session=None):
        """
        Initializes the TeraBoxDownloader with an optional session object.

        Args:
            session (requests.Session, optional): A session object for making HTTP requests. 
                                                  If not provided, a new session will be created.
        """
        self.session = session or requests.Session()
        self.base_url = "https://www.terabox.com"
        self.supported_domains = [
            "terabox.com",
            "1024terabox.com",
            "teraboxlink.com",
            "freeterabox.com"
        ]

    def _validate_url(self, url):
        """
        Validates if the provided URL is a supported TeraBox link.

        Args:
            url (str): The URL to validate.

        Returns:
            bool: True if the URL is valid, False otherwise.
        """
        parsed_url = urlparse(url)
        return any(domain in parsed_url.netloc for domain in self.supported_domains)

    def get_direct_link(self, terabox_url):
        """
        Extracts the direct downloadable video link from a TeraBox URL.

        Args:
            terabox_url (str): The TeraBox URL to extract the direct link from.

        Returns:
            str: The direct download link.

        Raises:
            TeraBoxError: If the URL is invalid or the page cannot be fetched.
            LinkNotFoundError: If the direct link cannot be extracted.
        """
        if not self._validate_url(terabox_url):
            raise TeraBoxError("Unsupported TeraBox URL format.")

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        try:
            response = self.session.get(terabox_url, headers=headers)
            response.raise_for_status()  # Raise an error for HTTP failures
        except requests.RequestException as e:
            raise TeraBoxError(f"Failed to fetch page: {e}")

        # Extract the direct MP4 link (this pattern may change)
        match = re.search(r'"(https://[^"]+?\.mp4)"', response.text)
        if match:
            return match.group(1)

        raise LinkNotFoundError("Direct download link not found in the page.")

    def download_video(self, terabox_url, save_path="downloads", file_name=None):
        """
        Downloads the video from the extracted direct link.

        Args:
            terabox_url (str): The TeraBox URL to download the video from.
            save_path (str, optional): The directory to save the downloaded file. Defaults to "downloads".
            file_name (str, optional): The name of the file to save. If not provided, the name will be extracted from the URL.

        Returns:
            str: The path to the downloaded file.

        Raises:
            LinkNotFoundError: If the direct link cannot be extracted.
            DownloadError: If the download fails.
            TeraBoxError: If an unexpected error occurs.
        """
        try:
            direct_link = self.get_direct_link(terabox_url)
            print(f"Downloading from: {direct_link}")

            if not os.path.exists(save_path):
                os.makedirs(save_path)

            # Use provided file name or extract from URL
            if not file_name:
                file_name = os.path.basename(urlparse(direct_link).path)
            else:
                file_name = f"{file_name}.mp4" if not file_name.endswith(".mp4") else file_name

            file_path = os.path.join(save_path, file_name)

            with self.session.get(direct_link, stream=True) as r:
                r.raise_for_status()
                with open(file_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)

            print(f"Download complete: {file_path}")
            return file_path

        except LinkNotFoundError as e:
            raise LinkNotFoundError(f"Could not extract a valid download link: {e}")

        except requests.RequestException as e:
            raise DownloadError(f"Failed during download: {e}")

        except Exception as e:
            raise TeraBoxError(f"Unexpected error: {e}")

    def batch_download(self, terabox_urls, save_path="downloads"):
        """
        Downloads multiple videos from a list of TeraBox URLs.

        Args:
            terabox_urls (list): A list of TeraBox URLs to download.
            save_path (str, optional): The directory to save the downloaded files. Defaults to "downloads".

        Returns:
            list: A list of paths to the downloaded files.

        Raises:
            TeraBoxError: If any error occurs during the batch download.
        """
        downloaded_files = []
        for url in terabox_urls:
            try:
                file_path = self.download_video(url, save_path)
                downloaded_files.append(file_path)
            except Exception as e:
                print(f"Failed to download {url}: {e}")
        return downloaded_files

    def set_session(self, session):
        """
        Sets a custom session object for making HTTP requests.

        Args:
            session (requests.Session): The session object to use.
        """
        self.session = session

    def clear_session(self):
        self.session = requests.Session()
