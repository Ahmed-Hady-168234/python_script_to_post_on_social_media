import pyautogui
import time

#Steps involved
#1- Go to the search bar and click it
#2- Go and open google chrome browser   
#3- Go to the url bar and click on it then type the Linkedin link then hit enter
#4- Open the post area and write the content
#5- Post it


#1- Go to the search bar and click it
TypeHereToSearch_TextBox_Location = pyautogui.locateCenterOnScreen("1-TypeHereToSearch_TextBox.png", grayscale=True, confidence= 0.5)
pyautogui.moveTo(TypeHereToSearch_TextBox_Location.x, TypeHereToSearch_TextBox_Location.y)
pyautogui.click()
#write google chrome in the search bar
pyautogui.write("Google Chrome")


#2- Go and open google chrome browser   
googleChrome_Location = pyautogui.locateCenterOnScreen("2-googleChrome.png", grayscale=True, confidence= 0.5)
#loop tell finding the required pixels
while googleChrome_Location == None:
    googleChrome_Location = pyautogui.locateCenterOnScreen("2-googleChrome.png", grayscale=True, confidence= 0.5)
pyautogui.moveTo(googleChrome_Location.x, googleChrome_Location.y)
pyautogui.click()

#3- Go to the url bar and click on it then type the facebook link then hit enter
chromEnterURL_Location = pyautogui.locateCenterOnScreen("3-chromEnterURL.png")
#loop tell finding the required pixels
while chromEnterURL_Location == None:
    chromEnterURL_Location = pyautogui.locateCenterOnScreen("3-chromEnterURL.png", grayscale=True, confidence= 0.5)
pyautogui.moveTo(chromEnterURL_Location.x, chromEnterURL_Location.y)
pyautogui.click()
pyautogui.write("www.linkedin.com", 0.01)
time.sleep(0.3)
pyautogui.hotkey('Enter')


#4- Open the post area and write the content
startPost_Location = pyautogui.locateCenterOnScreen("4-startPost.png", grayscale=True, confidence= 0.7)
#loop tell finding the required pixels
while startPost_Location == None:
    startPost_Location = pyautogui.locateCenterOnScreen("4-startPost.png", grayscale=True, confidence= 0.7)
pyautogui.moveTo(startPost_Location.x, startPost_Location.y)
pyautogui.click()
time.sleep(0.5)

pyautogui.write('''
Alsalam Alaykum
This post is written automatically by python script
As a solution of the task required in the Embedded Linux Diploma at IMT school
The recorded video and source code can be founded in the comments
''')

#5- Post it
time.sleep(3)
PostButton_Location = pyautogui.locateCenterOnScreen("5-PostButton.png", grayscale=True, confidence= 0.7)
#loop tell finding the required pixels
while PostButton_Location == None:
    PostButton_Location = pyautogui.locateCenterOnScreen("5-PostButton.png", grayscale=True, confidence= 0.7)
pyautogui.moveTo(PostButton_Location.x, PostButton_Location.y)
pyautogui.click()
