import os
import sys 
from selenium import webdriver

# define the name of directory where folder will be created
path = "path/to/directory"
browser = webdriver.Chrome()
browser.get("http://github.com/login")

def create():
	newFolderName = str(sys.argv[1])
	os.mkdir(path + newFolderName)
	#select username field in browser and insert username
	login_user = browser.find_elements_by_xpath("//*[@id='login_field']")[0]
	login_user.send_keys('MY_USERNAME') #add your gitHub username here
	#select password field in browser and insert password
	login_user = browser.find_elements_by_xpath("//*[@id='password']")[0]
	login_user.send_keys('MY_PASSWORD') #add your gitHub password here
	#select login button and click
	login_user = browser.find_elements_by_xpath("//*[@id='login']/form/div[3]/input[4]")[0]
	login_user.click()
	#navigate to create new repo
	browser.get("http://github.com/new")
	create_repo = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]
	create_repo.send_keys(newFolderName)
	create_repo = browser.find_elements_by_xpath("//*[@id='new_repository']/div[3]/button")[0]
	create_repo.submit() #create new repo
	browser.quit()

if __name__ == "__main__":
	create()

