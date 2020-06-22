# --------------
#Code starts here
def palindrome(num):
    temp = str(num)
    while(True):
        temp = str(int(temp) + 1)
        num = num + 1
        rev = temp[::-1]
        if(temp==rev):
            return num 
            break
        
p = palindrome(8)     
print(p)



# --------------
#Code starts here
def a_scramble(str_1, str_2):
    str1 = str_1.replace(' ', '')
    str2 = str_2.replace(' ', '')
    str1 = sorted(str1.lower())
    str2 = sorted(str2.lower())
    c = 0
    for j in str2:
        for k in str1:
            if (j == k):
                c = c + 1
                str1.remove(k)
                break
    if(c == len(str2)):
        return True
    else:
        return False


a = a_scramble("Tom Marvolo Riddle","Voldemort")
print(a)
    



# --------------
#Importing header files
from math import sqrt

#Code starts here

#Function to check for perfect square 
def is_perfect_square(x): 
    s = sqrt(x)
    return (int(s)*int(s) == x) 
 
#Function to check for fibonacci number
def check_fib(num):
    if is_perfect_square((5*num*num) + 4) or is_perfect_square((5*num*num) - 4): #Formula for checking fibonacci number
        return True
    
    return False     

#Code ends here


# --------------
#Code starts here

#Function to compress string
def compress(word):
    word=word.lower()
    mist=[]
    l=0
    while(l<len(word)):
        m=word[l]
        j=0
        while(l<len(word) and word[l]==m):
                 j=j+1
                 l=l+1    

        mist.append(m)
        mist.append(str(j))
    
    return ''.join(mist)

#Code ends here


# --------------
#Code starts here
def k_distinct(string, k):
    string = string.lower()
    unique = []
    for i in string:
        if i not in unique:
            unique.append(i)
        
    if(k == len(unique)):
        return True
    else:
        return False





