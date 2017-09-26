def distributeCandies(candies):
    """
    :type candies: List[int]
    :rtype: int
    """
    kinds = len(list(set(candies)))
    return kinds if kinds <= len(candies) / 2 else len(candies) / 2


if __name__ == "__main__":
    candies = [1,1,1,1,2,2,2,3,3,3]
    print(distributeCandies(candies))