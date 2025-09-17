#!/usr/bin/env python3
def average(scores):
    if not scores:
        return 0.0

    total = sum(scores.values())
    count = len(scores)
    return round(total / count, 2)


if __name__ == "__main__":
    class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9,
    }

    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13,
    }

    print("Class 3B average:", average(class_3B))
    print("Class 3C average:", average(class_3C))