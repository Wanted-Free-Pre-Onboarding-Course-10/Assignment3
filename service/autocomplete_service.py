from redis import StrictRedis
cache = StrictRedis()

def autoComplete(prefix):
    result = []

    # bytes -> string
    for key in cache.scan_iter(f"{prefix}*"):
        result.append(key.decode('utf-8'))

    return result;
