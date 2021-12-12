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

#4. Откройте книгу "HTML 5 Forms"
book_html_5_forms = driver.find_element_by_css_selector('a[href="http://practice.automationtesting.in/product/html5-forms/"]').click()

#5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
name_book = driver.find_element_by_css_selector('h1[itemprop="name"]')
name_book_get_text = name_book.text
assert name_book_get_text == 'HTML5 Forms'

driver.quit()
