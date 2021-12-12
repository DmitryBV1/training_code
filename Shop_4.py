from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

#4. Откройте книгу "Android Quick Start Guide"
android_quick_book = driver.find_element_by_css_selector('a[href="http://practice.automationtesting.in/product/android-quick-start-guide/"]').click()

#5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
old_price = driver.find_element_by_css_selector(".price del")
old_price_get_text = old_price.text
assert '600' in old_price_get_text

#6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
new_price = driver.find_element_by_css_selector(".price ins")
new_price_get_text = new_price.text
assert '450' in new_price_get_text

#7. Добавьте явное ожидание и нажмите на обложку книги
#• Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
android_book = WebDriverWait(driver, 10).until(
   EC.element_to_be_clickable((By.CSS_SELECTOR, 'a img[alt="Android Quick Start Guide"]')))
android_book.click()

#8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
android_book_close = WebDriverWait(driver,10).until(
   EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close')))
android_book_close.click()

driver.quit()
