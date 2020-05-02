#Get email of the last user to push to a github repository
import selenium
from selenium import webdriver

#Asks user for github repository of desired email
link = input("Paste the link to the github repo you want the email from: ")
driver = webdriver.Firefox()
driver.get(link)

# Send id information
class_box = driver.find_element_by_class_name('commits')

#Click Repository
class_box.click()

#Get most recent commit message
commit_box = driver.find_element_by_class_name('message')

#clicks most recent commit message
commit_box.click()

#Gets notes of push
newUrl = driver.current_url
newUrl+=(".patch")
driver.get(newUrl)

#Finds email within texts and prints
element = driver.find_element_by_xpath("//pre[contains(text(),'From:')]").text
if "From:" in element:
    output = element.splitlines()
    aNewOutput = output[1]
    finalString = aNewOutput.split("<",1)[1]
    print ("The email associated with the last push to this repository is: " + finalString[:-1])
driver.close()