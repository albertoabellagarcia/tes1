from selenium import webdriver
     
    # you can use driver = webdriver.PhantomJS() 
    # if you want a headless browser. 
    # You need to have PhantomJS installed in path
     
driver = webdriver.Firefox()
     
driver.get("http://www.tarlabs.com")
     
    # will print the page source
print driver.page_source
