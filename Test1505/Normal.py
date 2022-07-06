print("p1 : even odd numbers")
num = 2
if (num % 2) == 0:
    print("{0} is Even number".format(num))
else:
    print("{0} is Odd number".format(num))
print("If list is given to find even odd")
lisevenodd = [1, 2, 3, 4]
lenevenodd = len(lisevenodd)
for e in range(0, lenevenodd):
    num = lisevenodd[e]
    if (num % 2) == 0:
        print("{0} is Even number".format(num))
    else:
        print("{0} is Odd number".format(num))

print()
print("p2 : fibonise series till given number")
first = 0
second = 1
n = 10
for b in range(0, n):
    print(first)
    next = first + second
    first = second
    second = next

print()
print("p3 : find factorial pf given number")
n = 4
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("The factorial of 4 is : ", end="")
print(fact)
print("If list is given to find factorial")
lisfact = [1, 2, 3, 4]
len1 = len(lisfact)
fact = 1
for i in range(0, len1):
    n = lisfact[i]
    for j in range(1, n + 1):
        fact = fact * j
    print("The factorial of " + str(n) + "is : ", end="")
    print(fact)
    fact = 1

print()
print("p4 : prime no")
num = 1
flag = True
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num / 2) + 1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            flag = False
            print(num, "is not a prime number")
            break
if flag:
    print("It is prime number")
print("print 1 to 100 prime numbers")
temp = 0
for c in range(1, 100):
    for d in range(2, c):
        if c % d == 0:
            temp = temp + 1
    if temp == 0:
        print(c)
    else:
        temp = 0

print()
print("p5 : Reverse no")
revno = 12345
rev = 0
while revno != 0:
    r = revno % 10
    rev = rev * 10 + r
    revno = revno // 10
print(rev)

print()
print("p6 : Armstrong Number")
n = 153
num = 0
nu = n
while nu != 0:
    rem = nu % 10
    num = num + rem*rem*rem
    nu = nu // 10
if num == n:
    print("Armstrong")
else:
    print("Not armstrong")

print()
print("p7 : Swap 2 no")
x = 50
y = 40
x = x+y
y = x-y
x = x-y
print(x)
print(y)