import time
import requests


def rate_request(method, url, **kwargs):
    """
    A wrapper around requests.request that handles rate limiting (HTTP 429)
    and retries requests that encounter a 429 error using exponential backoff.

    For any HTTP error response other than 429, the function raises an HTTPError
    that includes the full response content as its error message.

    The signature is identical to requests.request.
    Optional parameters in kwargs:
      - max_retries (int): Maximum number of retry attempts (default: 5)
      - backoff_factor (int or float): Factor to calculate the delay between retries (default: 1)

    All other parameters are forwarded directly to requests.request.

    :param method: The HTTP method to use (e.g., "GET", "POST", etc.).
    :param url: The URL to request.
    :param kwargs: Additional parameters for requests.request and retry configuration.
    :return: The Response object on success.
    :raises: HTTPError (with response content) for any non-429 error response,
             or Exception if the maximum number of retries is exceeded.
    """
    max_retries = kwargs.pop("max_retries", 5)
    backoff_factor = kwargs.pop("backoff_factor", 1)
    retries = 0

    while retries <= max_retries:
        try:
            response = requests.request(method, url, **kwargs)
        except requests.exceptions.RequestException as e:
            # Raise network-related errors (ConnectionError, Timeout, etc.) immediately.
            raise

        # If the response indicates rate limiting (HTTP 429), wait and retry.
        if response.status_code == 429:
            retry_after = response.headers.get("Retry-After")
            if retry_after and retry_after.isdigit():
                sleep_time = int(retry_after)
            else:
                sleep_time = backoff_factor * (2**retries)
            print(f"Rate limited (429). Retrying in {sleep_time} seconds...")
            time.sleep(sleep_time)
            retries += 1
            continue

        # For any other error status, do not retry;
        # raise an HTTPError that contains the full response content.
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            error_message = response.text  # Use the full response content
            raise requests.exceptions.HTTPError(
                f"HTTP error {response.status_code}: {error_message}", response=response
            ) from e

        return response

    raise Exception("Maximum number of retries exceeded without success.")
