import redis
import json

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)


def get_cache(key):
    data = r.get(key)
    if data:
        return json.loads(data)
    return None


def set_cache(key, value, expire=60):
    r.set(key, json.dumps(value, default=str), ex=expire)


def delete_cache(key):
    r.delete(key)