import random
from typing import List

spouses = {"wife": "musical", "husband": "football"}


def wife_choice() -> str:
    return random.choice(list(spouses.values()))


def husband_choice() -> str:
    return random.choice(list(spouses.values()))


def compare_choices() -> List[int]:
    w_c = wife_choice()
    h_c = husband_choice()
    if w_c == h_c:
        print("Both win !")
        if w_c == spouses["wife"]:
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
    print(compare_choices())
