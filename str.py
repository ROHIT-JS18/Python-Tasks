# Ek string ko reverse karo (without using [::-1]).

'''
str = "Apple"
new_str = ""
i = -1
while i != -6:
    new_str = new_str + str[i]
    i = i - 1
print(new_str)  

'''

# Ek function likho jo count kare string me vowels kitne hain.

'''
str = "Apple"
tuple = ['a','e','i','o','u']

for i in range(0,len(str)):
    if str[i].lower() in tuple :
        print(str[i],'this is a vowel')
    else:
        print(str[i],'This is not a vowel')

'''

# Ek function likho jo count kare string me consonants kitne hain.
'''str = "Apple"
tuple = ['a','e','i','o','u']
count = 0
for i in range(0,len(str)):
    if str[i].lower() not in tuple :
        # print(str[i],'this is a consonants')
        count = count+1
    # else:
    #     # print(str[i],'This is a vowel')
print(count)'''

# Check karo string palindrome hai ya nahi.

'''Palindrome => SOS '''

'''str = str(input('Enter a string :- '))
new_str = ""
i = -1
while i != -len(str)-1:
    new_str = new_str + str[i]
    i = i - 1 

if new_str == str :
    print('This is palindrome string')
else:
    print("This is not a palindrome string")'''

# Ek string me se saare spaces remove karo.

'''
str = "' Happy birthday Jon '"
'This time we have a string function name '
new = str.replace(' ','')
print(new)
'''

# Ek function likho jo string ka first and last character swap kare.

'''
str = str(input('Enter a string :- '))

for i in str:
    if i == str[0]:
        i = str[-1]
    elif i == str[-1]:
        i = str[0]
    print(i,end="")

'''

# Ek function likho jo string ko uppercase me convert kare (without using .upper()).
# str = 'rohit'

# Ek function likho jo string ko lowercase me convert kare (without using .lower()).

# Ek string me kisi specific character ki frequency count karo.
' frequency count = how many times a character occur'
'''input = 'hello_world'
print(input.count('l'))'''
# Check karo do strings anagram hain ya nahi.

'''str1 = str(input('Enter a string :- '))
str2 = str(input('Enter a string :- '))
new_str = ""
i = -1
while i != -len(str1)-1:
    new_str = new_str + str1[i]
    i = i - 1 

if new_str == str2 :
    print('anagram') 
else:
    print('Not anagram')'''

# Ek sentence me total words count karo.

'''
str = 'i am Rohit'
count = 0
for i in str:
    if i == ' ':
        pass
    else:
        count+=1

print(count)

'''
# Sentence ke har word ka first letter capital karo (without using .title()).
str = 'roy is boy'
a = str.capitalize()
print(a)
# Ek function likho jo duplicate characters remove kare.

# Ek function likho jo string me sab digits alag extract kare.

# Ek function likho jo string me sirf alphabets extract kare.

# Ek function likho jo check kare string me saare characters unique hain ya nahi.

# Ek function likho jo longest word in a sentence return kare.

# Ek function likho jo smallest word in a sentence return kare.

# Ek function likho jo kisi substring ka occurrence count kare (without using .count()).

# Ek function likho jo string rotation check kare (e.g., "abcde" and "cdeab").

# Ek function likho jo recursion se factorial nikale.

# Recursion se Fibonacci number nikalo.

# Ek function likho jo kisi number ko binary me convert kare (without using bin()).

# Ek function likho jo check kare number Armstrong hai ya nahi.

# Ek program likho jo kisi list ko manually sort kare (without sort()).

# Ek function likho jo dictionary ko value ke basis par sort kare.

# Ek function likho jo string me character frequency count kare.

# Ek function likho jo matrix transpose kare.

# Ek function likho jo nested list ko flatten kare.

# Ek mini project:
# Ek simple Student Management System banao jisme:

# Add student

# Remove student

# Search student

# Display all students