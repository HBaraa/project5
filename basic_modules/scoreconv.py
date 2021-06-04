# -*- coding: utf-8 -*-

def convert_score(score):
    # scores_id = []
    # for score in lst:
    nutriscore = None
    if score == "a":
        nutriscore = 1
    elif score == "b":
        nutriscore = 2
    elif score == "c":
        nutriscore = 3
    elif score == "d":
        nutriscore = 4
    elif score == "e":
        nutriscore = 5
    else:
        pass
    return nutriscore


if __name__ == "__main__":
    convert_score()
