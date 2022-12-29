import asyncio
from concurrent.futures import ThreadPoolExecutor
from functools import wraps
from typing import Any


def to_async(func: Any):
    """Runs a synchronous function in an asynchronous context.

    Args:
        func (Any): A function to run asynchronously.
    """

    @wraps(func)
    async def run_async(*args, **kwargs):
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(executor=None, func=func, *args, **kwargs)
