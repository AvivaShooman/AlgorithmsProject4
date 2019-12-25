#!/usr/bin/env python3
import re

def clean_text(filename):
    # open file and read text                                                                                                                             
    f = open(filename)
    text = f.readlines()

    # convert text to lowercase letters 
    lowerCaseString = text[0].lower()

    # remove anything that is not a letter
    newString = ""
    pattern = "[a-z]"

    for c in lowerCaseString:
        if re.match(pattern, c):
            newString += c

    count = len(newString)

    print("The name of the file is", filename)
    print("The number of characters our file contains:", count)
    print(newString)
    
    return newString

#Rabin Karp, https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/
def search(pat, txt, q):
    n = len(pat)
    m = len(txt)
    i = 0
    j = 0
    p = 0	# hash value for pattern
    t = 0	# hash value for txt
    h = 1
    d = 26 #Here because we use lowercase letters as our character set
    
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
        # Count the number of hash value comparisons
        count_m += 1 
        # Compare hash of current window in text with that of pattern; if match, do one by one 
        if p==t:
            # Check for characters one by one
            for j in range(n):
                # Count the number of letter by letter comparisons
                count_n += 1
                if txt[i+j] != pat[j]:
                    break
                
            j+=1
            # if p == t and pat[0...n-1] = txt[i, i+1, ...i+n-1]
            if j==n:
                print("Pattern found at index " + str(i))
  
        # Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if i < m-n:  

            t = (d*(t-ord(txt[i])*h) + ord(txt[i+n]))%q
            # We might get negative values of t, converting it to positive
            if t < 0:
                t = t+q
                
    return count_m + count_n
    
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
    #Set up test data
    pat_list1 = ['art', 'thebeg', 'cret', 'ans', 'andthe', 'the', 'ear', 'thy', 'inni', 'in']
    pat_list2 = ['daysandyears', 'luminary', 'lightup', 'yield', 'andfor', 'founded', 'appoint', 'andtheyshallbeforsigns', 'toseparatebetween', 'torah']
    pat_list3 = ['greatcity', 'lesha', 'masterofthesoil', 'youshallnoteat', 'accordingly', 'scatterplot', 'thesearethegenerations', 'befruitfulandmultiply', 'establishmycovenant', 'therainbowshallbeintheclouds']
    pat_list4 = ['heavenward', 'greatcity', 'daysandyears', 'art', 'scatterplot', 'torah', 'andfor', 'iwillmakeyouexceedinglyfruitful', 'abrahamwascircumcised', 'thelandthatiwillshowyou']
    text_files = [('./10_words.txt', pat_list1), ('./100_words.txt', pat_list2), ('./1000_words.txt', pat_list3), ('./10000_words.txt', pat_list4)]
    ans1 = 0
    ans2 = 0

    for File in text_files:
        print("")
        print("The file we are on is", File)
        
        # Driver program to test Rabin-Karp 
        txt = clean_text(File[0])
        q = 101 # A prime number
        pat = File[1]
        
        for i in range(len(pat)):
            print("The pattern is", pat[i])
            ans1 = search(pat[i], txt, q)
            print("The number of comparisons RK is", ans1)

            # Driver program to test Knuth-Morris Pratt
            ans2 = KMPSearch(pat[i], txt)
            print("The number of comparisons KMP is", ans2)

main()
