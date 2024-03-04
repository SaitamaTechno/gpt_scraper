try:
    import sql1
    import time
    while 1:
        f=open("/headless/gpt/webdriver_status.txt", "r")
        webdriver_status=f.read()
        f.close()
        if webdriver_status=="processing":
            break
        print(webdriver_status)
        time.sleep(1)

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import ElementNotInteractableException
    from selenium.common.exceptions import StaleElementReferenceException
    from selenium.common.exceptions import WebDriverException

    import json

    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-data-dir=/headless/.config/chromium/") #Path to your chrome profile
    #options.add_experimental_option('prefs', {'intl.accept_languages': 'tr,tr_TR'})
    #options.add_argument("--lang=tr_TR.UTF-8")
    #options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    #input("first page")

    driver.get("https://chat.openai.com")
    time.sleep(5)
    print(driver.title)
    #input("first page")
    #time.sleep(3)                         
    #chat1=driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div/nav/div[2]/div[2]/div/span[3]/div/ol/li/div/a")
    #chat_link=chat1.get_attribute("href")
    #driver.get(chat_link)
    #time.sleep(5)
    text_input=driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/main/div[2]/div[2]/form/div/div/div/textarea")
    text_input.send_keys("hi")
    text_input.send_keys(Keys.ENTER)
    time.sleep(2)
    div_list=driver.find_elements(By.XPATH, f"/html/body/div[1]/div[1]/div[2]/main/div[2]/div[1]/div/div/div/div")
    a=len(div_list)
    a+=20
    def ask_gpt(question):
        #input("textarea")
        global a
        text_input=driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/main/div[2]/div[2]/form/div/div/div/textarea")
        text_input.send_keys(question)
        text_input.send_keys(Keys.ENTER)
        time.sleep(1)
        a+=20
        for i in range(a,0,-1):
            try:
                last_msg_owner=driver.find_element(By.XPATH, f"/html/body/div[1]/div[1]/div[2]/main/div[2]/div[1]/div/div/div/div[{i}]/div/div/div[2]/div[1]")
                last_msg_owner=last_msg_owner.text
                if last_msg_owner=="ChatGPT":
                    a=i
                    break
            except NoSuchElementException:
                pass
        print(a)
        while 1:
            try:
                driver.find_element(By.XPATH, f"/html/body/div[1]/div[1]/div[2]/main/div[2]/div[1]/div/div/div/div[{a}]/div/div/div[2]/div[2]/div[2]/div/div")
                break
            except NoSuchElementException:
                time.sleep(0.1)
        time.sleep(0.3)
        response=driver.find_element(By.XPATH, f"/html/body/div[1]/div[1]/div[2]/main/div[2]/div[1]/div/div/div/div[{a}]/div/div/div[2]/div[2]/div[1]/div/div")
        response=response.text
        return response
    time.sleep(10)
    f=open("/headless/gpt/webdriver_status.txt", "w")
    f.write("on")
    f.close()

    while 1:
        response=sql1.last_msg()
        if response[2]=="!gpt":
            answer=ask_gpt(response[1])
            sql1.update_last_msg(answer)
            print(answer)
            f=open("/headless/gpt/webdriver_status.txt", "w")
            f.write("processing")
            f.close()
        time.sleep(0.1)

    """
    while 1:
        question=input("Ask:")
        response=ask_gpt(question)
        print(response)
    input("Finished")
    driver.quit()
    """
except Exception as e:
    f=open("/headless/gpt/webdriver_status.txt", "w")
    f.write("Error:This error occurs because you probably did not login to chatgpt with your credentials. Please delete this container and create a new one. Then, log in your credentials in VNC. "+str(e))
    f.close()
    driver.quit()
    sql1.update_last_msg("Error:This error occurs because you probably did not login to chatgpt with your credentials. Please delete this container and create a new one. Then, log in your credentials in VNC. "+str(e))
    