import sys, time, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if len(sys.argv) != 5:
	print("ERROR: Improper commandline arguments!")
	print("Usage: python SouthwestCheckIn.py <confirmationNumber> <firstName> <lastName> <checkInTime>")
	exit()

# Set Confirmation Number, First Name, and Last Name (CheckIn Parameters)
confirmationNumber = sys.argv[1]
firstName = sys.argv[2]
lastName = sys.argv[3]
checkInTime = sys.argv[4]
date = datetime.datetime.strptime(checkInTime, "%m/%d/%Y-%H:%M")

print(date)
print(datetime.datetime.now().replace(hour=20))
delta = datetime.timedelta(minutes=1)
print(datetime.datetime.now() + delta)

while datetime.datetime.now() < date:
	time.sleep(1)

print(datetime.datetime.now())
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://www.southwest.com/')

checkInTab = driver.find_element_by_id('booking-form--check-in-tab')
checkInTab.click()

wait = WebDriverWait(driver, 10)
confirmationNumberBox = wait.until(EC.visibility_of_element_located((By.ID, 'confirmationNumber')))
confirmationNumberBox.send_keys(confirmationNumber)
firstNameBox = driver.find_element_by_id('firstName')
firstNameBox.send_keys(firstName)
lastNameBox = driver.find_element_by_id('lastName')
lastNameBox.send_keys(lastName)

checkInButton = driver.find_element_by_id('jb-button-check-in')
checkInButton.click()

reviewResultsCheckInButton = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'air-check-in-review-results--check-in-button')))
reviewResultsCheckInButton.click()

print("Successfully checked in passenger %s %s with confirmation number %s" %(firstName, lastName, confirmationNumber))
exit()
