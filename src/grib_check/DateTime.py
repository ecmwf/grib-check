#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

from datetime import datetime, timedelta


def _extract_int(value) -> int:
    """Extract an int from a value that may be a KeyValue, numpy scalar, or plain int."""
    if hasattr(value, 'value'):  # KeyValue
        return int(value.value())
    return int(value)


# GRIB2 Code Table 4.4: Indicator of unit of time range
_GRIB_UNIT_NAMES = {
    0: "minute",
    1: "hour",
    2: "day",
    3: "month",
    4: "year",
    5: "decade",
    6: "normal",
    7: "century",
    10: "3hours",
    11: "6hours",
    12: "12hours",
    13: "second",
}


def _grib_unit_to_timedelta(value: int, unit_code: int) -> timedelta:
    """Convert a GRIB time value + unit code (Table 4.4) to a timedelta."""
    if unit_code == 0:
        return timedelta(minutes=value)
    elif unit_code == 1:
        return timedelta(hours=value)
    elif unit_code == 2:
        return timedelta(days=value)
    elif unit_code == 10:
        return timedelta(hours=value * 3)
    elif unit_code == 11:
        return timedelta(hours=value * 6)
    elif unit_code == 12:
        return timedelta(hours=value * 12)
    elif unit_code == 13:
        return timedelta(seconds=value)
    else:
        unit_name = _GRIB_UNIT_NAMES.get(unit_code, f"unknown({unit_code})")
        raise ValueError(
            f"Cannot convert GRIB time unit '{unit_name}' (code={unit_code}) to timedelta"
        )


class TimeDelta:
    """Wrapper around timedelta for GRIB time values with unit awareness.

    Interprets the unit according to GRIB2 Code Table 4.4 and builds an
    expression string that tracks provenance.  Use ``.to_key_value()`` to
    convert into a ``KeyValue`` for assertion arithmetic.

    *value* and *unit_indicator* may be plain ints, numpy scalars, or
    KeyValue objects.
    """

    def __init__(self, value, unit_indicator):
        val = _extract_int(value)
        unit_code = _extract_int(unit_indicator)
        self._td = _grib_unit_to_timedelta(val, unit_code)
        self._expr = f"TimeDelta({value}, {unit_indicator})"

    def to_key_value(self):
        """Convert to ``KeyValue(expr, timedelta)`` for use with Assert classes."""
        from .KeyValue import KeyValue
        return KeyValue(self._expr, self._td)

    def value(self) -> timedelta:
        return self._td

    def __eq__(self, other) -> bool:
        if isinstance(other, TimeDelta):
            return self._td == other._td
        if isinstance(other, timedelta):
            return self._td == other
        return NotImplemented

    def __ne__(self, other) -> bool:
        if isinstance(other, TimeDelta):
            return self._td != other._td
        if isinstance(other, timedelta):
            return self._td != other
        return NotImplemented

    def __str__(self) -> str:
        return f"{self._expr}({self._td})"

    def __repr__(self) -> str:
        return f"TimeDelta({self._td})"

    def __hash__(self) -> int:
        return hash(self._td)


class DataTime:
    """Wrapper around datetime for GRIB date/time values.

    Builds an expression string that tracks provenance.  Use
    ``.to_key_value()`` to convert into a ``KeyValue`` for assertion
    arithmetic.

    Two construction forms::

        DataTime(dataDate, dataTime)          # GRIB form (YYYYMMDD, HHMM)
        DataTime(year=, month=, day=, ...)    # component form
    """

    def __init__(self, *args, year=None, month=None, day=None, hour=0, minute=0, second=0):
        if len(args) == 2 and year is None and month is None and day is None:
            # GRIB form: DataTime(dataDate, dataTime)
            dataDate, dataTime = args
            dd = _extract_int(dataDate)
            dt = _extract_int(dataTime)
            self._dt = datetime(
                year=dd // 10000,
                month=(dd % 10000) // 100,
                day=dd % 100,
                hour=dt // 100,
                minute=dt % 100,
            )
            self._expr = f"DateTime({dataDate}, {dataTime})"
        elif len(args) == 0 and year is not None and month is not None and day is not None:
            # Component form: DataTime(year=, month=, day=, ...)
            y = _extract_int(year)
            mo = _extract_int(month)
            d = _extract_int(day)
            h = _extract_int(hour)
            mi = _extract_int(minute)
            s = _extract_int(second)
            self._dt = datetime(year=y, month=mo, day=d,
                                hour=h, minute=mi, second=s)
            parts = [str(year), str(month), str(day)]
            if h or mi or s:
                parts.extend([str(hour), str(minute), str(second)])
            self._expr = f"DateTime({', '.join(parts)})"
        else:
            raise TypeError(
                "DataTime() requires either 2 positional args (dataDate, dataTime) "
                "or keyword args (year=, month=, day=, ...)"
            )

    def to_key_value(self):
        """Convert to ``KeyValue(expr, datetime)`` for use with Assert classes."""
        from .KeyValue import KeyValue
        return KeyValue(self._expr, self._dt)

    def value(self) -> datetime:
        return self._dt

    def __eq__(self, other) -> bool:
        if isinstance(other, DataTime):
            return self._dt == other._dt
        if isinstance(other, datetime):
            return self._dt == other
        return NotImplemented

    def __ne__(self, other) -> bool:
        if isinstance(other, DataTime):
            return self._dt != other._dt
        if isinstance(other, datetime):
            return self._dt != other
        return NotImplemented

    def __str__(self) -> str:
        return f"{self._expr}({self._dt.strftime('%Y-%m-%d %H:%M:%S')})"

    def __repr__(self) -> str:
        return f"DataTime({self._dt})"

    def __hash__(self) -> int:
        return hash(self._dt)
