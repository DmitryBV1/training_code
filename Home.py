from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

#1 Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

#2 Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")

#3 Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
selenium_ruby_book = driver.find_element_by_css_selector('.attachment-shop_catalog.size-shop_catalog.wp-post-image').click()

#4 Нажмите на вкладку "REVIEWS"
reviews_click = driver.find_element_by_css_selector(".reviews_tab").click()

#5 Поставьте 5 звёзд
driver.execute_script("window.scrollBy(0, 700);")
star_5 = driver.find_element_by_class_name("star-5").click()

#6 Заполните поле "Review" сообщением: "Nice book!"
comment = driver.find_element_by_css_selector(".comment-form-comment #comment")
comment.send_keys("Nice book!")

#7 Заполните поле "Name"
name = driver.find_element_by_id("author")
name.send_keys("John")

#8 Заполните "Email"
email = driver.find_element_by_id("email")
email.send_keys("testing@gmail.com")

#9 Нажмите на кнопку "SUBMIT"
submit = driver.find_element_by_id("submit").click()

driver.quit()
