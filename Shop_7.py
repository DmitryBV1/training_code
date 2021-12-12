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

#3. Добавьте в корзину книги "HTML5 WebApp Development"
driver.execute_script("window.scrollBy(0, 300);")
HTML5_book = driver.find_element_by_css_selector('a[href="/shop/?add-to-cart=182"]').click()

#4. Перейдите в корзину
basket = driver.find_element_by_css_selector('a[href="http://practice.automationtesting.in/basket/"]').click()

#5. Нажмите "PROCEED TO CHECKOUT"
wait = WebDriverWait(driver, 20)
checkout_EC = wait.until(
   EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="http://practice.automationtesting.in/checkout/"]'))).click()

#6. Заполните все обязательные поля
#• Перед заполнением first name, добавьте явное ожидание
#• Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
#• Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
first_name_EC = wait.until(EC.element_to_be_clickable((By.ID, 'billing_first_name')))

first_name = driver.find_element_by_id('billing_first_name')
first_name.send_keys('John')

last_name = driver.find_element_by_id('billing_last_name')
last_name.send_keys('Smith')

email = driver.find_element_by_id('billing_email')
email.send_keys('test@test.com')

phone = driver.find_element_by_id('billing_phone')
phone.send_keys('1111111111')

country = driver.find_element_by_id('s2id_billing_country').click()
input_country = driver.find_element_by_id('s2id_autogen1_search')
input_country.send_keys('Sweden')
vote_country = driver.find_element_by_id('select2-results-1').click()

adress = driver.find_element_by_id('billing_address_1')
adress.send_keys('Lenina street')

pastcode = driver.find_element_by_id('billing_postcode')
pastcode.send_keys('111222')

city = driver.find_element_by_id('billing_city')
city.send_keys('Stockholm')

#7. Выберите способ оплаты "Check Payments"
#• Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
check_payments = driver.find_element_by_id('payment_method_cheque').click()

#8. Нажмите PLACE ORDER
place_order = driver.find_element_by_id('place_order').click()

#9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
thank_you = wait.until(
   EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce-thankyou-order-received'), 'Thank you. Your order has been received.'))
print('Текст "Thank you. Your order has been received." отоброжается? -', thank_you)

#10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
text_check_payments = wait.until(
   EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.shop_table.order_details > tfoot > tr:nth-child(3) > td'), 'Check Payments'))
print('Текст "Check Payments" отобразился? -', text_check_payments)

driver.quit()

