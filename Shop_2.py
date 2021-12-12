import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

#1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

#2. Залогиньтесь
my_account = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/my-account/']").click()
log_email = driver.find_element_by_id("username")
log_email.send_keys("testing_667@gmail.com")
log_pass = driver.find_element_by_id("password")
log_pass.send_keys("abt389950103")
login_btn = driver.find_element_by_css_selector("input[name=login]").click()

#3. Нажмите на вкладку "Shop"
shop = driver.find_element_by_id('menu-item-40').click()

#4. Откройте категорию "HTML"
html_link = driver.find_element_by_css_selector('a[href="http://practice.automationtesting.in/product-category/html/"]').click()

#5. Добавьте тест, что отображается три товара
books_on_the_page = driver.find_elements_by_css_selector('.woocommerce-LoopProduct-link')
if len(books_on_the_page) == 3:
   print('На странице 3 книги')
else:
   print('Ошибка. На странице', str(len(books_on_the_page)))
driver.quit()
