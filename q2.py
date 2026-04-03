def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''

    while adjacent_duplicates_exist(s):
        result = ""
        for i in range(len(s)):
            if i < len(s)-1 and s[i] == s[i+1]:
                result += s[i+2:]
                break
            
            else:
                result += s[i]
        s = result
    return s

def adjacent_duplicates_exist(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False