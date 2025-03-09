import datetime
import re
import sys

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DATE_LEN = len("YYYY-MM-DD")
DATE_FMT = "%Y-%m-%d"

DATETIME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$")
DATETIME_LEN = len("YYYY-MM-DDTHH:MM:SS")
DATETIME_FMT = "%Y-%m-%dT%H:%M:%S"


def date_to_string(dt):
    if isinstance(dt, str):
        if len(dt) == DATE_LEN:
            validate_date_str(dt)
        elif len(dt) == DATETIME_LEN:
            validate_datetime_str(dt)
        else:
            raise ValueError("Date input should be in format of either YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS")
        return dt
    elif isinstance(dt, datetime.datetime):
        return dt.strftime(DATETIME_FMT)
    elif isinstance(dt, datetime.date):
        return dt.strftime(DATE_FMT)
    elif isinstance(dt, int):
        return datetime.datetime.utcfromtimestamp(dt).strftime(DATETIME_FMT)
    else:
        raise TypeError("Date input must be one of: str, date, datetime, float, int, or None")


def validate_date_str(datestr):
    if not DATE_RE.match(datestr):
        raise ValueError("Date input should be in format of YYYY-MM-DD")


def validate_datetime_str(datetimestr):
    if not DATETIME_RE.match(datetimestr):
        raise ValueError("Datetime input should be in format of YYYY-MM-DDTHH:MM:SS")
