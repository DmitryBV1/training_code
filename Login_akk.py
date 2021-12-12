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

#3. В разделе "Login", введите email для логина
log_email = driver.find_element_by_id("username")
log_email.send_keys("testing_667@gmail.com")

#4. В разделе "Login", введите пароль для логина
log_pass = driver.find_element_by_id("password")
log_pass.send_keys("abt389950103")

#5. Нажмите на кнопку "Login"
login_btn = driver.find_element_by_css_selector("input[name=login]").click()

#6. Добавьте проверку, что на странице есть элемент "Logout"
logout_element = WebDriverWait (driver,10).until(
   EC.visibility_of_element_located((By.LINK_TEXT, "Logout")))
if logout_element is not None:
   print('Элемент "Logout" присутствует на странице')
else:
   print('Элемент "Logout" отсутствует на странице')

driver.quit()