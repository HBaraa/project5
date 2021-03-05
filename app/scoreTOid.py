# -*- coding: utf-8 -*-
def convert_score(lst):
    scores_id = []
    for score in lst:
        if score == "a":
            score_id = 1
            scores_id.append(score_id)
        elif score == "b":
            score_id = 2
            scores_id.append(score_id)
        elif score == "c":
            score_id = 3
            scores_id.append(score_id)
        elif score == "d":
            score_id = 4
            scores_id.append(score_id)
        elif score == "e":
            score_id = 5
            scores_id.append(score_id)
        else:
            pass
    return scores_id


if __name__ == "__main__":
    convert_score(lst)
