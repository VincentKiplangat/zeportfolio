import zlib
from django.core.cache import cache

def compress_and_cache(key, data, timeout=300):
    """
    Compresses the data and stores it in the cache.

    :param key: The cache key to store the data under.
    :param data: The data to store (must be a string).
    :param timeout: How long the data should stay in cache, in seconds.
    """
    compressed_data = zlib.compress(data.encode('utf-8'))
    cache.set(key, compressed_data, timeout)

def decompress_from_cache(key):
    """
    Retrieves and decompresses the data from the cache.

    :param key: The cache key to retrieve the data from.
    :return: The decompressed data or None if not found.
    """
    compressed_data = cache.get(key)
    if compressed_data:
        return zlib.decompress(compressed_data).decode('utf-8')
    return None
