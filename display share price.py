from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tkinter import *
import tkinter.font as font
import time
import json

with open('stock_names_url.json', 'r') as f:
    stocks_name_dict = json.load(f)


time_input = int(input('\nHow much seconds delay do you want? '))
user_input = input('Enter the Company Name : ')

temp_list = []
for x, y in stocks_name_dict.items():
    if user_input.upper() in x.upper():
        temp_list1 = [x,y]
        temp_list.append(temp_list1)

#print(temp_list)

if len(temp_list) > 1:
    print('')
    print(f'Companies that have {user_input} in their name are : ')
    # print(', '.join(temp_list))
    available_options = ''
    for item in temp_list:
        available_options += item[0] + '\n'

    print(available_options)
    print('This entry is CASE SENSITIVE. Please enter carefully.')
    selection = input('Which one? ')
    url = stocks_name_dict[f'{selection}']
else:
    selection = temp_list[0][0]
    url = stocks_name_dict[f'{temp_list[0][0]}']

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome("E:\Python\chromedriver.exe", options=options)
driver.get(url)


def share_price_alert():
    live_stock_price = (driver.find_element_by_id('nsecp')).get_attribute('data-numberanimate-value')

    gui = Tk(className='Stock Price Alert')
    gui.geometry("500x200")

    # define font
    myFont = font.Font(family='Helvetica', size=40, weight='bold')

    # create button
    button = Button(gui, text=f'{selection} - {live_stock_price}', bg='black', fg='white')

    # apply font to the button label
    button['font'] = myFont

    # add button to gui window
    button.pack()
    
    #Make the window jump above all
    gui.attributes('-topmost',True)

    gui.after(5000, lambda: gui.destroy())

    gui.mainloop()

    time.sleep(time_input)
    share_price_alert()


share_price_alert()