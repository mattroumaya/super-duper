#!/usr/bin/env python
# coding: utf-8

#%%

import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import camelot
import ghostscript
import os
import string
from camelot.handlers import PDFHandler
import shutil
from webdriver_manager.chrome import ChromeDriverManager


#%%
# Set up options so PDFs download automatically

chrome_options = Options()

download_dir = "C:\\Matt\Python\ACGME\pdfs"

chrome_options.add_experimental_option('prefs',  {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
    }
)

b = webdriver.Chrome("C:\Matt\Python\chromedriver\chromedriver.exe", options = chrome_options)

b.get('https://apps.acgme.org/ads/Public/Reports/Report/1')

inputs = Select(b.find_element_by_css_selector('#SpecialtyCode'))

input1 = len(inputs.options)


options = inputs.options


#%%
# This is the fun part where ~165 pdfs get automatically downloaded

names = []
for items in range(input1):
     inputs.select_by_index(items)
     button = b.find_element_by_id('btnView')
     button.click()

