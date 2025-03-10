from ratisbona_utils.parsing import TokenDefinition

token_definitions = [
    # 1. ISO Datetime (with T or space separator) with optional seconds, milliseconds and timezone.
    # Example: 2024-02-28T14:30, 2024-02-28 14:30:00, 2024-02-28T14:30:00.123, 2024-02-28T14:30:00+02:00
    TokenDefinition(
        "Datetime",
        r"(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})[T ]"
        r"(?P<hour>\d{2}):(?P<minute>\d{2})"
        r"(?:\:(?P<second>\d{2}))?"
        r"(?:\.(?P<millisecond>\d{1,3}))?"
        r"(?P<timezone>Z|[+\-]\d{2}:\d{2})?",
    ),
    # 2. German Date: day.month.year (e.g., 28.2.2024)
    TokenDefinition("Date", r"(?P<day>\d{1,2})\.(?P<month>\d{1,2})\.(?P<year>\d{4})"),
    # 3. ISO Date: year-month-day (e.g., 2024-02-28)
    TokenDefinition("Date", r"(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})"),
    # 4. American Date: month/day/year (e.g., 02/28/2024)
    TokenDefinition("Date", r"(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4})"),
    # 5. Time (only): hour:minute with optional seconds and milliseconds.
    # Examples: 14:30, 14:30:00, 14:30:00.123
    TokenDefinition(
        "Time",
        r"(?P<hour>\d{1,2}):(?P<minute>\d{2})"
        r"(?:\:(?P<second>\d{2}))?"
        r"(?:\.(?P<millisecond>\d{1,3}))?",
    ),
    # 6. Relative Dates in German and English.
    # Matches words like "heute", "morgen", "übermorgen", "gestern", "vorgestern" as well as
    # "today", "tomorrow", "day after tomorrow", "day before yesterday".
    # Using the inline (?i) flag to ignore case.
    TokenDefinition(
        "RelativeDate",
        r"(?i)\b(?P<rel>(heute|morgen|übermorgen|gestern|vorgestern|today|tomorrow|day after tomorrow|day before yesterday))\b",
    ),
]
