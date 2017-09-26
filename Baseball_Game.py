def calPoints(ops):
    """
    :type ops: List[str]
    :rtype: int
    """
    # exclude_invalid_list = []
    # for k, v in enumerate(ops):
    #     if v != "C":
    #         exclude_invalid_list.append(v)
    #     else:
    #         exclude_invalid_list.pop(-1)
    # print(exclude_invalid_list)
    #
    # round_score = [0]
    # score_sum = [0]
    # for i in xrange(len(exclude_invalid_list)):
    #     try:
    #         score = int(exclude_invalid_list[i])
    #
    #     except ValueError:
    #         if exclude_invalid_list[i] == "D":
    #             score = round_score[i] * 2
    #
    #         elif exclude_invalid_list[i] == "+":
    #             score = round_score[i] + round_score[i - 1]
    #
    #     round_score.append(score)
    #     score_sum.append(score_sum[i] + score)
    # return score_sum[-1]
    round_points = []
    for c in ops:
        if c.lstrip('+-').isdigit():
            round_points.append(int(c))
        elif c == "C":
            round_points.pop(-1)
        elif c == "D":
            round_points.append(round_points[-1] * 2)
        elif c == "+":
            round_points.append(sum(round_points[-2: ]))
    return sum(round_points)


if __name__ == "__main__":
    s = ["5","2","C","D","+"]
    print(str(calPoints(s)))
    s = ["5","-2","4","C","D","9","+","+"]
    print(str(calPoints(s)))
