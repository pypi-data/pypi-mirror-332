import logging

from redis_cache import utils


logger = logging.getLogger(__name__)


def test_generate_cache_key():
    import json
    import pickle

    def add(a, b):
        return a + b

    correct_cache = "9b646071fce1c34ea1e2c66b78521b26"

    result = utils.generate_key(add, (1, 2), {}, json.dumps, hash_func="md5")
    assert result == correct_cache

    result = utils.generate_key(add, (), {"a": 1, "b": 2}, json.dumps, hash_func="md5")
    assert result == correct_cache

    result = utils.generate_key(add, (), {"b": 2, "a": 1}, json.dumps, hash_func="md5")
    assert result == correct_cache

    correct_cache = "c566e73a8a5f4e4f6179f90950cc4df6"

    result = utils.generate_key(add, (1, 2), {}, pickle.dumps, hash_func="md5")
    assert result == correct_cache

    result = utils.generate_key(
        add, (), {"a": 1, "b": 2}, pickle.dumps, hash_func="md5"
    )
    assert result == correct_cache

    result = utils.generate_key(
        add, (), {"b": 2, "a": 1}, pickle.dumps, hash_func="md5"
    )
    assert result == correct_cache
