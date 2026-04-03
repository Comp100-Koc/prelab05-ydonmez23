def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    
    a = len(s)
    full = 0 
    word = "" 
    
    for i in range(a):
        start, stop = i, i 
        while start >= 0 and stop < a and s[start] == s[stop]:
            if (stop - start + 1) > full:
                full = stop - start + 1
                word = s[start:stop+1]
            start -= 1
            stop += 1
            
        start, stop = i, i + 1 
        while start >= 0 and stop < a and s[start] == s[stop]: 
            if (stop - start + 1) > full:
                full = stop - start + 1
                word = s[start:stop+1]
            start -= 1
            stop += 1

    if full < 2:
        return ""  

    return word