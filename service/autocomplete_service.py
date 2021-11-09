from app import redis_cache

def autoComplete(query, language):
    result = []

   # 레디스에서 해당 쿼리가 prefix인 모든 key 찾기
    for key in redis_cache.scan_iter(f"*{query}*"):
        # 요청온 언어와 같은 언어(value)의 key들만 result에 담는다.
        if byte2str(redis_cache.get(key)) == language:
            result.append(byte2str(key))


    return result;

def byte2str(byte):
    return byte.decode('utf-8')

