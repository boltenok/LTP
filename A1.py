def seconds_difference(time_1, time_2):
    """ (number, number) -> number

    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.

    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    """
    return time_2 - time_1
# print(seconds_difference(1800.0, 3600.0))
# print(seconds_difference(3600.0, 1800.0))
# print(seconds_difference(1800.0, 2160.0))
# print(seconds_difference(1800.0, 1800.0))

def hours_difference(time_1, time_2):
    """ (number, number) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.

    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    """
    return (time_2 - time_1)/3600
# print(hours_difference(1800.0, 3600.0))
# print(hours_difference(3600.0, 1800.0))
# print(hours_difference(1800.0, 2160.0))
# print(hours_difference(1800.0, 1800.0))

def to_float_hours(hours, minutes, seconds):
    """ (int, int, int) -> float

    Return the total number of hours in the specified number
    of hours, minutes, and seconds.

    Precondition: 0 <= minutes < 60  and  0 <= seconds < 60

    >>> to_float_hours(0, 15, 0)
    0.25
    >>> to_float_hours(2, 45, 9)
    2.7525
    >>> to_float_hours(1, 0, 36)
    1.01
    """
    return hours + (minutes/60) + (seconds/3600)
# print(to_float_hours(0, 15, 0))
# print(to_float_hours(2, 45, 9))
# print(to_float_hours(1, 0, 39))

def to_24_hour_clock(hours):
    """ (number) -> number

    hours is a number of hours since midnight. Return the
    hour as seen on a 24-hour clock.

    Precondition: hours >= 0

    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(48)
    0
    >>> to_24_hour_clock(25)
    1
    >>> to_24_hour_clock(4)
    4
    >>> to_24_hour_clock(28.5)
    4.5
    """

    return hours % 24
# print(to_24_hour_clock(24))
# print(to_24_hour_clock(48))
# print(to_24_hour_clock(25))
# print(to_24_hour_clock(4))
# print(to_24_hour_clock(28.5))

### Write your get_hours function definition here:
def get_hours(time_elapsed):
    """ (int) -> int

    Return number of even hours from a given time in seconds elapsed from the midnight.

    >>> get_hours(3600)
    1
    >>> get_hours(7200)
    2
    >>> get_hours(105000)
    5
    >>> get_hours(1800)
    0
    """
    return (time_elapsed // 3600) % 24
# print(get_hours(3600))
# print(get_hours(7200))
# print(get_hours(105000))
# print(get_hours(1800))

### Write your get_minutes function definition here:
def get_minutes(time_elapsed):
    """ (int) -> int

        Return number of even minutes from a given time in seconds elapsed from the midnight.

        >>> get_minutes(3600)
        0
        >>> get_minutes(7200)
        0
        >>> get_minutes(4200)
        10
        >>> get_minutes(1803)
        30
    """
    return (time_elapsed % 3600) // 60
# print(get_minutes(3600))
# print(get_minutes(7200))
# print(get_minutes(4200))
# print(get_minutes(1803))

### Write your get_seconds function definition here:
def get_seconds(time_elapsed):
    """ (int) -> int

        Return number of even minutes from a given time in seconds elapsed from the midnight.

        >>> get_seconds(3600)
        0
        >>> get_seconds(7233)
        33
        >>> get_seconds(1823)
        23
        >>> get_seconds(3589)
        49
    """
    return (time_elapsed % 3600) % 60
# print(get_seconds(3600))
# print(get_seconds(7233))
# print(get_seconds(1823))
# print(get_seconds(3589))

def time_to_utc(utc_offset, time):
    """ (number, float) -> float

    Return time at UTC+0, where utc_offset is the number of hours away from
    UTC+0.

    >>> time_to_utc(+0, 12.0)
    12.0
    >>> time_to_utc(+1, 12.0)
    11.0
    >>> time_to_utc(-1, 12.0)
    13.0
    >>> time_to_utc(-11, 18.0)
    5.0
    >>> time_to_utc(-1, 0.0)
    1.0
    >>> time_to_utc(-1, 23.0)
    0.0
    """
    return to_24_hour_clock(time - utc_offset)
# print(time_to_utc(0, 12.0))
# print(time_to_utc(+1, 12.0))
# print(time_to_utc(-1, 12.0))
# print(time_to_utc(-11, 18.0))
# print(time_to_utc(-1, 0.0))
# print(time_to_utc(-1, 23.0))



def time_from_utc(utc_offset, time):
    """ (number, float) -> float

    Return UTC time in time zone utc_offset.

    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    >>> time_from_utc(-1, 12.0)
    11.0
    >>> time_from_utc(+6, 6.0)
    12.0
    >>> time_from_utc(-7, 6.0)
    23.0
    >>> time_from_utc(-1, 0.0)
    23.0
    >>> time_from_utc(-1, 23.0)
    22.0
    >>> time_from_utc(+1, 23.0)
    0.0
    """
    return to_24_hour_clock(time + utc_offset)
# print(time_from_utc(+0, 12.0))
# print(time_from_utc(+1, 12.0))
# print(time_from_utc(-1, 12.0))
# print(time_from_utc(+6, 6.0))
# print(time_from_utc(-7, 6.0))
# print(time_from_utc(-1, 0.0))
# print(time_from_utc(-1, 23.0))
# print(time_from_utc(+1, 23.0))


