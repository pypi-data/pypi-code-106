import inspect


def get_fn_ln():
    _, filename, ln, _, _, _ = inspect.getouterframes(
        inspect.currentframe()
    )[1]  # returns: frame, filename, ln, fn, lolc, idx

    return filename, ln
