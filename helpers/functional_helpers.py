from selenium.webdriver.common.by import By

def login_funk(driver, user_login, user_pass):
    """
    Compare text to be found and which we accept
    :param driver: webdriver instance
    :param user_login: information to login :login id
    :param user_pass: information to login : password
    :return : none
    """
    find_form_log = driver.find_element(By.XPATH, '//*[@id="login-form"]//*[@class="form-control"]')
    find_form_log.send_keys(user_login)

    find_form_pass = driver.find_element(By.XPATH, '//*[@id="login-form"]//*[@name="password"]')
    find_form_pass.send_keys(user_pass)

    find_button_signin = driver.find_element(By.XPATH, '//*[@id="submit-login"]')
    find_button_signin.click()