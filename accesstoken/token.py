from dataclasses import asdict
from entity.Account import *
import jwt

SECRET_KEY = "0oRNvlDf9Aw1Q6rBiLYvdRx7QHCiyd7z"
ALGORITHM = "HS256"

def get_token(acc):
    payload = asdict(acc)
    return jwt.encode(payload, SECRET_KEY, algorithm = ALGORITHM).decode('utf-8')

def decode_token(token):
    return jwt.decode(token, SECRET_KEY, algorithm = ALGORITHM)