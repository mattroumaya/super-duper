#!/usr/bin/env python
# coding: utf-8

#%%
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
#%%



# ! ! ! ! ! ! ! ! 
# ! update these parameters !

# same as setwd() in R - location where pdfs will be saved
download_dir = "C:\\me\path\something\pdfs"

# the location of your chromedriver .exe file
path_to_chromedriver = "C:\me\path\chromedriver\chromedriver.exe"


# ! ! ! ! ! ! ! ! 




# set up options so pdfs download automatically
# this sets options in chrome so that pdfs are automatically downloaded without 
# prompting user to click a "download" button
chrome_options = Options()
chrome_options.add_experimental_option('prefs',  {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
    }
)

# this script requires chromedriver to be downloaded
# NOTE chromedriver is regularly updated to keep up with Chrome updates
# so you may need to update your version of chromedriver often
# NOTE it is also important that the version of chromedriver matches the version of
# Chrome that you are using.
# to download: https://chromedriver.chromium.org/downloads
b = webdriver.Chrome(path_to_chromedriver, options = chrome_options)

# this opens the web page
b.get('https://apps.acgme.org/ads/Public/Reports/Report/1')

# this searches the css for #SpecialtyCode, which will map to every drop-down element
inputs = Select(b.find_element_by_css_selector('#SpecialtyCode'))
input1 = len(inputs.options)
options = inputs.options


#%%

# this is the fun part where ~165 pdfs get automatically downloaded
names = []
for items in range(input1):
     inputs.select_by_index(items)
     button = b.find_element_by_id('btnView')
     button.click()

