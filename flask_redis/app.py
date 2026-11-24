import time
import socket
import redis
from flask import Flask, make_response

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count() -> int:
    return int(cache.get('hits') or 0)

def incr_hit_count() -> int:
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/metrics')
def metrics():
    data = (
        "# HELP view_count Flask-Redis-App visit counter\n"
        "# TYPE view_count counter\n"
        f'view_count{{service="Flask-Redis-App"}} {get_hit_count()}\n'
    )
    response = make_response(data, 200)
    response.mimetype = "text/plain"
    return response

@app.route('/')
def hello():
    incr_hit_count()
    count = get_hit_count()
    return 'Hello World! I have been seen {} times. My name is: {}\n'.format(count, socket.gethostname())
