import pyautogui
import time

#Steps involved
#1- Go to the search bar and click it
#2- Go and open google chrome browser   
#3- Go to the url bar and click on it then type the facebook link then hit enter
#4- Search for the group on FB
#5- Open the group that appeared in the search
#6- Open the post area and write content
#7- Post it


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
pyautogui.write("facebook.com", 0.01)
time.sleep(0.1)
pyautogui.hotkey('Enter')

#4- Search for the group on FB
SearchInFacebook_Location = pyautogui.locateCenterOnScreen("4-SearchInFacebook.png", grayscale=True, confidence= 0.5)
#loop tell finding the required pixels
while SearchInFacebook_Location == None:
    SearchInFacebook_Location = pyautogui.locateCenterOnScreen("4-SearchInFacebook.png", grayscale=True, confidence= 0.5)
pyautogui.moveTo(SearchInFacebook_Location.x, SearchInFacebook_Location.y)
pyautogui.click()
pyautogui.write("9707022220@IMTSchool")
pyautogui.click()


#5- Open the group that appeared in the search
IMTEmbeddedLinuxGroup_Location = pyautogui.locateCenterOnScreen("5-IMTEmbeddedLinuxGroup.png", grayscale=True, confidence= 0.7)
#loop tell finding the required pixels
while IMTEmbeddedLinuxGroup_Location == None:
    IMTEmbeddedLinuxGroup_Location = pyautogui.locateCenterOnScreen("5-IMTEmbeddedLinuxGroup.png", grayscale=True, confidence= 0.7)
pyautogui.moveTo(IMTEmbeddedLinuxGroup_Location.x, IMTEmbeddedLinuxGroup_Location.y)
pyautogui.click()


#6- Open the post area and write content
writeSomething_Location = pyautogui.locateCenterOnScreen("6-writeSomething.png", grayscale=True, confidence= 0.7)
#loop tell finding the required pixels
while writeSomething_Location == None:
    writeSomething_Location = pyautogui.locateCenterOnScreen("6-writeSomething.png", grayscale=True, confidence= 0.7)
pyautogui.moveTo(writeSomething_Location.x, writeSomething_Location.y)
pyautogui.click()
time.sleep(0.5)

pyautogui.write('''Alsalam Alaykum
This post is written automatically by python script

Late is better than never

The video will be posted in the comments with the source code''')

#7- Post it
time.sleep(3)
PostButton_Location = pyautogui.locateCenterOnScreen("7-PostButton.png", grayscale=True, confidence= 0.7)
#loop tell finding the required pixels
while PostButton_Location == None:
    PostButton_Location = pyautogui.locateCenterOnScreen("7-PostButton.png", grayscale=True, confidence= 0.7)
pyautogui.moveTo(PostButton_Location.x, PostButton_Location.y)
pyautogui.click()
 