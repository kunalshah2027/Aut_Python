import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support import expected_conditions as EC

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#Print alternate cvharacters from s string and then remove duplicate characters from
# the new string with printing duplicate letter at one time
#write a request get call and va;idate few fields
print("Try programiz.pro")
s = "perficient india pvt ltd"
s1 = ""
for v in range(0, len(s)):
    if v % 2 == 0:
        # print(s[v])
        s1 = s1 + s[v]
print(s1)
# o/p = prinvt
dictact = {}
s1 = s1.replace(" ","")
for i in range(0, len(s1)):
    counter = 0
    for j in range(0, len(s1)):
        if j < i and s1[i] == s1[j]:
            break
        if s1[i] == s1[j]:
            counter = counter + 1
        if j == len(s1) - 1:
            dictact[s1[i]] = counter
print(dictact)
for k, v in dictact.items():
    print(k)




