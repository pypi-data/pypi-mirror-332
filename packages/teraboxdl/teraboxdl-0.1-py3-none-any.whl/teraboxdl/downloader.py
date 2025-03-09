import requests
import re
import os
from urllib.parse import urlparse
from .exceptions import TeraBoxError, LinkNotFoundError, DownloadError

class TeraBoxDownloader:
    def __init__(self, session=None):
        self.session = session or requests.Session()
        self.base_url = "https://www.terabox.com"

    def get_direct_link(self, terabox_url):
        """Extracts the direct downloadable video link from TeraBox URL."""
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

        raise LinkNotFoundError()

    def download_video(self, terabox_url, save_path="downloads"):
        """Downloads the video from the extracted direct link."""
        try:
            direct_link = self.get_direct_link(terabox_url)
            print(f"Downloading from: {direct_link}")

            if not os.path.exists(save_path):
                os.makedirs(save_path)

            file_name = os.path.join(save_path, os.path.basename(urlparse(direct_link).path))

            with self.session.get(direct_link, stream=True) as r:
                r.raise_for_status()
                with open(file_name, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)

            print(f"Download complete: {file_name}")
            return file_name

        except LinkNotFoundError as e:
            raise LinkNotFoundError(f"Could not extract a valid download link: {e}")

        except requests.RequestException as e:
            raise DownloadError(f"Failed during download: {e}")

        except Exception as e:
            raise TeraBoxError(f"Unexpected error: {e}")