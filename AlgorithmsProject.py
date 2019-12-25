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
    # d is the size of the character set (26? 128? 256?)
    # q is used for modulo, generally a prime number
  
    # The value of h would be "pow(d, n-1)%q"
    for i in xrange(n-1):
        h = (h*d)%q
  
    # Calculate the hash value of pattern and first window of text
    for i in xrange(n):
        p = (d*p + ord(pat[i]))%q
        t = (d*t + ord(txt[i]))%q
        
 # Slide the pattern over text one by one
    for i in xrange(m-n+1):
        # Compare hash of current window in text with that of pattern; if match, do one by one 
        if p==t:
            # Check for characters one by one
            for j in xrange(n):
                if txt[i+j] != pat[j]:
                    break
            j+=1
            # if p == t and pat[0...n-1] = txt[i, i+1, ...i+n-1]
            if j==n:
                print "Pattern found at index " + str(i)
  
        # Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if i < n-m:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+n]))%q
            # We might get negative values of t, converting it to positive
            if t < 0:
                t = t+q

#Knuth-Morris-Pratt, https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
def computeLPSArray(pat, n, lps):
    len = 0 # length of the previous longest prefix suffix
  
    lps[0] # initialized to 0 outside the function
    i = 1
  
    # the loop calculates lps[i] for i = 1 to n-1
    while i < n:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1

def KMPSearch(pat, txt):
    n = len(pat)
    m = len(txt)
    # create and compute lps[] that will hold the longest prefix suffix values for pattern
    lps = [0]*n
    computeLPSArray(pat, n, lps)
    j = 0 # index for pat[]
    i = 0 # index for txt[]
    while i < m:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == n:
            print "Found pattern at index " + str(i-j)
            j = lps[j-1]
        # mismatch after j matches
        elif i < m and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters, they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1



                
def main():
    # Driver program to test Rabin-Karp 
    txt = "GEEKS FOR GEEKS"
    pat = "GEEK"
    q = 101 # A prime number 
    search(pat,txt,q)

    # Driver program to test Knuth-Morris Pratt
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    KMPSearch(pat, txt)

main()
