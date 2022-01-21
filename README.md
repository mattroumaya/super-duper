# super-duper

1. Find which version of Chrome you are using. In your Chrome browser, click on the three dots at the top-right, and then **Help**, and **About Google Chrome**
2. Install [ChromeDriver](https://chromedriver.chromium.org/downloads). Make sure to download the version that is compatible with your current version of Chrome.
3. Run the python script `get data.py`. Make sure to update paths to your directory, and Chrome version if needed.
4. Once all of the pdfs are saved to a folder, it will be helpful to rename the pdfs as the name of the medical specialty (located at the top of each pdf). The R script that will parse the pdf data is written so that it will create a `specialty` column, so you can filter/sample from the file if needed. This can probably be automated somehow! 
5. Run the R script `rpd scraper.r`. Additional cleaning might be needed, but this will hopefully produce a file that is mostly useful.
