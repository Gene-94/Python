#! ~/Programas/Python/Lab/.venv/bin/python3

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
print("# Info de login da Alura #")
user = input("Nome de utilizador: ")
passwd = input("Password: ")

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get("https://cursos.alura.com.br/course/javascript-programando-na-linguagem-web/task/23665")
while(True):
    try:
        button = browser.find_element_by_css_selector("a.task-actions-button-next:nth-child(1)")
        sleep(3)
    except:
        auth_user = browser.find_element_by_css_selector("#login-email")
        auth_user.send_keys(user)
        auth_pass = browser.find_element_by_css_selector("#password")
        auth_pass.send_keys(passwd)
        auth_btn = browser.find_element_by_css_selector(".btn-login")
        auth_btn.click()
        continue
    try:
        video = browser.find_element_by_css_selector("button.vjs-big-play-button")
        video.click()
        sleep(15)
    except:
        video = False
    try:
        #escolha = browser.find_element(By.XPATH, "//li[contains(@data-correct, 'true')]")
        #escolha = browser.find_elements_by_css_selector('li[data-correct="true"]')
        #for x in range(0,len(escolha)):
        #    escolha[x].click()
        #escolha = browser.findElements(By.className('li[data-correct="true"]'))
        for block in content_blocks:
            elements = block.find_elements_by_tag_name("a")
            for el in elements:
                a_elements.append(el)

    except:
        escolha = browser.find_element_by_css_selector('li[data-correct="true"]')
        escolha = False
    
    break
    button.click()
    