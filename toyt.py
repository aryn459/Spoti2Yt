from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH = r'C:/Users/User/chromedriver/chromedriver.exe'
BRAVE_PATH = r'	C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'  # Change if different

options = Options()
options.binary_location = BRAVE_PATH

USER_DATA_DIR = r'C:\Users\User\AppData\Local\BraveSoftware\Brave-Browser\User Data'
PROFILE_NAME = 'Profile 5'
options.add_argument(f'--user-data-dir={USER_DATA_DIR}')
options.add_argument(f'--profile-directory={PROFILE_NAME}')

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://music.youtube.com/")
