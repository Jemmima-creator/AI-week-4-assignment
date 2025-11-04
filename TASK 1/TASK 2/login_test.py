from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Automatically installs and manages ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the test login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Initialize counters
total_tests = 2
passed_tests = 0

# --- Test 1: Valid Login ---
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

if "logged-in-successfully" in driver.current_url:
    print("Valid Login Test: Passed ")
    passed_tests += 1
else:
    print("Valid Login Test: Failed ")

# --- Test 2: Invalid Login ---
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID, "username").send_keys("wrong_user")
driver.find_element(By.ID, "password").send_keys("wrong_pass")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

if "Your username is invalid!" in driver.page_source:
    print("Invalid Login Test: Passed ")
    passed_tests += 1
else:
    print("Invalid Login Test: Failed ")

# --- Final Summary ---
success_rate = (passed_tests / total_tests) * 100
failure_rate = 100 - success_rate

print("\n--- TEST SUMMARY ---")
print(f"Total Tests: {total_tests}")
print(f"Passed: {passed_tests}")
print(f"Failed: {total_tests - passed_tests}")
print(f"Success Rate: {success_rate}%")
print(f"Failure Rate: {failure_rate}%")
import time
time.sleep(5)


driver.quit()
