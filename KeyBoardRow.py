def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    key_board = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
                 ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
                 ['z', 'x', 'c', 'v', 'b', 'n', 'm']]

    # row_one = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    # row_two = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    # row_three = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    result = []
    for word in words:
        flag = -1
        count = 0
        flag_char_not_in_a_line = False
        for c in word.lower():
            if flag == -1:
                if c in key_board[0]:
                    flag = 0
                elif c in key_board[1]:
                    flag = 1
                elif c in key_board[2]:
                    flag = 2
                count += 1
            else:
                if c in key_board[flag]:
                    count += 1
                else:
                    flag_char_not_in_a_line = True
                    break
        if not flag_char_not_in_a_line:
            result.append(word)

    return result





if __name__=="__main__":
    words = ["Hello", "Alaska", "Dad", "Peace"]
    print(findWords(words))