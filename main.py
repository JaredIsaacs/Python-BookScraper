import sys
import pdfkit

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

STDOUT = sys.stdout

if __name__ == '__main__':

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.wuxiaworld.com/novel/warlock-of-the-magus-world/wmw-chapter-1")
    book_title = driver.find_element(by=By.CLASS_NAME, value="ww-1lzehbp")
    book_content = driver.find_element(by=By.CLASS_NAME, value="ww-80ezzz")
    test = book_content.get_attribute('innerHTML')

    with open(book_title.text + ".txt", mode="w", encoding="utf-8") as f:
        sys.stdout = f
        print(book_content.text)
        sys.stdout = STDOUT

    pdfkit.from_string('<meta http-equiv="Content-type" content="text/html; charset=utf-8" />' + test, 'out.pdf')

    driver.close()
    print(test)





