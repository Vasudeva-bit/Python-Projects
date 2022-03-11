from selenium import webdriver
browser=webdriver.Chrome('./chromedriver')
browser.get('http://www.seleniumeasy.com/test/basic-first-form-demo.html')
assert 'Selenium Easy Demo' in browser.title
button=browser.find_element_by_class_name('btn-default')
assert 'Show Message' in button.text 
button=browser.find_element_by_class_name('btn-default')
input=browser.find_element_by_id('user-message')
input.clear()
input.send_keys('hi')
button.click()
print('hi' in (browser.find_element_by_id('display')).text)
browser.close()
