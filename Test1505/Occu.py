s = "aaaaaffkendfnfndfb"
arr = [1, 1 ,1, 2 , 3 , 4 , 5 , 6 , 7 , 8,2 , 7 , 4 , 4]
print("P1 : Occurance Of each char of array Using Count-->")
print("Given Array is " + str(arr))
print("Expected output is occ of 1=3, 2=2, 3=1, 4=3, 5=1, 6=1, 7=2, 8=1")
print("In this we are using count fun to get ele count and then putting that "
      "ele to empty array to avoid repeated chacking of element then for "
      "fetching valu of specific key we are storing it in dict as k , v pair")
arrdup = []
occdict = {}

for oc in arr:
    if oc not in arrdup:
        cn = arr.count(oc)
        print("occ of " +str(oc)+ " is " +str(cn)+ " time")
        arrdup.append(oc)
        occdict[str(oc)] = str(cn)
print(occdict)
print(occdict.get('3'))
print()

print("P2 : Occurance Of each char of array Using For loop-->")
print("Given Array is " + str(arr))
print("Expected output is occ of 1=3, 2=2, 3=1, 4=3, 5=1, 6=1, 7=2, 8=1")
occdict = {}
for oc in arr:
    if oc not in occdict:
        occdict[oc] = 1
    else:
        occdict[oc] += 1
print(occdict)
print()

print("P3 : Occurance Of each char of String -->Same code as array")
print("Given string is " + s)
print("Expected string is a=5, b=1, d=2, e=1, f=5, k=1, n=3")
arrdup = []
occdict = {}
for oc in s:
    if oc not in arrdup:
        cn = s.count(oc)
        print("occ of " +str(oc)+ " is " +str(cn)+ " time")
        arrdup.append(oc)
        occdict[str(oc)] = str(cn)
print(occdict)
print(occdict.get('f'))
print()

print("P4 : Occurance Of each char of String Using For loop-->Same code as array")
print("Given string is " + s)
print("Expected string is a=5, b=1, d=2, e=1, f=5, k=1, n=3")
occdict = {}
for oc in s:
    if oc not in occdict:
        occdict[oc] = 1
    else:
        occdict[oc] += 1
print(occdict)
print()

print("P5 : Get non repeated characters from array Using count and for loop")
print("Given Array is " + str(arr))
print("Expected  is [3, 5, 6, 8] ")
arrnondup = []
for oc in arr:
    if arr.count(oc) == 1:
        #print("Non Repeated Character in arr is " +str(oc))
        arrnondup.append(str(oc))
arrnondup.sort()
print(arrnondup)
occdict = {}
for oc in arr:
    if oc not in occdict:
        occdict[oc] = 1
    else:
        occdict[oc] += 1
for oc in arr:
    if occdict[oc] == 1:
        print(oc , end =" ")
print()
print()

print("P6: Get non repeated characters from String Using count and For loop --> Same code as array")
print("Given string is " + s)
print("Expected string is [b, e, k] ")
arrnondup1 = []
for oc in s:
    if s.count(oc) == 1:
        #print("Non Repeated Character in arr is " +str(oc))
        arrnondup1.append(str(oc))
arrnondup1.sort()
print(arrnondup1)
occdict = {}
for oc in s:
    if oc not in occdict:
        occdict[oc] = 1
    else:
        occdict[oc] += 1
for oc in s:
    if occdict[oc] == 1:
        print(oc , end =" ")
print()
print()

print("P7: Get First non repeated characters from Array and string")
print("Given array is " + str(arr))
print("Expected string is 3 ")
print("Given string is " + s)
print("Expected string is b ")
print(arrnondup[0])
print(arrnondup1[0])
print()

print("P8 : Find occurance of word in string")
s = "Java is good but python is very good"
print("Given string is " + s)
print("Expected string for occ of is word is : 2")
cn = s.count("is")
print("occ of is word is : " +str(cn)+ " time")
print("Also if you dont want count fun then you can split the string and "
      "compare with the given word and increase counter")
counter = 0
for kj in s.split():
    if kj == "is":
        counter = counter + 1
print("occ of is word is : " +str(counter)+ " time")

print("P9 : Find occurance of word in string from file")
s = "Java is good but python is very good Java is good but python is very good"
print("Given string is " + s)
print("Expected string for occ of is word is : 4")
file = open("F:\Aut_Python\data\occ.txt", "r")
#read content of file to string
data = file.read()
#get number of occurrences of the substring in the string
occurrences = data.count("is")
print(occurrences)