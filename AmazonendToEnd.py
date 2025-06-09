import time
from selenium import webdriver

from selenium.webdriver import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.implicitly_wait(5)

driver.get('https://www.amazon.in/')
driver.maximize_window()

action = ActionChains(driver)

# Hover over 'Sign in'
action.move_to_element(driver.find_element('xpath','(//a[@data-nav-role="signin"])[1]')).perform()
action.context_click(driver.find_element('xpath', '//span[@class="nav-action-inner"]')).click().perform()

# Sign in
driver.find_element('xpath', '//input[@name="email"]').send_keys('Khanshahida96@gmail.com')
driver.find_element('xpath', '(//span[@class="a-button-inner"])[2]').click()
driver.find_element('xpath', '//input[@id="ap_password"]').send_keys('343@Engineer')
driver.find_element('xpath', '(//span[@class="a-button-inner"])[1]').click()

# Search and click book
driver.find_element('xpath', '//input[@id="twotabsearchtextbox"]').send_keys("Mindset book")
driver.find_element('xpath','//div[@id="sac-suggestion-row-1"]').click()

# driver.find_element('xpath', '(//span[contains(text(),"MINDSET book for solo Readers")])[1]').click()
driver.find_element('xpath', '//span[text()="MINDSET (REVISED AND UPDATED) [Paperback] Dweck, Carol"]').click()

# Switch to new tab
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])

# Add to cart and checkout
driver.find_element('xpath', '//input[@id="add-to-cart-button"]').click()
driver.find_element('xpath', '//span[@id="nav-cart-count"]').click()
driver.find_element('xpath', '//input[@name="proceedToRetailCheckout"]').click()
time.sleep(2)

# Close current tab
driver.close()
