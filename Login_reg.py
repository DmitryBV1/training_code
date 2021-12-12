import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

#1 Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

#2. Нажмите на вкладку "My Account Menu"
my_account = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/my-account/']").click()

#3. В разделе "Register", введите email для регистрации
reg_email = driver.find_element_by_id("reg_email")
reg_email.send_keys("testing_667@gmail.com")

#4. В разделе "Register", введите пароль для регистрации
reg_pass = driver.find_element_by_id("reg_password")
reg_pass.send_keys("abt389950103")

#Ждем появление плашки о надежности пароля
strong_pass = WebDriverWait (driver, 20).until(
   EC.presence_of_element_located((By.CSS_SELECTOR, '.woocommerce-password-strength.strong')))
strong_pass.click()

#5. Нажмите на кнопку "Register"
time.sleep(3)
reg_btn = driver.find_element_by_css_selector(".woocomerce-FormRow.form-row .woocommerce-Button.button").click()

driver.quit()