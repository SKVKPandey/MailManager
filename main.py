from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from selenium import webdriver
from pyautogui import press
from _thread import start_new_thread
from time import sleep

Window.size = (1400, 700)

ChromeDriverPath = 'Drivers\chromedriver.exe'

code='''
ScreenManager:
	MainScreen:

<MainScreen>:
	
	name:'main'
    spam:spam
    inbox:inbox
    data:data
    win:win
    openspam:openspam
    openinbox:openinbox
	
	MDNavigationLayout:

		ScreenManager:
			Screen:

                MDBoxLayout:
                    orientation: 'vertical'

                    MDGridLayout:
                        cols: 4
                        size_hint_y: None
                        height: '60dp'

                        MDBoxLayout:
                            orientation: 'vertical'
                            line_color: 0, 0, 1, 1
                            md_bg_color: 0, 1, 1, 0.5

                            MDGridLayout:
                                cols: 2

                                MDCheckbox:

                                MDLabel:
                                    text: "Direct Login"

                                MDCheckbox:

                                MDLabel:
                                    text: "Profiles"

                        MDBoxLayout:
                            orientation: 'vertical'
                            line_color: 0, 0, 1, 1
                            md_bg_color: 0, 1, 1, 0.5

                            MDGridLayout:
                                cols: 2

                                MDCheckbox:

                                MDLabel:
                                    text: "Reporting"

                        MDBoxLayout:
                            orientation: 'vertical'
                            line_color: 0, 0, 1, 1
                            md_bg_color: 0, 1, 1, 0.5

                            MDGridLayout:
                                cols: 2

                                MDCheckbox:

                                MDLabel:
                                    text: "Chrome"

                                MDCheckbox:

                                MDLabel:
                                    text: "Firefox"

                        MDBoxLayout:
                            orientation: 'vertical'
                            line_color: 0, 0, 1, 1
                            md_bg_color: 0, 1, 1, 0.5

                            MDGridLayout:
                                cols: 2

                                MDCheckbox:

                                MDLabel:
                                    text: "Opera"

                                MDCheckbox:

                                MDLabel:
                                    text: "Edge"

                    Widget:

                MDBoxLayout:
                    orientation: 'vertical'
                    padding: 30

                    MDGridLayout:
                        cols: 2
                        size_hint_y: None
                        height: '100dp'
                    
                        MDBoxLayout:
                            orientation: "horizontal"

                            MDBoxLayout:
                                orientation: "vertical"

                                MDGridLayout:
                                    cols: 2

                                    MDLabel:
                                        text: "Spam Messages"

                        MDBoxLayout:
                            orientation: "horizontal"

                            MDBoxLayout:
                                orientation: "vertical"

                                MDGridLayout:
                                    cols: 2

                                    MDLabel:
                                        text: "Inbox Messages"

                    MDGridLayout:
                        cols: 2
                        size_hint_y: None
                        height: '20dp'      

                        MDBoxLayout:
                            orientation: "horizontal"
                            line_color: 0, 0, 1, 1

                            MDGridLayout:
                                cols: 2

                                MDCheckbox:
                                    id: spam

                                MDLabel:
                                    text: "One By One"

                            MDGridLayout:
                                cols: 2

                                Widget:

                                Widget:

                        MDBoxLayout:
                            orientation: "horizontal"
                            line_color: 0, 0, 1, 1

                            MDGridLayout:
                                cols: 2

                                MDCheckbox:
                                    id: inbox

                                MDLabel:
                                    text: "One By One"

                            MDGridLayout:
                                cols: 2
                                
                                Widget:

                                Widget:

                    MDGridLayout:
                        cols: 2
                        size_hint_y: None
                        height: '300dp'      

                        MDBoxLayout:
                            orientation: "vertical"
                            line_color: 0, 0, 1, 1

                            MDBoxLayout:
                                orientation: "vertical"

                                MDGridLayout:
                                    cols: 4

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:
                                                id: openspam

                                            MDLabel:
                                                text: "Open"

                                    Widget:

                                    Widget:

                                    Widget:

                            MDBoxLayout:
                                orientation: "vertical"

                                MDGridLayout:
                                    cols: 4

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:

                                            MDLabel:
                                                text: "No Action"
                                                font_size: '12dp'

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:

                                            MDLabel:
                                                text: "Add Flag"
                                                font_size: '12dp'

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:

                                            MDLabel:
                                                text: "Add to Contact"
                                                font_size: '12dp'

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:

                                            MDLabel:
                                                text: "Reply"
                                                font_size: '12dp'

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:

                                            MDLabel:
                                                text: "Forward"
                                                font_size: '12dp'

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:

                                            MDLabel:
                                                text: "Click Link"
                                                font_size: '12dp'

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:

                                            MDLabel:
                                                text: "Mark Read"
                                                font_size: '12dp'

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:

                                            MDLabel:
                                                text: "Categorize"
                                                font_size: '12dp'  
                            
                        MDBoxLayout:
                            orientation: "vertical"
                            line_color: 0, 0, 1, 1

                            MDBoxLayout:
                                orientation: "vertical"

                                MDGridLayout:
                                    cols: 4

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:
                                                id: openinbox

                                            MDLabel:
                                                text: "Open"

                                    Widget:

                                    Widget:

                                    Widget:

                            MDBoxLayout:
                                orientation: "vertical"

                                MDGridLayout:
                                    cols: 4

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:

                                            MDLabel:
                                                text: "No Action"
                                                font_size: '12dp'

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:

                                            MDLabel:
                                                text: "Add Flag"
                                                font_size: '12dp'

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:

                                            MDLabel:
                                                text: "Add to Contact"
                                                font_size: '12dp'

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:

                                            MDLabel:
                                                text: "Reply"
                                                font_size: '12dp'

                                MDGridLayout:
                                    cols: 5

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:

                                            MDLabel:
                                                text: "Forward"
                                                font_size: '12dp'

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:

                                            MDLabel:
                                                text: "Click Link"
                                                font_size: '12dp'

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:

                                            MDLabel:
                                                text: "Archive"
                                                font_size: '12dp'

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:

                                            MDLabel:
                                                text: "Pin"
                                                font_size: '12dp'

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:

                                            MDLabel:
                                                text: "Categorize"
                                                font_size: '12dp'  
                    MDBoxLayout:
                        orientation: 'vertical'

                        MDGridLayout:
                            cols: 1
                            size_hint_y: None
                            height: '100dp'

                            MDTextFieldRect:
                                id: data
                                hint_text: "Email ID (Required); Password(required); Proxy IP"
                                required: True
                                multiline: True
                                size_hint: 0.4, None
                                height: "80dp"
                                pos_hint: {'center_x': 0.2}

                            Widget:

                        MDGridLayout:
                            cols: 4
                            size_hint_y: None
                            height: '80dp'
                            spacing: 20

                            MDTextFieldRect:
                                id: win
                                hint_text: "Windows"
                                required: True
                                size_hint: None, None
                                height: "30dp"
                                pos_hint: {'center_x': 0.2}

                            MDRaisedButton:
                                text: "Start"
                                text_color: 0, 0, 0, 1
                                md_bg_color: 0, 0, 1, 1
                                on_release: root.start()
                                

                            MDRaisedButton:
                                text: "Pause"
                                text_color: 0, 0, 0, 1
                                md_bg_color: 1, 1, 0, 1

                            MDRaisedButton:
                                text: "Stop"
                                text_color: 0, 0, 0, 1
                                md_bg_color: 1, 0, 0, 1

'''

class MainScreen(Screen):

    def winGenerator(self, win):
        for row in win:
            if self.spam.active:
                if len(row)==2:
                    driver = webdriver.Chrome(ChromeDriverPath) #Drive_Address
                    driver.get(f'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1653476060&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3ded19b33f-25c3-b2f9-7ec9-4a74b91fdab7&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
                    sleep(2)

                    username = driver.find_element_by_xpath("//input[@name='loginfmt']")

                    username.send_keys(f'''{row[0].strip()}''') 

                    sleep(0.5)

                    submit = driver.find_element_by_xpath("//input[@type='submit']").click()
                    sleep(2)

                    password = driver.find_element_by_xpath("//input[@name='passwd']")

                    password.send_keys(f'''{row[1].strip()}''')
                    sleep(0.5)

                    submit = driver.find_element_by_xpath("//input[@type='submit']").click()
                    sleep(2)

                    submit = driver.find_element_by_xpath("//input[@type='submit']").click()
                    sleep(2)

                    driver.get('https://outlook.live.com/mail/0/junkemail')
                    sleep(5)

                    if self.openspam.active:

                        while True:

                            try:

                                submit = driver.find_element_by_xpath("//div[@role='option']").click()
                                sleep(4)

                                submit = driver.find_element_by_xpath(f'//*[@id="ReadingPaneContainerId"]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/span[2]').click()
                                sleep(4)

                                press('enter')
                                sleep(2)

                            except Exception as e:
                                print(e)
                                break

                elif len(row)>=3:
                    PROXY = row[2]
                    chrome_options = webdriver.ChromeOptions()
                    chrome_options.add_argument('--proxy-server=%s' % PROXY)
                    driver = webdriver.Chrome(ChromeDriverPath, options=chrome_options) #Drive_Address
                    driver.get(f'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1653476060&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3ded19b33f-25c3-b2f9-7ec9-4a74b91fdab7&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
                    sleep(2)

                    username = driver.find_element_by_xpath("//input[@name='loginfmt']")

                    username.send_keys(f'''{row[0].strip()}''') 

                    sleep(0.5)

                    submit = driver.find_element_by_xpath("//input[@type='submit']").click()
                    sleep(2)

                    password = driver.find_element_by_xpath("//input[@name='passwd']")

                    password.send_keys(f'''{row[1].strip()}''')
                    sleep(0.5)

                    submit = driver.find_element_by_xpath("//input[@type='submit']").click()
                    sleep(2)

                    submit = driver.find_element_by_xpath("//input[@type='submit']").click()
                    sleep(2)

                    driver.get('https://outlook.live.com/mail/0/junkemail')
                    sleep(5)

                    if self.openinbox.active:

                        while True:

                            try:

                                submit = driver.find_element_by_xpath("//div[@role='option']").click()
                                sleep(4)

                                submit = driver.find_element_by_xpath(f'//*[@id="ReadingPaneContainerId"]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/span[2]').click()
                                sleep(4)

                                press('enter')
                                sleep(2)

                            except Exception as e:
                                print(e)
                                break                    

            elif self.inbox.active:
                if len(row)==2:
                    print(row)
                    driver = webdriver.Chrome(ChromeDriverPath) #Drive_Address
                    driver.get(f'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1653476060&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3ded19b33f-25c3-b2f9-7ec9-4a74b91fdab7&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
                    sleep(2)

                    username = driver.find_element_by_xpath("//input[@name='loginfmt']")

                    username.send_keys(f'''{row[0].strip()}''') 

                    sleep(0.5)

                    submit = driver.find_element_by_xpath("//input[@type='submit']").click()
                    sleep(2)

                    password = driver.find_element_by_xpath("//input[@name='passwd']")

                    password.send_keys(f'''{row[1].strip()}''')
                    sleep(0.5)

                    submit = driver.find_element_by_xpath("//input[@type='submit']").click()
                    sleep(2)

                    submit = driver.find_element_by_xpath("//input[@type='submit']").click()
                    sleep(2)

                    driver.get('https://outlook.live.com/mail/0/')
                    sleep(5)

                    while True:

                        try:

                            submit = driver.find_element_by_xpath("//div[@role='option']").click()
                            sleep(4)

                            submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[5]/button/span/i[2]').click()
                            sleep(2)
                        
                            press('down')
                            press('enter')
                            sleep(2)

                        except Exception as e:
                            print(e)
                            break
                        
                elif len(row)>=3:
                    chrome_options = webdriver.ChromeOptions()
                    chrome_options.add_argument('--proxy-server=%s' % row[2].strip())
                    driver = webdriver.Chrome(ChromeDriverPath, options=chrome_options) #Drive_Address
                    driver.get(f'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1653476060&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3ded19b33f-25c3-b2f9-7ec9-4a74b91fdab7&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
                    sleep(2)

                    username = driver.find_element_by_xpath("//input[@name='loginfmt']")

                    username.send_keys(f'''{row[0].strip()}''') 

                    sleep(0.5)

                    submit = driver.find_element_by_xpath("//input[@type='submit']").click()
                    sleep(2)

                    password = driver.find_element_by_xpath("//input[@name='passwd']")

                    password.send_keys(f'''{row[1].strip()}''')
                    sleep(0.5)

                    submit = driver.find_element_by_xpath("//input[@type='submit']").click()
                    sleep(2)

                    submit = driver.find_element_by_xpath("//input[@type='submit']").click()
                    sleep(2)

                    driver.get('https://outlook.live.com/mail/0/junkemail')
                    sleep(5)

                    while True:

                        try:

                            submit = driver.find_element_by_xpath("//div[@role='option']").click()
                            sleep(4)

                            submit = driver.find_element_by_xpath(f'//*[@id="ReadingPaneContainerId"]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/span[2]').click()
                            sleep(4)

                            press('enter')
                            sleep(2)

                        except Exception as e:
                            print(e)
                            break

    
    def start(self):
        data_list = [tuple(x.split(';')) for x in self.data.text.split('\n')]
        win_sequence =[]
        win_n = int(self.win.text.strip())

        for i in range(win_n, len(data_list), win_n):
            win_sequence.append(data_list[i-win_n:i])
        win_sequence.append(data_list[-(len(data_list)%win_n):])

        for win in win_sequence:
            start_new_thread(self.winGenerator, (win,))

            
sm = ScreenManager()
sm.add_widget(MainScreen(name = 'main'))

class MailManagerApp(MDApp):

    def build(self):
        self.theme_cls = ThemeManager()
		#self.icon="a_icon.png"
        self.theme_cls.primary_palette='DeepPurple'
        self.theme_cls.primary_hue='900'
        self.screen=Builder.load_string(code)
        return self.screen

MailManagerApp().run()