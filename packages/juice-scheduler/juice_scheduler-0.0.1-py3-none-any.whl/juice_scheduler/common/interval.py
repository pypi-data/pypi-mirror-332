import copy
from operator import itemgetter


def intervals_clean(intervals, max_gap=0, min_interval=0):
    """
    Clean a list of intervals removing intervals <= min_interval and if gaps < max_gap join intervals

    :param intervals: list of interval
    :param max_gap: The maximum acceptable gap between values;
    Consecutive values with Intervals smaller than max_gaps will be combined into a single interval.
    Default: 0   (any gap keeps intervals separate)
    :param min_interval: The smallest acceptable interval;
    Any interval smaller is discarded; Default: 0   (all intervals are accepted)
    :return: list of intervals [[start0, end0]...] values without gaps > max_gap and (end_i - stat_i) > min_interval
    """

    list_of_intervals = copy.deepcopy(intervals)

    n = len(list_of_intervals) - 1
    for i in range(n, 0, -1):
        if list_of_intervals[i][0] - list_of_intervals[i - 1][1] < max_gap:
            list_of_intervals[i - 1] = [list_of_intervals[i - 1][0], list_of_intervals[i][1]]
            list_of_intervals.pop(i)

    return [interval for interval in list_of_intervals if (interval[1] - interval[0]) > min_interval]


def not_intervals(intervals, start=None, end=None):
    """
    Get the complementary of a given list os intervals [start0, end0],...]
    If absolute start/end values of interval is provided, the corresponding interval is included

    :param intervals: list of intervals
    :param start: absolute start value of intervals; default None
    :param end: absolute end value of intervals; default None
    :return: not_events: list of intervals
    """
    not_events = []
    for i in range(len(intervals[:-1])):
        not_events.append([intervals[i][1], intervals[i+1][0]])

    if len(not_events) == 0 and len(intervals) != 1:
        if start is not None and end is not None:
            not_events = [[start, end]]
    else:
        if start is not None and start <= intervals[0][0]:
                not_events.insert(0, [start, intervals[0][0]])

        if end is not None and end >= intervals[-1][1]:
                not_events.append([intervals[-1][1], end])

    return not_events

def merge_intervals(list_of_intervals):
    """
    Merge list of intervals [[start0, end0]...]

    :param list_of_intervals:
    :return: a new list of intervals
    """

    if not list_of_intervals:
        return []

    intervals = sorted(list_of_intervals, key=itemgetter(0))

    count = 0
    for p in intervals:
        (start, end) = tuple(p)
        if start > intervals[count][1]:
            count += 1
            intervals[count] = p
        elif end > intervals[count][1]:
            intervals[count] = [intervals[count][0], end]

    return intervals[:count + 1]

