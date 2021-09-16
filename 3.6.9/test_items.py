from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_button_add_to_basket(browser):
    browser.get(link)
    btn_add = "btn.btn-lg.btn-primary.btn-add-to-basket"
    found_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, btn_add))
    )
    assert found_button != False, 'Do not found the button of add to basket'