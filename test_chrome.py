import time

import pytest
from selenium.webdriver.common.by import By

base_url="https://www.linkedin.com/"

@pytest.mark.parametrize(("login", "password"),
                         [
                             ("Alexandr85@mail.ru","874102145"),#everything should be fine
                             ("Vladim","2019")#it should say that there are not enough characters,or something like that
                         ])

@pytest.mark.linkedin
def test_linkedin_reg(browser, login, password):
    browser.get(base_url)
    browser.find_element(By.CSS_SELECTOR, "[action-type='ACCEPT']").click()
    #cookie
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, ".btn-md.btn-tertiary.nav__button-tertiary").click()
    #Join button
    time.sleep(3)
    browser.find_element(By.ID, "email-address").send_keys(login)
    browser.find_element(By.ID, "password").send_keys(password)
    #Registration field
    browser.find_element(By.CLASS_NAME, "join-form__form-body-submit-button").click()
    #Join button
