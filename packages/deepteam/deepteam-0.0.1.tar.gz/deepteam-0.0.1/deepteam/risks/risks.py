from enum import Enum
from typing import Dict, Type

from deepteam.vulnerabilities import BaseVulnerability
from deepteam.vulnerabilities.types import *


class LLMRiskCategories(Enum):
    RESPONSIBLE_AI = "Responsible AI"
    ILLEGAL = "Illegal"
    BRAND_IMAGE = "Brand Image"
    DATA_PRIVACY = "Data Privacy"
    UNAUTHORIZED_ACCESS = "Unauthorized Access"


def getRiskCategory(
    vulnerability: Type[BaseVulnerability],
) -> LLMRiskCategories:
    risk_category_map: Dict[Type[BaseVulnerability], LLMRiskCategories] = {
        #### Responsible AI ####
        BiasType: LLMRiskCategories.RESPONSIBLE_AI,
        ToxicityType: LLMRiskCategories.RESPONSIBLE_AI,
        #### Illegal ####
        IllegalActivityType: LLMRiskCategories.ILLEGAL,
        GraphicContentType: LLMRiskCategories.ILLEGAL,
        PersonalSafetyType: LLMRiskCategories.ILLEGAL,
        #### Brand Image ####
        MisinformationType: LLMRiskCategories.BRAND_IMAGE,
        ExcessiveAgencyType: LLMRiskCategories.BRAND_IMAGE,
        RobustnessType: LLMRiskCategories.BRAND_IMAGE,
        IntellectualPropertyType: LLMRiskCategories.BRAND_IMAGE,
        CompetitionType: LLMRiskCategories.BRAND_IMAGE,
        #### Data Privacy ####
        PromptLeakageType: LLMRiskCategories.DATA_PRIVACY,
        PIILeakageType: LLMRiskCategories.DATA_PRIVACY,
        #### Unauthorized Access ####
        UnauthorizedAccessType: LLMRiskCategories.UNAUTHORIZED_ACCESS,
    }

    return risk_category_map.get(
        vulnerability, None
    )  # Returns None if not found
