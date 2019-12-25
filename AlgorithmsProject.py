#!/usr/bin/env python3

#Rabin Karp, https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/
def search(pat, txt, q):
    n = len(pat)
    m = len(txt)
    i = 0
    j = 0
    p = 0	# hash value for pattern
    t = 0	# hash value for txt
    h = 1
    d = 26 # d is 26 here because only lowercase letters
    
    # d is the size of the character set (26? 128? 256?)
    # q is used for modulo, generally a prime number

    # Initialize variables for counting operations
    count_m = 0
    count_n = 0

    # The value of h would be "pow(d, n-1)%q"
    for i in range(n-1):
        h = (h*d)%q
  
    # Calculate the hash value of pattern and first window of text
    for i in range(n):
        p = (d*p + ord(pat[i]))%q
        t = (d*t + ord(txt[i]))%q
        
 # Slide the pattern over text one by one
    for i in range(m-n+1):
        count_m += 1
        # Compare hash of current window in text with that of pattern; if match, do one by one 
        if p==t:
            # Check for characters one by one
            for j in range(n):
                if txt[i+j] != pat[j]:
                    break
                else:
                    count_n += 1
            j+=1
            # if p == t and pat[0...n-1] = txt[i, i+1, ...i+n-1]
            if j==n:
                print("Pattern found at index " + str(i))
  
        # Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if i < n-m:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+n]))%q
            # We might get negative values of t, converting it to positive
            if t < 0:
                t = t+q
                
    return count_n, count_m, count_m * count_n

#Knuth-Morris-Pratt, https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
def computeLPSArray(pat, n, lps):
    len = 0 # length of the previous longest prefix suffix
  
    lps[0] # initialized to 0 outside the function
    i = 1

    # Track count
    count_n = 0
  
    # the loop calculates lps[i] for i = 1 to n-1
    while i < n:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
            count_n += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1
                count_n += 1
    return count_n
                
def KMPSearch(pat, txt):
    n = len(pat)
    m = len(txt)
    # create and compute lps[] that will hold the longest prefix suffix values for pattern
    lps = [0]*n
    count_n = computeLPSArray(pat, n, lps)
    j = 0 # index for pat[]
    i = 0 # index for txt[]

    count_m = 0
    
    while i < m:
        if pat[j] == txt[i]:
            i += 1
            j += 1
            count_m += 1
        if j == n:
            print("Found pattern at index " + str(i-j))
            j = lps[j-1]
        # mismatch after j matches
        elif i < m and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters, they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
                count_m += 1
    return count_n + count_m

def main():
    # Driver program to test Rabin-Karp 
    txt = "GEEKS FOR GEEKS"
    pat = "GEEK"
    q = 101 # A prime number
    ans = 0
    ans = search(pat,txt,q)
    print("The number of comparisons is", ans)

    # Driver program to test Knuth-Morris Pratt
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    ans = KMPSearch(pat, txt)
    print("The number of comparisons is", ans)

main()
