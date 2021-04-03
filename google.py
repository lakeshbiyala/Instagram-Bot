from selenium import webdriver

import time

browser = webdriver.Chrome()

url = "https://google.com"

browser.get(url)
time.sleep(1)
"""
<input class="gLFyf gsfi" name="q" type="text">
"""
name = 'q'
search_el = browser.find_element_by_name(name)
print(search_el)

search_el.send_keys("eminem")

"""
<input class="gNO89b" name="btnK" type="submit" >
"""
submit_btn_el = browser.find_element_by_css_selector("input[type='submit']")
print(submit_btn_el.get_attribute('name'))
time.sleep(2)
submit_btn_el.click()
