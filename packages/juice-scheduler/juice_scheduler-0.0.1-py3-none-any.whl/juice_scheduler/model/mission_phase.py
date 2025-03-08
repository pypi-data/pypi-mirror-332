from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from juice_scheduler.common.date_utils import datestr_to_timestamp

if TYPE_CHECKING:
    from pathlib import Path


class MissionPhase:
    def __init__(self, name, description: str, start: float, end: float):
        self.name: str = name
        self.description: str = description
        self.start: float = start
        self.end: float = end

class MissionPhaseHandler:
    def __init__(self):
        self.phases: dict[str, MissionPhase] = {}

    def add_phase(self, name: str, description: str, start: float, end: float):
        if name in self.phases:
            raise DuplicatedMissionPhaseError
        if start >= end:
            raise MissionPhaseDurationError

        self.phases[name] = MissionPhase(name, description, start, end)

    def get_mission_phase(self, name: str) -> MissionPhase:
        if name not in self.phases:
            raise NonExistingMissionPhaseError
        return self.phases[name]

    def get_mission_phases(self) -> list[str]:
        return list(self.phases.keys())

    @staticmethod
    def from_file(mission_phases_path: Path) :
        handler = MissionPhaseHandler()
        with mission_phases_path.open("r") as f:
            lines = f.readlines()
            # Skip header line
            for line in lines[1:]:
                name, description, start, end = line.strip().split(",")
                start_timestamp = datestr_to_timestamp(start)
                end_timestamp = datestr_to_timestamp(end)
                if start_timestamp >= end_timestamp:
                    logging.warning("Mission phase %s has an invalid duration", name)
                    continue
                handler.add_phase(name, description, start_timestamp, end_timestamp)
        return handler


class DuplicatedMissionPhaseError(Exception):
    pass

class NonExistingMissionPhaseError(Exception):
    pass

class MissionPhaseDurationError(Exception):
    pass
