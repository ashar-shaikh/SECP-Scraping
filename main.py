from flask import Flask
from selenium import webdriver
import os

app = Flask(__name__)

@app.route('/')
def app():
   chrome_options = webdriver.ChromeOptions()
   chrome_options.add_argument("--headless")
   chrome_options.add_argument("--disable-dev-shm-usage")
   chrome_options.add_argument("--no-sandbox")
   chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

   driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
   driver.get("https://medium.com")
   print("Finished!")
   driver.quit()
   return '<h1>Hello World</h1>'