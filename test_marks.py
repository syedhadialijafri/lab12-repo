import os
from selenium import webdriver
from selenium.webdriver.common.by import By

tests = [("-1","Rejected"),("0","Accepted"),("5","Accepted"),("10","Accepted"),("11","Rejected")]
path = "file:///" + os.path.abspath("index.html").replace("\\", "/")
driver = webdriver.Chrome()
passed = 0
print(f"{'Input':<8}{'Expected':<12}{'Actual':<12}Result")
try:
    for val, expected in tests:
        driver.get(path)
        box = driver.find_element(By.ID, "mark")
        box.clear(); box.send_keys(val)
        driver.find_element(By.ID, "submit").click()
        actual = driver.find_element(By.ID, "result").text
        ok = actual == expected
        passed += ok
        print(f"{val:<8}{expected:<12}{actual:<12}{'PASS' if ok else 'FAIL'}")
finally:
    driver.quit()
print(f"{passed}/{len(tests)} tests passed")
