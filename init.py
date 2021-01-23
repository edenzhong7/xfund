from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
import csv
import json
from lxml import etree,html
import pymongo


def get_html(url):
    browser = webdriver.Chrome()
    browser.get(url)
    html = browser.page_source
    return html


def get_mongo_collection(name):
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.ddfund
    collection = getattr(db, name)
    return collection