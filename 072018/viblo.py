import time
import csv
from selenium import webdriver


def validate_with_username_and_not_password(browser):
    """
    Function validate form login khi có username nhưng không có password
    :param browser:
    :return:
    """
    try:
        username = browser.find_elements_by_name("username")
        if not username:
            print("Case 1 fail")
            return False
        username = username[0]
        username.clear()
        username.send_keys("ntvan")

        password = browser.find_elements_by_name("password")
        if not password:
            print("Case 1 fail")
        password = password[0]
        password.clear()

        time.sleep(1)  # sleep 1s

        login_button_elm = browser.find_elements_by_xpath("//div[@class='login-form']/button")
        login_button_elm[0].click()
        if 'Password is required' in browser.page_source:
            print("Case 1 pass")
            return True
        else:
            print("Case 1 fail")
            return False

    except Exception as e:
        print(e)


def validate_with_password_and_not_username(browser):
    """
    Function validate form login khi có password nhưng không có username
    :param browser:
    :return:
    """
    try:
        username = browser.find_elements_by_name("username")
        if not username:
            print("Case 2 fail")
            return False
        username = username[0]
        username.clear()

        password = browser.find_elements_by_name("password")
        if not password:
            print("Case 2 fail")
            return False
        password = password[0]
        password.clear()
        password.send_keys("abcd1234")

        time.sleep(1)  # sleep 1s

        login_button_elm = browser.find_elements_by_xpath("//div[@class='login-form']/button")
        login_button_elm[0].click()
        if 'Username or Email is required' in browser.page_source:
            print("Case 2 pass")
            return True
        else:
            print("Case 2 fail")
            return False

    except Exception as e:
        print(e)


def validate_with_username_incorrect_and_password_correct(browser):
    """
    Function validate form login khi có username sai nhưng password đúng
    :param browser:
    :return:
    """
    try:
        username = browser.find_elements_by_name("username")
        username = username[0]
        username.clear()
        username.send_keys("hoangminh")

        password = browser.find_elements_by_name("password")
        password = password[0]
        password.clear()
        password.send_keys("abcd1234")

        time.sleep(5)  # sleep 1s
        login_button_elm = browser.find_elements_by_xpath("//div[@class='login-form']/button")
        login_button_elm[0].click()
        time.sleep(10)
        if 'The user credentials were incorrect.' in browser.page_source:
            print("Case 3 pass")
            return True
        else:
            print("Case 3 fail")
            return False
    except:
        pass



def validate_with_username_correct_and_password_incorrect(browser):
    """
    Function validate form login khi có username đúng nhưng password sai
    :param browser:
    :return:
    """
    try:
        username = browser.find_elements_by_name("username")
        if not username:
            print("Case 4 fail")
            return False
        username = username[0]
        username.clear()
        username.send_keys("ntvan")

        time.sleep(5)
        password = browser.find_elements_by_name("password")
        if not password:
            print("Case 4 fail")
            return False
        password = password[0]
        password.clear()
        password.send_keys("abcd1234")

        time.sleep(1)  # sleep 1s

        login_button_elm = browser.find_elements_by_xpath("//div[@class='login-form']/button")
        login_button_elm[0].click()
        time.sleep(10)
        if 'The user credentials were incorrect.' in browser.page_source:
            print("Case 4 pass")
            return True
        else:
            print("Case 4 fail")
            return False

    except Exception as e:
        print(e)


def validate_with_username_html_and_password_correct(browser):
    """
    Function validate form login khi có username đúng nhưng password sai
    :param browser:
    :return:
    """
    try:
        username = browser.find_elements_by_name("username")
        if not username:
            print("Case 5 fail")
            return False
        username = username[0]
        username.clear()
        username.send_keys("<u>ntvan</u>")

        password = browser.find_elements_by_name("password")
        if not password:
            print("Case 5 fail")
            return False
        password = password[0]
        password.clear()
        password.send_keys("abcd1234")

        time.sleep(1)  # sleep 1s

        login_button_elm = browser.find_elements_by_xpath("//div[@class='login-form']/button")
        login_button_elm[0].click()
        time.sleep(10)
        if 'The user credentials were incorrect.' in browser.page_source:
            print("Case 5 pass")
            return True
        else:
            print("Case 5 fail")
            return False

    except Exception as e:
        print(e)


def validate_with_username_overlong_and_password_correct(browser):
    """
    Function validate form login khi có username đúng nhưng password sai
    :param browser:
    :return:
    """
    try:
        username = browser.find_elements_by_name("username")
        if not username:
            print("Case 6 fail")
            return False
        username = username[0]
        username.clear()
        long_text = 256 * "ntvan"
        username.send_keys(long_text)

        password = browser.find_elements_by_name("password")
        if not password:
            print("Case 6 fail")
            return False
        password = password[0]
        password.clear()
        password.send_keys("abcd1234")

        time.sleep(1)  # sleep 1s

        login_button_elm = browser.find_elements_by_xpath("//div[@class='login-form']/button")
        login_button_elm[0].click()
        time.sleep(10)
        if 'The user credentials were incorrect.' in browser.page_source:
            print("Case 6 pass")
            return True
        else:
            print("Case 6 fail")
            return False

    except Exception as e:
        print(e)


def validate_with_username_correct_and_password_less(browser):
    """
    Function validate form login khi có username đúng nhưng password sai
    :param browser:
    :return:
    """
    try:
        username = browser.find_elements_by_name("username")
        if not username:
            print("Case 7 fail")
            return False
        username = username[0]
        username.clear()
        username.send_keys("ntvan")

        password = browser.find_elements_by_name("password")
        if not password:
            print("Case 7 fail")
            return False
        password = password[0]
        password.clear()
        password.send_keys("H")

        time.sleep(1)  # sleep 1s

        login_button_elm = browser.find_elements_by_xpath("//div[@class='login-form']/button")
        login_button_elm[0].click()
        time.sleep(10)
        if 'The user credentials were incorrect.' in browser.page_source:
            print("Case 7 pass")
            return True
        else:
            print("Case 7 fail")
            return False

    except Exception as e:
        print(e)


def validate_with_username_less_and_password_correct(browser):
    """
    Function validate form login khi có username đúng nhưng password sai
    :param browser:
    :return:
    """
    try:
        username = browser.find_elements_by_name("username")
        if not username:
            print("Case 8 fail")
            return False
        username = username[0]
        username.clear()
        username.send_keys("m")

        password = browser.find_elements_by_name("password")
        if not password:
            print("Case 8 fail")
            return False
        password = password[0]
        password.clear()
        password.send_keys("abcd1234")

        time.sleep(1)  # sleep 1s

        login_button_elm = browser.find_elements_by_xpath("//div[@class='login-form']/button")
        login_button_elm[0].click()
        time.sleep(10)
        if 'The user credentials were incorrect.' in browser.page_source:
            print("Case 8 pass")
            return True
        else:
            print("Case 8 fail")
            return False

    except Exception as e:
        print(e)


def validate_with_username_correct_and_password_correct(browser):
    """
    Function validate form login khi có username đúng nhưng password đúng
    :param browser:
    :return:
    """
    try:
        username = browser.find_elements_by_name("username")
        if not username:
            print("Case 9 fail")
            return False
        username = username[0]
        username.clear()
        username.send_keys("ntvan")

        password = browser.find_elements_by_name("password")
        if not password:
            print("Case 9 fail")
            return False
        password = password[0]
        password.clear()
        password.send_keys("abcd1234")

        time.sleep(1)  # sleep 1s

        login_button_elm = browser.find_elements_by_xpath("//div[@class='login-form']/button")
        login_button_elm[0].click()
        time.sleep(10)
        if 'Logout' in browser.page_source:
            print("Case 9 pass")
            return True
        else:
            print("Case 9 fail")
            return False

    except Exception as e:
        print(e)


def click_button(browser):
    browser.refresh()
    login = browser.find_element_by_xpath(
        "//div[@class='main-navbar__right']/div[@class='main-navbar__group'][2]/button[@class='el-button el-button--text']")
    login.click()

    time.sleep(5)
    return browser

if __name__ == '__main__':
    browser = webdriver.Chrome(executable_path="./chromedriver")
    browser.get("https://viblo.asia/")
    time.sleep(5)

    results = [["STT", "Checklist", u"Kết quả mong muốn"]]

    browser = click_button(browser)
    case_1 = validate_with_username_and_not_password(browser)
    results.append(["Case 1", u"validate_with_username_and_not_password", "Pass" if case_1 else "Fail"])

    browser = click_button(browser)
    case_2 = validate_with_password_and_not_username(browser)
    results.append(["Case 2", "validate_with_password_and_not_username", "Pass" if case_2 else "Fail"])

    browser = click_button(browser)
    case_3 = validate_with_username_incorrect_and_password_correct(browser)
    results.append(["Case 3", "validate_with_username_incorrect_and_password_correct", "Pass" if case_3 else "Fail"])

    browser = click_button(browser)
    case_4 = validate_with_username_correct_and_password_incorrect(browser)
    results.append(["Case 4", "validate_with_username_correct_and_password_incorrect", "Pass" if case_4 else "Fail"])

    browser = click_button(browser)
    case_5 = validate_with_username_html_and_password_correct(browser)
    results.append(["Case 5", "validate_with_username_html_and_password_correct", "Pass" if case_5 else "Fail"])

    browser = click_button(browser)
    case_6 = validate_with_username_overlong_and_password_correct(browser)
    results.append(["Case 6", "validate_with_username_overlong_and_password_correct", "Pass" if case_6 else "Fail"])

    browser = click_button(browser)
    case_7 = validate_with_username_correct_and_password_less(browser)
    results.append(["Case 7", "validate_with_username_correct_and_password_less", "Pass" if case_7 else "Fail"])

    browser = click_button(browser)
    case_8 = validate_with_username_less_and_password_correct(browser)
    results.append(["Case 8", "validate_with_username_less_and_password_correct", "Pass" if case_8 else "Fail"])

    browser = click_button(browser)
    case_9 = validate_with_username_correct_and_password_correct(browser)
    results.append(["Case 9", "validate_with_username_correct_and_password_correct", "Pass" if case_9 else "Fail"])

    myFile = open('result.csv', 'w')
    writer = csv.writer(myFile)
    writer.writerows(results)

    browser.close()
