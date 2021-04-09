from typing import Iterable, List

from decouple import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def _wait_for_elements(driver: WebDriver, locators: Iterable[tuple[str, str]]) -> None:
    """
    Wait for given certain elements to load
    :param driver: WebDriver object in which we're conducting test
    :param locators: Tuple of all the elements to be located, each being a tuple with (By.XX, element_identifier)
    """
    for locator in locators:
        element_present = expected_conditions.presence_of_element_located(locator)
        WebDriverWait(driver, 6.9).until(element_present)


def run_github_login(email: str, password: str) -> str:
    """
    Login to github and return username displayed
    :param email: email to be used for login
    :param password: password to be used for login
    :return: Username displayed
    """
    options = Options()
    options.headless = config("ass1_headless", cast=bool, default=False)
    driver = webdriver.Firefox(options=options)

    try:
        # go to github homepage
        driver.get("https://github.com/")

        # define link text for Sign in
        sign_in_link_text = "Sign in"

        # wait for the sign in link to load and then click on it
        _wait_for_elements(driver=driver, locators=((By.LINK_TEXT, sign_in_link_text),))
        driver.find_element_by_link_text(sign_in_link_text).click()

        # define IDs for email and password input fields and CSS Class for button field
        email_input_id = "login_field"
        password_input_id = "password"
        submit_button_class_name = "btn"

        # wait for all 3 elements to load and then login
        _wait_for_elements(
            driver=driver,
            locators=((By.ID, email_input_id), (By.ID, password_input_id), (By.CLASS_NAME, submit_button_class_name)),
        )
        driver.find_element_by_id(email_input_id).send_keys(email)
        driver.find_element_by_id(password_input_id).send_keys(password)
        driver.find_element_by_class_name(submit_button_class_name).click()

        # define xpath for username
        username_xpath = "/html/body/div[4]/div/aside[1]/div[2]/div[1]/details/summary/span[1]"

        # wait for username to load and then return username
        _wait_for_elements(driver=driver, locators=((By.XPATH, username_xpath),))
        username = driver.find_element_by_xpath(username_xpath).text

        # close WebDriver and return username
        driver.close()
        return username

    except Exception as e:
        driver.close()
        raise e


def run_google_scholar(query: str) -> List[str]:
    """
    Get 5 articles from Google Scholar that are published after 2020
    :param query: Query string to be searched to get list of
    :return: links to articles
    """
    options = Options()
    options.headless = config("ass1_headless", cast=bool, default=False)
    driver = webdriver.Firefox(options=options)

    try:
        # go to google scholars
        driver.get("https://scholar.google.com/")

        # define IDs for query input and search button
        query_input_id = "gs_hdr_tsi"
        search_button_id = "gs_hdr_tsb"

        # wait for query input and search button to load, then enter query and search
        _wait_for_elements(driver=driver, locators=((By.ID, query_input_id), (By.ID, search_button_id)))
        driver.find_element_by_id(query_input_id).send_keys(query)
        driver.find_element_by_id(search_button_id).click()

        # define link text for link to articles since 2020
        since_2020_link_text = "Since 2020"

        # wait for link to load and click on it
        _wait_for_elements(driver=driver, locators=((By.LINK_TEXT, since_2020_link_text),))
        driver.find_element_by_link_text(since_2020_link_text).click()

        # define class name for divs showing an article and xpath to anchor tag with article link from the article div as root
        article_div_class = "gs_ri"
        article_anchor_tag_xpath = "h3/a"

        # wait for divs to load
        _wait_for_elements(driver=driver, locators=((By.CLASS_NAME, article_div_class),))
        article_divs = driver.find_elements_by_class_name(article_div_class)

        # iterate through the first 5 article divs and get links
        links = []
        for article_div in article_divs[:5]:
            links.append(article_div.find_element_by_xpath(article_anchor_tag_xpath).get_property("href"))

        driver.close()
        return links
    except Exception as e:
        driver.close()
        raise e
