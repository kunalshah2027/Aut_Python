s = "aaaaaffkendfnfndfb"
arr = [1, 1 ,1, 2 , 3 , 4 , 5 , 6 , 7 , 8,2 , 7 , 4 , 4]
substring = "kunfjkvjvkunsk"
print("P1 : Remove all Occurance Of each char of array /Remove duplicates -->")
print("Given Array is " + str(arr))
print("Expected output is 12345678")
arrdup = []
for oc in arr:
    if oc not in arrdup:
        arrdup.append(oc)
print(arrdup)
print()

print("P2 : Remove all Occurance Of each char of String /Remove duplicates -->")
print("Given string is " + s)
print("Expected string is afkendb")
arrdup = []
for oc in s:
    if oc not in arrdup:
        arrdup.append(oc)
print(str(arrdup))
print("For printin list as string or to conver list to string we have to "
      "take one empty string then use join fun as emptystring.join(list) "
      "and directly put this statement in print statement")
stt = ""
print(stt.join(arrdup))
print()

print("P3 : Remove all Occurance Of substring of String /Remove duplicates ")
print("Given string is " + substring)
print("Expected string is fjkvjvsk")
occdict = {}
print(substring.replace("kun", ""))