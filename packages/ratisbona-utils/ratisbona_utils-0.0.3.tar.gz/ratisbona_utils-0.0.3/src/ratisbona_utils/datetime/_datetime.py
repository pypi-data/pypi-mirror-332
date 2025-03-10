import re
from calendar import monthrange
from datetime import time, date, datetime, timedelta
from typing import Iterator

from dateutil.tz import tzlocal

from ratisbona_utils.monads import Maybe, Just, Nothing


def ensure_timezone(a_datetime: datetime) -> datetime:
    if a_datetime.tzinfo is None:
        return a_datetime.replace(tzinfo=tzlocal())
    return a_datetime

def ensure_no_timezone(a_datetime: datetime) -> datetime:
    return a_datetime.replace(tzinfo=None)

def to_datetime(a_date: date) -> datetime:
    return datetime.combine(a_date, time.min)

def format_ms_HHMMSSss(time_elapsed_millis: int, show_msec: bool = True) -> str:
    """
        Formats a time in milliseconds to a string in the format `HH:MM:SS.mmm`.
    """
    raw_secs, milliseconds = divmod(time_elapsed_millis, 1000)
    raw_min, seconds = divmod(raw_secs, 60)
    hours, minutes = divmod(raw_min, 60)
    retval = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    if show_msec:
        retval += f".{milliseconds:03d}"
    return retval


def last_day_of_month(given_date: date) -> date:
    """
        Gives the last day of the month of the given date.
        Bitterly missed in the standard library for the actual datatype date, no reason aparent, why they combined
        the int-typed version with unrelated stuff to monthrange...

        Args:
            given_date: date, the date for which the last day of the month is requested.

        Returns:
            date: The last day of the month of the given date.
    """
    last_day = monthrange(given_date.year, given_date.month)[1]
    return date(given_date.year, given_date.month, last_day)


def month_iterator(start: date, end: date) -> Iterator[tuple[int, int]]:
    """
    Provides an iterator that advances month by month from start (inclusive) to end (exclusive) and yields year and month number.

    Args:
        start: date, the day the iterator should start (inclusive).
        end: date, the day the iterator should end (exclusive).

    Returns:
        Tuple[int, int]: Year and month, e.g. (2020, 1) for January 2020.
    """
    current = start.replace(day=1)
    while current < end:
        yield current.year, current.month
        current = (current + timedelta(days=32)).replace(day=1)


def try_parse_leading_isodate(value: str) -> Maybe[tuple[date, str]]:
    """
    Tries to parse a date in the format 'YYYY-MM-DD' from the beginning of the given string.

    Args:
        value: str, the string to parse.

    Returns:
        Maybe[date]: The parsed date or nothing if the string does not start with a valid date.
    """
    match = re.match(r"(\d{4})-(\d{2})-(\d{2})(.*)", value)
    if not match:
        return Nothing
    year, month, day = map(int, match.groups()[0:3])
    rest = match.groups()[3]
    try:
        return Just((date(year, month, day), rest))
    except ValueError:
        return Nothing
