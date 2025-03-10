"""
    A package that contains utilities for datetime handling
"""

from ._stopwatch import Stopwatch, with_stopwatch
from ._datetime import (
    ensure_timezone,
    ensure_no_timezone,
    to_datetime,
    format_ms_HHMMSSss,
    last_day_of_month,
    month_iterator,
)
from ._ddate import (
    DDateWeekday,
    ddate,
    DDateSeason,
    maybe_get_discordian_season_and_day,
    yold_by_date,
    maybe_get_discordian_weekday,
    decode,
)
from ._gaussian_easter import calculate_easter_date
