from selenium import webdriver
from conf import INSTA_USERNAME, INSTA_PASSWORD
import time

browser = webdriver.Chrome()

url = "https://instagram.com"

browser.get(url)
time.sleep(2)

username_el = browser.find_element_by_name("username")
password_el = browser.find_element_by_name("password")
submit_btn_el = browser.find_element_by_css_selector("button[type='submit']")

username_el.send_keys(INSTA_USERNAME)
password_el.send_keys(INSTA_PASSWORD)
submit_btn_el.click()
time.sleep(2)

body_el = browser.find_element_by_css_selector("body")
html_text = body_el.get_attribute("innerHTML")
# print(html_text)

"""
<button class="_5f5mN       jIbKX  _6VtSN     yZn4P   ">Follow</button>
"""

#xpath :eg.
# my_btn_xpath = "//button"
# my_btn_el = browser.find_element_by_xpathr(my_button_xpath)

def automate_follow(browser):
    # my_follow_btn_xpath = "//button[contains(text(), 'Follow')][not (contains(text(), 'Following))]" #(xpath helps to chain such condiitons)
    # my_follow_btn_xpath = "//a[contains(text(), 'Follow')][not (contains(text(), 'Following))]"

    follow_btn_xpath = "//*[contains(text(), 'Follow')][not (contains(text(), 'Following'))][not (contains(text(), 'Followers'))]"
    follow_btn_elements = browser.find_elements_by_xpath(follow_btn_xpath)

    for btn in follow_btn_elements:
        time.sleep(2) #self-throttle
        try:
            btn.click()
        except:
            pass

time.sleep(2)
account_url = "https://www.instagram.com/shakira/"      #Shakira's Instagram account
browser.get(account_url)

post_url_pattern = "https://www.instagram.com/p/<post-slug-id>"

post_xpath_str = "//a[contains(@href, '/p/')]"
post_links = browser.find_elements_by_xpath(post_xpath_str)

post_link_el = None
if len(post_links)>0:
    post_link_el =  post_links[0]

if post_link_el != None:
    post_href = post_link_el.get_attribute("href")
    browser.get(post_href)


def automated_comment(browser, content="Awesome post!!"):
    time.sleep(2)
    """
    <textarea placeholder="Add a comment…" ></textarea>
    """
    comment_xpath_str = "//textarea[contains(@placeholder, 'Add a comment…')]"
    comment_el = browser.find_element_by_xpath(comment_xpath_str)
    comment_el.send_keys(content)

    submit_btns_xpath = "button[type='submit']"
    submit_btns_els = browser.find_elements_by_css_selector(submit_btns_xpath)
    time.sleep(2)
    for btn in submit_btns_els:
        try:
            btn.click()
        except:
            pass



def automate_like(browser):
    """
    <svg aria-label="Like" ></svg>
    """
    like_heart_svg_xpath = "//*[contains(@aria-label, 'Like')]"
    all_like_heart_els = browser.find_elements_by_xpath(like_heart_svg_xpath)

    #biggest sized heart represent like for post. we want that. 
    max_heart = -1
    for heart_el in all_like_heart_els:
        h = heart_el.get_attribute("height")
        current_h = int(h)
        if current_h > max_heart:
            max_heart = current_h

    all_like_heart_els = browser.find_elements_by_xpath(like_heart_svg_xpath)
    for heart_el in all_like_heart_els:
        h = heart_el.get_attribute("height")
        if h == max_heart or h == f"{max_heart}":
            parent_button = heart_el.find_element_by_xpath('..') # '..' takes us up one level i.e to parent btn level
            time.sleep(2)
            try:
                parent_button.click()
            except:
                pass    



# automate_follow(browser)
# automate_like(browser)
# automated_comment(browser, "Awesome post!!")


