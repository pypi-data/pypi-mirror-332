from typing import List

from deepteam.vulnerabilities import BaseVulnerability
from deepteam.vulnerabilities.robustness import RobustnessType


class Robustness(BaseVulnerability):
    def __init__(self, types: List[RobustnessType]):
        if not isinstance(types, list):
            raise TypeError(
                "The 'types' attribute must be a list of RobustnessType enums."
            )
        if not types:
            raise ValueError("The 'types' attribute cannot be an empty list.")
        if not all(isinstance(t, RobustnessType) for t in types):
            raise TypeError(
                "All items in the 'types' list must be of type RobustnessType."
            )
        super().__init__(types=types)

    def get_name(self) -> str:
        return "Robustness"
