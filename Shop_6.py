import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

#1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

#2. Нажмите на вкладку "Shop"
shop = driver.find_element_by_id('menu-item-40').click()

#3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
#• Перед добавлением первой книги, проскролльте вниз на 300 пикселей
#• После добавления 1-й книги добавьте sleep
driver.execute_script("window.scrollBy(0, 300);")
HTML5_book = driver.find_element_by_css_selector('a[href="/shop/?add-to-cart=182"]').click()
time.sleep(5)
driver.execute_script("window.scrollBy(0, 100);")
JS_Data_book = driver.find_element_by_css_selector('a[href="/shop/?add-to-cart=180"]').click()

#4. Перейдите в корзину
basket = driver.find_element_by_css_selector('a[href="http://practice.automationtesting.in/basket/"]').click()
time.sleep(4)

#5. Удалите первую книгу
del_first_book = driver.find_element_by_css_selector('tbody > tr.cart_item:nth-child(1) > .product-remove > a').click()

#6. Нажмите на Undo (отмена удаления)
undo = driver.find_element_by_partial_link_text('Undo').click()

#7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
#• Предварительно очистите поле с помощью локатор_поля.clear()
clear = driver.find_element_by_css_selector('tbody > tr:nth-child(2) .quantity > input').clear()
time.sleep(3)
books_3 = driver.find_element_by_css_selector('tbody > tr:nth-child(2) .quantity > input')
books_3.send_keys(3)

#8. Нажмите на кнопку "UPDATE BASKET"
update_basket = driver.find_element_by_css_selector('input[name="update_cart"]').click()
time.sleep(3)

#9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
value_from_JS = driver.find_element_by_css_selector('tbody > tr:nth-child(2) .quantity input')
value_from_JS.get_attribute('value') #что-то у меня не получилось через assert решить :(
if value_from_JS.get_attribute('value') == '3':
   print('В корзине 3 книги "JS Data Structures and Algorithm"')
else:
   print('Ошибка! В корзине НЕ три книги "JS Data Structures and Algorithm"')

#10. Нажмите на кнопку "APPLY COUPON"
time.sleep(3)
apply_coupon = driver.find_element_by_css_selector('input[name="apply_coupon"]').click()

#11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
text_error = WebDriverWait(driver, 10).until(
   EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-error'), "Please enter a coupon code."))
print("Сообщение возникло? -", text_error)
time.sleep(5)
driver.quit()
