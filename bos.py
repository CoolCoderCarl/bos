import random
from typing import List


class Spouses:
    preferred_choices = {"wife": "musical", "husband": "football"}

    def spouse_choice(self) -> str:
        return random.choice(list(self.preferred_choices.values()))

    def compare_choices(self, wife_choice, husband_choice) -> List[int]:
        w_c = wife_choice
        h_c = husband_choice
        if w_c == h_c:
            print("Both win !")
            if w_c == self.preferred_choices["wife"]:
                print(f"Wife choose {w_c}; husband choose {h_c}")
                return [2, 1]
            else:
                print(f"Husband choose {h_c}; wife choose {w_c}")
                return [1, 2]
        else:
            print("Both lost")
            print(f"Wife choose {w_c}")
            print(f"Husband choose {h_c}")
            return [0, 0]


if __name__ == "__main__":
    wife = Spouses().spouse_choice()
    husband = Spouses().spouse_choice()
    comparing = Spouses()
    comparing.compare_choices(wife, husband)
