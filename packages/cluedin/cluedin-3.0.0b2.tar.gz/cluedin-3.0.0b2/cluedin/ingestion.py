import time
from typing import Any, Generator

import requests

from .context import Context
from .env import CLUEDIN_REQUEST_TIMEOUT_IN_SECONDS


def post(
    context: Context,
    url: str,
    collection: list[Any],
    batch_size: int = 10_000,
    delay_in_seconds: int = 0
) -> Generator[dict[str, Any], None, None]:
    """Send a POST request to CluedIn.

    Args:
        context (Context): Context object.
        url (str): URL to send the request to.
        collection (list): Collection of entities.
        batch_size (int): Batch size.
        delay_in_seconds (int): Delay between batches in seconds.

    Returns:
        Generator[dict[str, Any], None, None]: Generator of responses.
    """
    headers = {
        'Authorization': f'Bearer {context.access_token}'
    }

    def generate_batches(iterator, batch_size):
        batch = []
        for item in iterator:
            batch.append(item)
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch:
            yield batch

    for batch in generate_batches(collection, batch_size):
        response = requests.post(
            url=url,
            json=batch,
            headers=headers,
            timeout=CLUEDIN_REQUEST_TIMEOUT_IN_SECONDS,
            verify=context.verify_tls
        )
        response.raise_for_status()
        yield {
            'payload': batch,
            'response': response.json()
        }
        if delay_in_seconds:
            time.sleep(delay_in_seconds)
