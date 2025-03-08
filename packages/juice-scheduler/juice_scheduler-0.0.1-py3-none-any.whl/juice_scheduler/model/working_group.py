from .segment_list import SegmentList


class WorkingGroup:
    def __init__(self, name: str) -> None:
        self.name = name
        self.definitions: dict[str, SegmentList] = {}


    def add_interval(self, definition: str, start: float, end: float) -> SegmentList:
        if definition not in self.definitions:
            self.definitions[definition] = SegmentList(definition)
        self.definitions[definition].add_interval(start, end)
        return self.definitions[definition]
