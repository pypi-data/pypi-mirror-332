class TeraBoxError(Exception):
    def __init__(self, message="An error occurred in TeraBox"):
        print(f"[TeraBoxError] {message}")
        super().__init__(message)

class DownloadError(TeraBoxError):
    def __init__(self, message="Failed to download the file."):
        print(f"[DownloadError] {message}")
        super().__init__(message)

class LinkNotFoundError(TeraBoxError):
    def __init__(self, message="No valid download link found for the given URL."):
        print(f"[LinkNotFoundError] {message}")
        super().__init__(message)
