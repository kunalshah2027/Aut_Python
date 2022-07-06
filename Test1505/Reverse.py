s = "I am kunal"
s1 = ""
print("P1 : Reverse the entire String and its words also Using For lOOP")
print("Given string is " + s)
print("Expected string is lanuk ma I")
for i in s:
    s1 = i + s1
print(s1)
print()

print("P2 : Reverse the entire String and its words also Using Slicing")
print("Slice means [start,stop,step], giving no field as start and stop indicates default to 0 and string "
      "length respectively and “-1” denotes starting from end and stop at the start, hence reversing string.")
print("Given string is " + s)
print("Expected string is lanuk ma I")
print(s[::-1])
print()

print("P3 : Reverse the entire String and its words also Using Reversed")
print("The reversed() returns the reversed iterator of the given string and then "
      "its elements are joined empty string separated using join(). And reversed order string is formed.")
print("Given string is " + s)
print("Expected string is lanuk ma I")
s = "".join(reversed(s))
print(s)
print()

print("P4: Reversed entire String but not words")
print("In this we will split the string first and then print it in reversed order using "
      "for loop with s3 at end and simply adding element before s3 to print it in reverse order"
      "also we can use .join function with reversed for printing splitted list in reverse order")
s = "I am kunal"
print("Given string is " + s)
print("Expected string is kunal am I")
s2 = s.split()
s3 = ""
print(s2)
for rev in s2:
    s3 = rev + " " + s3
print("Output using for loop : " + s3)
print("Output using .join fun : " + " ".join(reversed(s2)))
print()

print("P5: Do not Reverse entire String but Reverse words at same place")
print("Given string is " + s)
print("Expected string is I ma lanuk")
print("In this we will split the string first and then print it in same order using "
      "for loop with s3 at starting and reversing the individual word and storing it in new string.")
print("Also We can write it using .join as for each splited word in s we will rever it first and then join by space")
s2 = s.split()
print(s2)
s3 = ""
for rev in s2:
    s3 = s3 + rev[::-1] + " "
print("Output using for loop : " + s3)
print("Output using .join fun : " + " ".join(word[::-1] for word in s.split(" ")))
print()

print("P6 : Reverse the entire String and its words also with keeping space intact")
print("Given string is I am kunal")
print("Expected string is l an ukmaI")
print("We will first find space postion in oroginal string then we will reverse the string and store it in s2"
      "will remove all spaces from s2 then will add spaces at positions we find above using for "
      "loop and concatination.")
s = "This is Python"
s2 = ""
s3 = ""
for j in range(len(s)):
    if s[j] == " ":
        print("Space at " + str(j) + " postion")
for ele in s:
    s2 = ele + s2
s2 = s2.replace(" ", "")
print(s2)
for k in range(len(s2)):
    if k == 4 or k == 6:
        s3 = s3 + " " + s2[k]
    else:
        s3 = s3 + s2[k]
print(s3)
print()

print("P7 : Reverse elements of array")
print("Python does not have built-in support for Arrays, but Python Lists can be used instead.")
print("we can use reverse() , slicing , For loop using range function with 3 args - range [start ,stop .step]"
      "so here in our case it startes from last index of arr and stops at -1 with step of -1 meeans "
      "substracting -1 from last index. , also using reversed() ")
print("end =" " is used to print output in same line")
arr = [1, 2, 3, 4, 5, 6, 7, 8]
print("Array is :", arr)
arr.reverse()
# it workd as sort in java as it modifies arr directly so It will return none if you directly print(arr.reverse())
print("Output Using reverse () : " + str(arr))
# The original array
arr = [11, 22, 33, 44, 55]
print("Array is :", arr)
res = arr[::-1]  # reversing using list slicing
print("Output Using Slicing :", res)
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=" ")
print()
for i in reversed(arr):
    print(i, end=" ")

print()
print("P8 : Replace Alternate Character to Uppercase")
k = "python is easy"
knew = ""
print("Given String is " + k)
print("Expected String is PyThOn iS EaSy")
for cas in range(len(k)):
    if cas % 2 == 0:
        knew = knew + k[cas].upper()
    else:
        knew = knew + k[cas]
print(knew)

print()
print("P9: Replace First Character to Uppercase For single word string")
k = "python"
print("Given String is " + k)
print("Expected Python")
uppercase_string=k.capitalize()
print(uppercase_string)
print("using for loop")
new_string=""
for i in range(len(k)):
   if i==0:
        new_string=new_string + k[i].upper()
   else:
        new_string=new_string + k[i]
print(new_string)

print()
print("P10: remove space ,reverse str and print odd position char")
k = "I am kunal"
print("Given String is " + k)
print("Expected lnka")
ksp = k.replace(" ","")
ksp2 =""
for i in ksp:
    ksp2 = i + ksp2
print(ksp2)
for cas in range(len(ksp2)):
    if cas % 2 == 0:
        print(ksp2[cas])

print()
print("P11: Check how many digits and letters are in string")
k = "kunal2027"
print("Given String is " + k)
print("Expected 5 and 4")
# initialized value
total_digits = 0
total_letters = 0
# iterate through all characters
for s in k:
    # if character is digit (return True)
    if s.isnumeric():
        total_digits = total_digits + 1
    # if character is letter (return False)
    else:
        total_letters = total_letters + 1
print("Total letters found :-", total_letters)
print("Total digits found :-", total_digits)

print()
print("P12: swap two strings")
a = "kunal"
b = "shah"
print("Given String is " + a +" "+ b)
print("Expected shah kunal")
a = a + b
#Extract str2 from updated str1
#in our case it will be substring(0, (9-4)).
#It will assign string a to b
b = a[0 : (len(a) - len(b))]
#Extract str1 from updated str1
#we need to extract string from in length(b) till end of the string.
#In our case it will be substring(5).
#It will assign string shah to a
a = a[len(b):]
print(a + " " +b)

print()
print("P13: Find no of vowels in string")
a = "life is good"
print("Given String is " + a)
print("Expected 5")
count = 0
# Creating a set of vowels
vowel = set("aeiouAEIOU")
for vo in a:
    if vo in vowel:
        count = count + 1
print("No. of vowels :", count)
