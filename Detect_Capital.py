def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    if word.isupper():
        return True
    if word.islower():
        return True
    if word[0].isupper() and word[1:].islower():
        return True
    else:
        return False


if __name__ == "__main__":
    a = "Google"
    print(detectCapitalUse(a))

    a = "USA"
    print(detectCapitalUse(a))

    a = "FlAg"
    print(detectCapitalUse(a))

    a = "A"
    print(detectCapitalUse(a))

    a = "leetcode"
    print(detectCapitalUse(a))