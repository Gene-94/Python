from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
import os

token = input("paste your token here: ")

os.environ['GH_TOKEN'] = token

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get("https://teams.microsoft.com")
sleep(7)
auth_user = browser.find_element_by_css_selector("#i0116")
auth_user.send_keys("5926205@formacao.iefp.pt")
auth_btn = browser.find_element_by_css_selector("#idSIButton9")
auth_btn.click()
sleep(3)
auth_user = browser.find_element_by_css_selector("#i0118")
auth_user.send_keys("iEFP10121994")
auth_btn = browser.find_element_by_css_selector("#idSIButton9")
auth_btn.click()
sleep(30)
auth_btn = browser.find_element_by_css_selector("#app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c")
auth_btn.click()
sleep(5)
auth_btn = browser.find_element_by_css_selector(".root-138")
auth_btn.click()