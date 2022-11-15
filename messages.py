import pyautogui
import webbrowser
from time import sleep
import phone

# phone_number = input("Phone Number(with area code): ")
num_messages = input("Amount of messages: ")
message = input("Message to sent: ")

num_messages_parsed = int(num_messages)


def message_iterator():
    webbrowser.open('https://web.whatsapp.com/send?phone='+phone.get_phone())
    sleep(10)
    for index in range(num_messages_parsed):
        print(index, message)
        pyautogui.typewrite(message)
        pyautogui.press('enter')


message_iterator()
