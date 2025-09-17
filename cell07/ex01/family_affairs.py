#!/usr/bin/env python3
def find_red_hair(family):
    red_list = []
    for name, color in family.items():
        if color == "red":
            red_list.append(name)
    return red_list


if __name__ == "__main__":
    family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red",
    }

    print(find_red_hair(family))