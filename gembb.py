from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from myclass import TennisOBJ
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

URL = "https://368gem.com/upcoming/Tennis"
geckodriver_path = 'working file\geckodriver.exe'
wait_until_class = "game-euro-mob"
scroll_distance = 200 # Adjust this value to control the amount of scrolling
scroll_delay = 0.1