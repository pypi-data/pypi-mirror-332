import random

from deepteam.attack_simulator.attack_enhancements import BaseAttackEnhancement
from .template import PromptInjectionTemplate


class PromptInjection(BaseAttackEnhancement):
    def enhance(self, attack: str) -> str:
        """Enhance the attack input using prompt injection techniques."""
        return random.choice(
            [
                PromptInjectionTemplate.enhance_1(attack),
                PromptInjectionTemplate.enhance_2(attack),
            ]
        )
