from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://brainacad.demo.site/english/customer/account/create/")
assert "Create New Customer Account" in driver.title
def otherfield(namefield,let):
    elem2 = driver.find_element_by_name(namefield)
    elem2.clear()
    elem2.send_keys(let)

def login(elname,file):
    elem = driver.find_element_by_name(elname)
    doc= open(file)
    for i3 in doc.readlines():
          letters=i3
          elem.clear()
          elem.send_keys(letters)
          elem.send_keys(Keys.TAB)
          elem.send_keys(Keys.RETURN)
          test = driver.find_element_by_name(elname).value_of_css_property('border-top-color')
          if test == "rgba(192, 192, 192, 1)":
              mark = " OK"
          else:
              mark = " Bad"
          elem.clear()
          f = open (file,"a")
          i4=letters+mark
          print(i4)
          f.write(i4+'\n')
          f.close()
 
index=1
while index<5:
    if index ==1:
        otherfield("lastname","Boosh")
        otherfield("email","p@p.com")
        otherfield("password","111111")
        otherfield("confirmation","11111")
        login("firstname","firstname.txt")
        index=index+1
    elif index ==2:
            otherfield("firstname","Boosh")
            otherfield("email","p@p.com")
            otherfield("password","111111")
            otherfield("confirmation","11111")
            login("lastname","lastname.txt")
            index=index+1
    elif index ==3:
            otherfield("firstname","Boosh")
            otherfield("lastname","Boosh")
            otherfield("password","111111")
            otherfield("confirmation","11111")
            login("email","email.txt")
            index=index+1
    elif index ==4:
            otherfield("firstname","Boosh")
            otherfield("lastname","Boosh")
            otherfield("email","p@p.com")
            otherfield("confirmation","QWERTTYUYTvbvnm98675452222njvhrk")
            login("password","password.txt")
            index=index+2
    else:
        print("Тестирование окончено")
