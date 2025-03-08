from typing import List

from deepteam.vulnerabilities import BaseVulnerability
from deepteam.vulnerabilities.toxicity import ToxicityType


class Toxicity(BaseVulnerability):
    def __init__(self, types: List[ToxicityType]):
        if not isinstance(types, list):
            raise TypeError(
                "The 'types' attribute must be a list of ToxicityType enums."
            )
        if not types:
            raise ValueError("The 'types' attribute cannot be an empty list.")
        if not all(isinstance(t, ToxicityType) for t in types):
            raise TypeError(
                "All items in the 'types' list must be of type ToxicityType."
            )
        super().__init__(types=types)

    def get_name(self) -> str:
        return "Toxicity"
