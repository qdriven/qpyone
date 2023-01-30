"""Main package for humanize."""

from .filesize import naturalsize
from .i18n import activate
from .i18n import deactivate
from .i18n import decimal_separator
from .i18n import thousands_separator
from .number import apnumber
from .number import clamp
from .number import fractional
from .number import intcomma
from .number import intword
from .number import metric
from .number import ordinal
from .number import scientific
from .time import naturaldate
from .time import naturalday
from .time import naturaldelta
from .time import naturaltime
from .time import precisedelta


# try:
#     # Python 3.8+
#     import importlib.metadata as importlib_metadata
# except ImportError:
#     # <Python 3.7 and lower
#     import importlib_metadata  # type: ignore
#
# __version__ = importlib_metadata.version(__name__)


__all__ = [
    "activate",
    "apnumber",
    "clamp",
    "deactivate",
    "decimal_separator",
    "fractional",
    "intcomma",
    "intword",
    "metric",
    "naturaldate",
    "naturalday",
    "naturaldelta",
    "naturalsize",
    "naturaltime",
    "ordinal",
    "precisedelta",
    "scientific",
    "thousands_separator",
]
