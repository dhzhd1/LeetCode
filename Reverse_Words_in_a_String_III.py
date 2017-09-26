def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    word_list = s.split(' ')
    for i in xrange(len(word_list)):
        word_list[i] = word_list[i][::-1]
    return ' '.join(word_list)

if __name__=="__main__":
    s = "Let's take LeetCode contest"
    print(reverseWords(s))