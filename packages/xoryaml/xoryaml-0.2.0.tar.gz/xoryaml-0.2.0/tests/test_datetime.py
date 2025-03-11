import datetime
import zoneinfo

import xoryaml

AMSTERDAM_1937_DATETIMES_WITH_Z = (
    '---\n- "1937-01-01T12:00:27.000087+00:20"',  # tzinfo<2022b and an example in RFC 3339
    '---\n- "1937-01-01T12:00:27.000087Z"',  # tzinfo>=2022b
    '---\n- "1937-01-01T12:00:27.000087+00:19"',  # some platforms
)


def test_datetime_naive():
    """
    datetime.datetime naive prints without offset
    """
    dumped = xoryaml.dumps([datetime.datetime(2000, 1, 1, 2, 3, 4, 123)])
    assert dumped == '---\n- "2000-01-01T02:03:04.000123"'


def test_datetime_min():
    """
    datetime.datetime min range
    """
    dumped = xoryaml.dumps([datetime.datetime(datetime.MINYEAR, 1, 1, 0, 0, 0, 0)])
    assert dumped == '---\n- "0001-01-01T00:00:00"'


def test_datetime_max():
    """
    datetime.datetime max range
    """
    dumped = xoryaml.dumps(
        [datetime.datetime(datetime.MAXYEAR, 12, 31, 23, 59, 50, 999999)]
    )
    assert dumped == '---\n- "9999-12-31T23:59:50.999999"'


def test_datetime_three_digits():
    """
    datetime.datetime three digit year
    """
    dumped = xoryaml.dumps([datetime.datetime(312, 1, 1)])
    assert dumped == '---\n- "0312-01-01T00:00:00"'


def test_datetime_two_digits():
    """
    datetime.datetime two digit year
    """
    dumped = xoryaml.dumps([datetime.datetime(46, 1, 1)])
    assert dumped == '---\n- "0046-01-01T00:00:00"'


def test_datetime_timezone_utc():
    """
    datetime.datetime.utc
    """
    dumped = xoryaml.dumps(
        [datetime.datetime(2018, 6, 1, 2, 3, 4, 0, tzinfo=datetime.timezone.utc)]
    )
    assert dumped == '---\n- "2018-06-01T02:03:04Z"'


def test_datetime_zoneinfo_utc():
    """
    zoneinfo.ZoneInfo("UTC")
    """
    dumped = xoryaml.dumps(
        [datetime.datetime(2018, 6, 1, 2, 3, 4, 0, tzinfo=zoneinfo.ZoneInfo("UTC"))]
    )
    assert dumped == '---\n- "2018-06-01T02:03:04Z"'


def test_datetime_zoneinfo_positive():
    dumped = xoryaml.dumps(
        [
            datetime.datetime(
                2018, 1, 1, 2, 3, 4, 0, tzinfo=zoneinfo.ZoneInfo("Asia/Shanghai")
            )
        ]
    )
    assert dumped == '---\n- "2018-01-01T02:03:04+08:00"'


def test_datetime_zoneinfo_negative():
    dumped = xoryaml.dumps(
        [
            datetime.datetime(
                2018, 6, 1, 2, 3, 4, 0, tzinfo=zoneinfo.ZoneInfo("America/New_York")
            )
        ]
    )
    assert dumped == '---\n- "2018-06-01T02:03:04-04:00"'


def test_datetime_zoneinfo_negative_non_dst():
    """
    datetime.datetime negative UTC non-DST
    """
    dumped = xoryaml.dumps(
        [
            datetime.datetime(
                2018, 12, 1, 2, 3, 4, 0, tzinfo=zoneinfo.ZoneInfo("America/New_York")
            )
        ]
    )
    assert dumped == '---\n- "2018-12-01T02:03:04-05:00"'


def test_datetime_zoneinfo_partial_hour():
    """
    datetime.datetime UTC offset partial hour
    """
    dumped = xoryaml.dumps(
        [
            datetime.datetime(
                2018, 12, 1, 2, 3, 4, 0, tzinfo=zoneinfo.ZoneInfo("Australia/Adelaide")
            )
        ]
    )
    assert dumped == '---\n- "2018-12-01T02:03:04+10:30"'


def test_datetime_partial_second_zoneinfo():
    """
    datetime.datetime UTC offset round seconds

    https://tools.ietf.org/html/rfc3339#section-5.8
    """
    dumped = xoryaml.dumps(
        [
            datetime.datetime(
                1937, 1, 1, 12, 0, 27, 87, tzinfo=zoneinfo.ZoneInfo("Europe/Amsterdam")
            )
        ]
    )
    assert dumped in AMSTERDAM_1937_DATETIMES_WITH_Z


def test_datetime_microsecond_max():
    """
    datetime.datetime microsecond max
    """
    dumped = xoryaml.dumps(datetime.datetime(2000, 1, 1, 0, 0, 0, 999999))
    assert dumped == '---\n"2000-01-01T00:00:00.999999"'


def test_datetime_microsecond_min():
    """
    datetime.datetime microsecond min
    """
    dumped = xoryaml.dumps(datetime.datetime(2000, 1, 1, 0, 0, 0, 1))
    assert dumped == '---\n"2000-01-01T00:00:00.000001"'


def test_date():
    """
    datetime.date
    """
    dumped = xoryaml.dumps([datetime.date(2000, 1, 13)])
    assert dumped == "---\n- 2000-01-13"


def test_date_min():
    """
    datetime.date MINYEAR
    """
    dumped = xoryaml.dumps([datetime.date(datetime.MINYEAR, 1, 1)])
    assert dumped == "---\n- 0001-01-01"


def test_date_max():
    """
    datetime.date MAXYEAR
    """
    dumped = xoryaml.dumps([datetime.date(datetime.MAXYEAR, 12, 31)])
    assert dumped == "---\n- 9999-12-31"


def test_date_three_digits():
    """
    datetime.date three digit year
    """
    dumped = xoryaml.dumps([datetime.date(312, 1, 1)])
    assert dumped == "---\n- 0312-01-01"


def test_date_two_digits():
    """
    datetime.date two digit year
    """
    dumped = xoryaml.dumps([datetime.date(46, 1, 1)])
    assert dumped == "---\n- 0046-01-01"


def test_time():
    """
    datetime.time
    """
    dumped0 = xoryaml.dumps([datetime.time(12, 15, 59, 111)])
    assert dumped0 == '---\n- "12:15:59.000111"'
    dumped1 = xoryaml.dumps([datetime.time(12, 15, 59)])
    assert dumped1 == '---\n- "12:15:59"'


def test_time_microsecond_max():
    """
    datetime.time microsecond max
    """
    dumped = xoryaml.dumps(datetime.time(0, 0, 0, 999999))
    assert dumped == '---\n"00:00:00.999999"'


def test_time_microsecond_min():
    """
    datetime.time microsecond min
    """
    dumped = xoryaml.dumps(datetime.time(0, 0, 0, 1))
    assert dumped == '---\n"00:00:00.000001"'
