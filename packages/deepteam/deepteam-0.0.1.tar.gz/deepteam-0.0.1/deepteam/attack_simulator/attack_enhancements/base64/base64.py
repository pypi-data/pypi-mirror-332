import base64
from deepteam.attack_simulator.attack_enhancements import BaseAttackEnhancement


class Base64(BaseAttackEnhancement):
    def enhance(self, attack: str) -> str:
        """Enhance the attack using Base64 encoding."""
        return base64.b64encode(attack.encode()).decode()
