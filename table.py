from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\Chrome webdriver\chromedriver.exe")
#driver.get("http://localhost:63342/Selenium%20Project/table11.html?_ijt=en2nrrt7uupdeuiku17dcn1j4q")
driver.get("file:///C:/Users/NARAYAN%20SAHOO/PycharmProjects/Selenium%20Project/table11.html")

rows = driver.find_element_by_xpath("/html/body/table/tbody/tr")  #/html/body/table/tbody
cols = driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/th")
print(len(rows))
print(len(cols))

print("Firstname"+"  "+"Lastname"+"age")
for r in range(2, rows+1):
    for c in range(1, cols+1):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end=" ")
        print()


