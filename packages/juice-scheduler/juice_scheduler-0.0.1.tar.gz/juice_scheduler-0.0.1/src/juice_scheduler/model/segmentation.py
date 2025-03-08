from __future__ import annotations

from typing import TYPE_CHECKING

from juice_scheduler.common.date_utils import datestr_to_timestamp
from juice_scheduler.model.segment_definition import NonExistingDefinitionError, SegmentDefinitionHandler

if TYPE_CHECKING:
    from pathlib import Path

    from juice_scheduler.model.segment_list import SegmentList

import json

from juice_scheduler.model.working_group import WorkingGroup


class Segmentation:

    def __init__(self, name: str):
        self.name : str = name
        self.working_groups: dict[str, WorkingGroup] = {}
        self.definitions: dict[str, SegmentList] = {}

    def add_interval(self, working_group: str, definition: str, start: float, end: float) -> None:
        """
        Adds an interval to the specified working group and definition.

        If the working group does not exist, it is created. The interval is then added to the
        corresponding definition within that working group.

        :param working_group: The name of the working group to which the interval belongs.
        :param definition: The definition under which the interval is categorized.
        :param start: The start time of the interval.
        :param end: The end time of the interval.
        :return: None
        """

        if working_group not in self.working_groups:
            self.working_groups[working_group] = WorkingGroup(working_group)
        definition_obj = self.working_groups[working_group].add_interval(definition, start, end)
        # indexing the definition, if it does not exist
        if definition not in self.definitions:
            self.definitions[definition] = definition_obj

    def get_working_group(self, working_group: str) -> WorkingGroup:
        """
        Get the working group with the given name.

        :param working_group: The name of the working group to get.
        :return: The working group with the given name.
        :raises NonExistingWorkingGroupError: If the working group does not exist.
        """
        if working_group not in self.working_groups:
            raise NonExistingWorkingGroupError
        return self.working_groups[working_group]

    @staticmethod
    def from_sht_struct(plan_json, definition_handler: SegmentDefinitionHandler) -> Segmentation:
        seg = Segmentation("sht")
        segment_list = plan_json.get("segments")

        for segment in segment_list:
            try:
                mnemonic = segment.get("segment_definition")
                working_group = definition_handler.get_definition(mnemonic).working_group
                start = segment.get("start")
                end = segment.get("end")
                seg.add_interval(working_group, mnemonic, datestr_to_timestamp(start), datestr_to_timestamp(end))
            except NonExistingDefinitionError:
                pass

        return seg


    @staticmethod
    def from_sht_files(plan_path: Path, definition_handler: SegmentDefinitionHandler) -> Segmentation:
        with plan_path.open("r") as plan_file:
            plan_json = json.load(plan_file)
        return Segmentation.from_sht_struct(plan_json, definition_handler)

    def to_sht_struct(self):
        segments = []
        sht_struct = {
            "creationDate": "2025-03-06T07:06:59.020Z",
            "name": "Checkpoint 2025-03-06T07:06:59.020Z",
            "segment_groups": [],
            "trajectory": "CREMA_5_0",
            "segments": segments,
        }
        for segment in self.definitions.values():
            segments.extend(segment.to_sht_struct())
        return sht_struct

    def dump_sht_file(self, plan_path: Path):
        sht_struct = self.to_sht_struct()
        with plan_path.open("w") as plan_file:
            json.dump(sht_struct, plan_file, indent=2)


class NonExistingWorkingGroupError(Exception):
    pass
