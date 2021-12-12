from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
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

#4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
#• Используйте проверку по value
default_value = driver.find_element_by_css_selector('option[value="menu_order"]')
default_value_get_text = default_value.text
assert default_value_get_text == 'Default sorting'

#5. Отсортируйте товары от большего к меньшему
#• в селекторах используйте класс Select
hight_to_low = driver.find_element_by_class_name('orderby')
select = Select(hight_to_low)
select.select_by_value('price-desc')

#7. Добавьте тест, что в селекторе выбран вариант сортировки от большего к меньшему
#• Используйте проверку по value
sort_hight_to_low = driver.find_element_by_css_selector('option[value="price-desc"]')
sort_hight_to_low_get_text = sort_hight_to_low.text
assert sort_hight_to_low_get_text == 'Sort by price: high to low'

driver.quit()