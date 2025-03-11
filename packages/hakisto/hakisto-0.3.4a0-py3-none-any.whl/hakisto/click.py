import inspect

# from hakisto import logger

__all__ = []

# logger._Logger.register_excluded_source_file(inspect.currentframe().f_code.co_filename)

try:
    import click
except ImportError as e:
    # logger.critical("package 'click' not found")
    raise e from None
else:
    from ._click import *
