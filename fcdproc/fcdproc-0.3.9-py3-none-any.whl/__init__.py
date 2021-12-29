# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""Top-module metadata."""


__all__ = [
    '__copyright__',
    '__credits__',
    '__packagename__',
    '__version__',
]

# Silence PyBIDS warning for extension entity behavior
# Can be removed once minimum PyBIDS dependency hits 0.14
try:
    import bids
    bids.config.set_option('extension_initial_dot', True)
except (ImportError, ValueError):
    pass
else:
    del bids