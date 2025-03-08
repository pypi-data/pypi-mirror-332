from __future__ import annotations

from copy import deepcopy

from portion import Interval, closed, to_data

from juice_scheduler.common.date_utils import timestamp_to_datestr


class SegmentList:
    def __init__(self, name: str) -> None:
        self.name = name
        self.instances: DateStrInterval = DateStrInterval()

    def add_interval(self, start: float, end: float) -> None:
        if start > end:
            raise InvalidIntervalError
        self.instances = self.instances.union(closed(start, end))

    def substract(self, interval: DateStrInterval) -> None:
        self.instances = self.instances - interval

    def deep_copy(self) -> SegmentList:
        return deepcopy(self)

    def __repr__(self) -> str:
        return repr(self.instances)

    def to_sht_struct(self) -> list[object]:
        segments = []
        for instance in self.instances:
            for interval in to_data(instance):
                segments.append({
                    "start": timestamp_to_datestr(interval[1]),
                    "end":  timestamp_to_datestr(interval[2]),
                    "timeline": "PRIME",
                    "segment_definition": self.name,
                    "resources": [],
                    "instrument_resources": [],
                    "overwritten": False,
                    "instrument_overwritten": False,
                })
        return segments


class InvalidIntervalError(Exception):
    pass


class DateStrInterval(Interval):
    def __repr__(self):
        if self.empty:
            return "()"
        string = []
        for interval in self._intervals:
            if interval.lower == interval.upper:
                string.append("[" + repr(interval.lower) + "]")
            else:
                string.append(
                    ("[")
                    + timestamp_to_datestr(interval.lower)
                    + ","
                    + timestamp_to_datestr(interval.upper)
                    + ("]"),
                )
        return " | ".join(string)


