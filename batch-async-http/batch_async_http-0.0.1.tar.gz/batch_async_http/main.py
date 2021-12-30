import asyncio
from functools import wraps
import inspect

def chunker(seq, size):
    """
    return a sequence/list in chunks of size=size
    Args:
        seq: list
        size: int - chunk size
    Returns:
        seq or list of chunks
    """
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def batch_async(size):
    def decorator(func):

        # Check to make decorated function is an async function
        if not inspect.iscoroutinefunction(func):
            raise TypeError('The batch_async decorator only works on async functions')

        @wraps(func)
        async def wrapper(*args):

            # Check to ensure there is only one input parameter
            sig = inspect.signature(wrapper)
            params = sig.parameters
            if len(params) > 1:
                raise TypeError('Functions using batch_async can only accept 1 argument, got {}'.format(len(params)))

            # prepare chunks of length n each to pass to API sychronously:
            list_of_seqs = chunker(*args, size)

            # gather all responses:
            response = await asyncio.gather(*map(func, list_of_seqs))

            # flatten list of responses back to one large list:
            flat_response = [item for sublist in response for item in sublist]

            return flat_response

        return wrapper

    return decorator
