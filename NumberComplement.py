# coding=utf-8
def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    '''
    Given a positive integer, output its complement number. The complement strategy is to flip 
    the bits of its binary representation.
    Note:
    The given integer is guaranteed to fit within the range of a 32-bit signed integer.
    You could assume no leading zero bit in the integer’s binary representation.
    
    Integer is 32bit signed, so the 31th bit is sign, 30~0th bit is number
    
        
        00001101
        11111111
        11110010
    
        00000010
    
        00001101
    &	10000000 == 0
    &	01000000 == 0
        ... ...
    &	00001000 != 0 (1000)
    & 	00000100 != 0 (100)
    &	00000010 == 0		
    &	00000001 != 0 (1)
    '''
    sign_flag = True if num & (1 << 31) != 0 else False
    flag = False
    result = 0
    for offset in xrange(30, -1, -1):
        if num & (1 << offset) == 0:
            if flag:
                result += 1 << offset
            else:
                continue
        else:
            if not flag:
                flag = True

    if sign_flag:
        result = -result

    return result

if __name__ == "__main__":
    num = [1,5]
    for i in num:
        print(findComplement(i))