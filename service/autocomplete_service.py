from app import redis_cache
from repository import autocomplete_respository
def autoComplete(query, language):
    result = []

   # 레디스에서 해당 쿼리가 prefix인 모든 key 찾기
    for key in redis_cache.scan_iter(f"*{query}*"):
        for value_language in redis_cache.smembers(key):
            if language == byte2str(value_language):
                result.append(byte2str(key))

    return result;

def byte2str(byte):
    return byte.decode('utf-8')



def RDBautoComplete(query, language):
    result = autocomplete_respository.findCompanyName(query, language)
    return result