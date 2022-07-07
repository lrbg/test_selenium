import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

class FindByClassName (unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Chrome('/Users/ba3/Desktop/chromedriver')
        driver.get('http://automationpractice.com/index.php')

    def testGetbntLogin(self):
        global btnLogin
        global inpUser
        
        btnLogin = driver.find_element_by_class_name("login")
        if btnLogin is not None:
            print("i found element Login")
            print (btnLogin)
            btnLogin.click()
            
        inpUser = driver.find_element_by_id("email")
        if inpUser is not None:
            print("i found element inpUser")
            print (inpUser)
            inpUser.send_keys("usertest2@mail.com")
            
        inpPass = driver.find_element_by_id("passwd")
        if inpPass is not None:
            print("i found element inpPass")
            print (inpPass)
            inpPass.send_keys("12121212Qw.")

        btnSubLogin = driver.find_element_by_id("SubmitLogin")
        if btnSubLogin is not None:
            print("i found element btnSubLogin")
            print (btnSubLogin)
            btnSubLogin.click()

        btnMenAdress = driver.find_element_by_xpath("//*[@id='block_top_menu']/ul/li[2]/a")
        if btnMenAdress is not None:
            print("i found element btnMenAdress")
            print (btnMenAdress)
            btnMenAdress.click()


        tltAdress = driver.find_element_by_xpath("//*[@id='center_column']/h1/span[1]")
        if tltAdress is not None:
            print("i found element title tltAdress")
            print (tltAdress)
            print("TITLE  ---> ", tltAdress.text)
            getAtributeTitle = tltAdress.get_attribute("class")
            print("ATRIBUTE CLASS ---->", getAtributeTitle)
           
        slcSortByProducts = driver.find_element_by_id("selectProductSort")
        if slcSortByProducts is not None:
            print("i found element slcSortByProducts")
            print (slcSortByProducts)
            selectBySort = Select(slcSortByProducts)
            selectBySort.select_by_value("quantity:desc")

        time.sleep(15)          

        btnLogOut = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div/nav/div[2]/a")
        if btnLogOut is not None:
            print("i found element btnLogOut")
            print (btnLogOut)
            btnLogOut.click()            

            


        

            

    #def testGetbntContactLink(self):
        #global btnConactLink
        #btnConactLink = driver.find_element_by_id("contact-link")
        #if btnConactLink is not None:
            #print("i found element btnConactLink")
            #print (btnConactLink)

    #def testGetimgDress(self):
        #global imgDressOrange
        #imgDressOrange = driver.find_element_by_xpath("//img[@src='http://automationpractice.com/img/p/8/8-home_default.jpg'][1]")
        #if imgDressOrange is not None:
            #print("i found element imgDressOrange")
            #print (imgDressOrange)

            
    def tearDown(self):
        driver.quit()
        print(":::::::::::: termine ::::::::::::")
