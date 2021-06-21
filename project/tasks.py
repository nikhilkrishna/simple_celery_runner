from typing_extensions import TypeAlias
from .celery import app
from mnemonic import Mnemonic

import hashlib


LANGUAGE = "english"



@app.task
def add(x, y):
    return x + y

@app.task
def hash_sha256(str):
    return hashlib.sha256(str)

@app.task
def generate_seed_words():
    mnemo = Mnemonic(LANGUAGE)
    return mnemo.generate(strength=256)

@app.task
def calculate_seed(words: str):
    mnemo = Mnemonic(LANGUAGE)
    return mnemo.to_seed(words, passphrase="").hex()
