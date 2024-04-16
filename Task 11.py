from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from time import sleep


class DragAndDrop:

    def __init__(self):
        self.url = "https://jqueryui.com/droppable/"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.actions = ActionChains(self.driver)

    def findElementByID(self, ID):
        return self.driver.find_element(By.ID,value=ID)

    def findElementByXpath(self,XPATH):
        return self.driver.find_element(By.XPATH, value=XPATH) # It is used to return the element by Xpath



    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(3)


    def quit(self):
        self.driver.quit()


    def getDragAndDrop(self):
        # This try block is used to check whether the element is present
        try:
            self.boot()
            # This method is used to switch between the frame
            self.driver.switch_to.frame(0)
            # It is used to find the staring point of Drag process by its ID
            start = self.findElementByID("draggable")
            # It Is used to find the destination point by its ID
            destination = self.findElementByID("droppable")
            # This method is used to perform the action
            self.actions.drag_and_drop(start,destination).perform()
            sleep(3)
            # It is used to check whether the process is done successfully
            Droppable= self.findElementByID("droppable")
            print(Droppable.text)
            if Droppable.text == "Dropped!":
                print("Success")
            else:
                print("Error")
        except NoSuchElementException as e:
            print(e)
        finally:
            self.driver.quit()

obj = DragAndDrop()
obj.getDragAndDrop()







