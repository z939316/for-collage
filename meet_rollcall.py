from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys

code = 'xojfgtsetv'#會議代碼
account='810293@stu.nknush.kh.edu.tw'
password="***********"


alist=["王XX","蘇XX","黃XX"]
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })

driver = webdriver.Chrome(options=opt, executable_path='C:\Program Files (x86)\chromedriver.exe')
meetpath="https://accounts.google.com/ServiceLogin?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&"
driver.get(meetpath)
driver.find_element_by_name('identifier').send_keys(account)
#輸入帳號

driver.find_element_by_xpath("//*[@id='identifierNext']").click()
time.sleep(2)
driver.find_element_by_name('password').send_keys(password)
#輸入密碼

driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
time.sleep(3)
driver.find_element_by_id("i3").send_keys('xojfgtsetv')
driver.find_element_by_id("i3").send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[1]/div[3]/div/div[2]/div[1]/span').click()
time.sleep(1)
clist = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[1]/div[2]/div[2]/div').text
driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[1]/div[2]').click()
driver.find_element_by_name('chatTextInput').send_keys('要點名囉')
driver.find_element_by_name('chatTextInput').send_keys(Keys.ENTER)
print(clist,"clist")
f=0;
ur=""
for i in range(45):
    if alist[i] not in clist:
        if i < 4:
            ur+="\n"+str(i+1)+'號 '+alist[i]+" 沒到"
            f=1
        if i > 3:
            ur+="\n"+str(i+2)+'號 '+alist[i]+" 沒到"
            f=1;
if f==0:
    ur=ur+"全到！"
driver.find_element_by_name('chatTextInput').send_keys(ur)
driver.find_element_by_name('chatTextInput').send_keys(Keys.ENTER)







