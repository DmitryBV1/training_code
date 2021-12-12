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

#3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
book_in_the_cart = driver.find_element_by_css_selector('a[href="/shop/?add-to-cart=182"]').click()
time.sleep(5)

#4. Добавьте тест, что в возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
#• Используйте для проверки assert
item_assert = driver.find_element_by_class_name('cartcontents')
item_assert_get_text = item_assert.text
assert item_assert_get_text == '1 Item'
price_in_the_cart = driver.find_element_by_css_selector('#wpmenucartli .amount')
price_in_the_cart_get_text = price_in_the_cart.text
assert '180' in price_in_the_cart_get_text

#5. Перейдите в корзину
basket = driver.find_element_by_css_selector('a[href="http://practice.automationtesting.in/basket/"]').click()

#6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
price_in_the_subtotal = WebDriverWait(driver,10).until(
   EC.visibility_of_element_located((By.CSS_SELECTOR, '.cart-subtotal .woocommerce-Price-amount.amount')))

#7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
price_in_the_total = WebDriverWait(driver,10).until(
   EC.visibility_of_element_located((By.CSS_SELECTOR, '.order-total .woocommerce-Price-amount.amount')))
driver.quit()
