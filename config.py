from dotenv import load_dotenv
from datetime import timedelta
import os
import redis

load_dotenv()

class ApplicationConfig:
    SECRET_KEY ="0x11100111"
    SESSION_TYPE = "redis"
    #SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=1)
    SESSION_COOKIE_HTTPONLY=True,
    REMEMBER_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Strict"
    SESSION_USE_SIGNER = True
    SESSION_KEY_PREFIX = 'session:'
    SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")
    #SESSION_REDIS = redis.StrictRedis(host='localhost', port=6379)