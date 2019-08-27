from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
from database.db import Dbase
class MailChecker:
    def __init__(self):
        self.email=""
        driverPath="./chromedriver.exe"
        self.regLink="https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&ct=1565704119&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d2202f2e7-d609-66d6-fcfc-08f622594775&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&contextid=D828185C1AB15CCA&bk=1565704336&uiflavor=web&mkt=TR-TR&lc=1055&uaid=c96eb594b09249d18c12d4466cc843b5&lic=1"
        #self.browser=webdriver.Chrome(executable_path=driverPath)
        self.browser = webdriver.PhantomJS(executable_path="./phantomjs-2.1.1-windows/bin/phantomjs.exe") # or add to your PATH
        self.browser.get(self.regLink)
        self.vt=Dbase()
    def check(self,email):
        self.browser.find_element_by_id("MemberName").send_keys(email)
        s1=Select(self.browser.find_element_by_id("LiveDomainBoxList"))
        s1.select_by_value("hotmail.com")
        time.sleep(1)
        self.browser.find_element_by_id("iSignupAction").click()
        time.sleep(1)
        try:
            self.browser.find_element_by_id("MemberNameError").text
            self.vt.addNonAvaible(email)
            return "Not Avaible"
        except:
            self.vt.addAvaible(email)
            return "Avaible"
        self.quit()
    def quit(self):
        self.browser.quit()