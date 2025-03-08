from deepteam.attack_simulator.attack_enhancements import BaseAttackEnhancement


class Rot13(BaseAttackEnhancement):
    def enhance(self, attack: str) -> str:
        """Enhance the attack using ROT13 encoding."""
        return attack.translate(
            str.maketrans(
                "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm",
            )
        )
