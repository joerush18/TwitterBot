from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(driver_location)

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(5)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(4)

    def search(self, search_item):
        bot = self.bot
        search = bot.find_element_by_class_name("r-30o5oe")
        search.send_keys(search_item)
        search.send_keys(Keys.RETURN)
        time.sleep(4)

driver_location = input("Enter Driver's Location: ")
user_name = input("Enter username: ")
user_password = input("Enter Password: ")
search_text = input('Enter #(text) only to search: ')
auto_twitter = TwitterBot(user_name, user_password)
auto_twitter.login()
auto_twitter.search(search_text)
