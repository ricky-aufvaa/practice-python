from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://tpirbay.top/search/the%20spiderman/1/99/0");
elements= driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/table/tbody/tr[1]/td[2]/a[1]");

#elements= driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/table/tbody/tr[2]/td[2]/a[1]");
# title = driver.find_elements(
# href = ""
# for element in elements:
#     href = element.get_attribute("href")
#     print(href)

titlehref = driver.find_elements(By.XPATH,"/html/body/div[2]/div[3]/table/tbody/tr[2]/td[2]/div/a")
for title in titlehref:
    tile= title.get_attribute("title")
    print(tile)
    # print(elements)

#print(WebElement)
driver.quit()
#element.click();
