import redis

# connected to redis
redis_connection = redis.Redis(host='localhost', port=16379, db=0)
