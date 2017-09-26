def lengthOfLongestSubstring(s):
    """
    :param s:
    :return: int
    """
    max_length = 0
    start_index = 0
    end_index = -1
    if len(s) == 0:
        return max_length

    while start_index < len(s) and end_index < len(s)-1:
        try:
            match_index = str(s[start_index: end_index + 1]).index(s[end_index + 1])
            start_index += match_index + 1
        except ValueError:
            pass
        end_index += 1
        max_length = max_length if max_length > (end_index - start_index + 1) else (end_index - start_index + 1)

    return max_length


if __name__=='__main__':
    # s = "abcjeudisdsoejse"
    # s = "abcabcbb"
    # s = "a"
    s = ""
    max_length = lengthOfLongestSubstring(s)
    print(max_length)