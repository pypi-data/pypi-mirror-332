from inspect import signature
from typing import Any, Callable
import hashlib
import logging


logger = logging.getLogger(__name__)


def get_args(fn: Callable, args: tuple, kwargs: dict[str, Any]) -> dict[str, Any]:
    """
    Нормализует аргументы функции в единый словарь {имя_параметра: значение},
    учитывая позиционные, ключевые, *args и **kwargs.
    """
    sig = signature(fn)
    bound_args = sig.bind(*args, **kwargs)
    bound_args.apply_defaults()

    return bound_args.arguments


def generate_key(
    fn: Callable,
    args: tuple,
    kwargs: dict[str, Any],
    serializer: Callable[[Any], str | bytes],
    key_prefix: str = "",
    hash_func: str | None = None,
) -> str:
    """
    Генерирует ключ для функции на основе её аргументов.
    """
    parsed_args = get_args(fn, args, kwargs)
    serialized_data = f"{fn.__module__}.{fn.__qualname__}:{serializer(parsed_args)}"
    logger.debug(f"Serialized data: {serialized_data}")

    if hash_func:
        hasher = hashlib.new(hash_func)
        hasher.update(serialized_data.encode("utf-8"))
        return key_prefix + hasher.hexdigest()
    else:
        return key_prefix + serialized_data
