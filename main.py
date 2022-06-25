from xml.dom.minidom import Element
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from selenium import webdriver
from pyautogui import press
from itertools import islice
from time import sleep
from socks import create_connection
from socks import PROXY_TYPE_SOCKS4
from socks import PROXY_TYPE_SOCKS5
from socks import PROXY_TYPE_HTTP
from imaplib import IMAP4
from imaplib import IMAP4_SSL
from imaplib import IMAP4_PORT
from imaplib import IMAP4_SSL_PORT
import ssl
import concurrent.futures

Window.size = (1400, 900)

ChromeDriverPath = 'Drivers\chromedriver.exe'

outlook_imap_url = 'imap-mail.outlook.com'

code='''
ScreenManager:
	BrowserModeScreen:
    IMAPModeScreen:

<BrowserModeScreen>:
	
	name:'brws'
    report:report
    spam:spam
    inbox:inbox
    data:data
    win:win
    openspam:openspam
    openinbox:openinbox
    spamnoaction:spamnoaction
    spamflag:spamflag
    spamread:spamread
    inboxnoaction:inboxnoaction
    inboxflag:inboxflag
    inboxpin:inboxpin
	
	MDNavigationLayout:

		ScreenManager:
			Screen:

                MDBoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Browser Mode"
                        elevation: 10
                        pos_hint: {"top": 1}

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
                                    id: report

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

                    MDBoxLayout:
                        orientation: 'horizontal'

                        MDRaisedButton:
                            text: "Browser Mode"

                        MDFlatButton:
                            text: "IMAP Mode"
                            on_release: 
                                app.root.current = 'imap'
                                root.manager.transition.direction = 'left'

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
                                                id: spamnoaction

                                            MDLabel:
                                                text: "No Action"
                                                font_size: '12dp'

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:
                                                id: spamflag

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
                                                id: spamread

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
                                                id: inboxnoaction

                                            MDLabel:
                                                text: "No Action"
                                                font_size: '12dp'

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:
                                                id: inboxflag

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
                                                id: inboxpin

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
                                hint_text: "Email ID (Required); Password(required); Proxy IP:Port"
                                required: True
                                multiline: True
                                size_hint: 0.4, None
                                height: "80dp"
                                pos_hint: {'center_x': 0.2}

                            Widget:

                        MDGridLayout:
                            cols: 3
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
                                text: "Stop"
                                text_color: 0, 0, 0, 1
                                md_bg_color: 1, 0, 0, 1

<IMAPModeScreen>:
	
	name:'imap'
    report:report
    spam:spam
    inbox:inbox
    data:data
    openspam:openspam
    openinbox:openinbox
    spamnoaction:spamnoaction
    spamflag:spamflag
    spamread:spamread
    inboxnoaction:inboxnoaction
    inboxflag:inboxflag
    inboxpin:inboxpin
	
	MDNavigationLayout:

		ScreenManager:
			Screen:

                MDBoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "IMAP Mode"
                        elevation: 10
                        pos_hint: {"top": 1}

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
                                    id: report

                                MDLabel:
                                    text: "Reporting"

                    Widget:

                MDBoxLayout:
                    orientation: 'vertical'
                    padding: 30

                    MDBoxLayout:
                        orientation: 'horizontal'

                        MDFlatButton:
                            text: "Browser Mode"
                            on_release: 
                                app.root.current = 'brws'
                                root.manager.transition.direction = 'right'

                        MDRaisedButton:
                            text: "IMAP Mode"

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
                                                id: spamnoaction

                                            MDLabel:
                                                text: "No Action"
                                                font_size: '12dp'

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:
                                                id: spamflag

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
                                                id: spamread

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
                                                id: inboxnoaction

                                            MDLabel:
                                                text: "No Action"
                                                font_size: '12dp'

                                    MDBoxLayout:
                                        orientation: 'vertical'

                                        MDGridLayout:
                                            cols: 2

                                            MDCheckbox:
                                                id: inboxflag

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
                                                id: inboxpin

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
                                hint_text: "Email ID (Required); Password(required); Proxy IP:Port"
                                required: True
                                multiline: True
                                size_hint: 0.4, None
                                height: "80dp"
                                pos_hint: {'center_x': 0.2}

                            Widget:

                        MDGridLayout:
                            cols: 2
                            size_hint_y: None
                            height: '80dp'
                            spacing: 20

                            MDRaisedButton:
                                text: "Start"
                                text_color: 0, 0, 0, 1
                                md_bg_color: 0, 0, 1, 1
                                on_release: root.start()

                            MDRaisedButton:
                                text: "Stop"
                                text_color: 0, 0, 0, 1
                                md_bg_color: 1, 0, 0, 1
            
'''

class SocksIMAP4(IMAP4):
    """
    IMAP service trough SOCKS proxy. PySocks module required.
    """

    PROXY_TYPES = {"socks4": PROXY_TYPE_SOCKS4,
                   "socks5": PROXY_TYPE_SOCKS5,
                   "http": PROXY_TYPE_HTTP}

    def __init__(self, host, port=IMAP4_PORT, proxy_addr=None, proxy_port=None,
                 rdns=True, username=None, password=None, proxy_type="socks5"):

        self.proxy_addr = proxy_addr
        self.proxy_port = proxy_port
        self.rdns = rdns
        self.username = username
        self.password = password
        self.proxy_type = SocksIMAP4.PROXY_TYPES[proxy_type.lower()]

        IMAP4.__init__(self, host, port)

    def _create_socket(self):
        return create_connection((self.host, self.port), proxy_type=self.proxy_type, proxy_addr=self.proxy_addr,
                                 proxy_port=self.proxy_port, proxy_rdns=self.rdns, proxy_username=self.username,
                                 proxy_password=self.password)


class SocksIMAP4SSL(SocksIMAP4):

    def __init__(self, host='', port=IMAP4_SSL_PORT, keyfile=None, certfile=None, ssl_context=None, proxy_addr=None,
                 proxy_port=None, rdns=True, username=None, password=None, proxy_type="socks5"):

        if ssl_context is not None and keyfile is not None:
                raise ValueError("ssl_context and keyfile arguments are mutually "
                                 "exclusive")
        if ssl_context is not None and certfile is not None:
            raise ValueError("ssl_context and certfile arguments are mutually "
                             "exclusive")

        self.keyfile = keyfile
        self.certfile = certfile
        if ssl_context is None:
            ssl_context = ssl._create_stdlib_context(certfile=certfile,
                                                     keyfile=keyfile)
        self.ssl_context = ssl_context

        SocksIMAP4.__init__(self, host, port, proxy_addr=proxy_addr, proxy_port=proxy_port,
                            rdns=rdns, username=username, password=password, proxy_type=proxy_type)

    def _create_socket(self):
        sock = SocksIMAP4._create_socket(self)
        server_hostname = self.host if ssl.HAS_SNI else None
        return self.ssl_context.wrap_socket(sock, server_hostname=server_hostname)

    def open(self, host='', port=IMAP4_PORT):
        SocksIMAP4.open(self, host, port)

class BrowserModeScreen(Screen):

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

                                if self.spamnoaction.active:

                                    submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[4]/button/span').click()
                                    sleep(4)

                                    press('enter')
                                    sleep(2)
                                    continue

                                elif self.spamread.active and self.spamflag.active:
                                    submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[9]/button').click()
                                    sleep(4)

                                    for _ in range(2):
                                        press('down')
                                    press('enter')
                                    sleep(3)

                                    submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[4]/button/span').click()
                                    sleep(4)

                                    for _ in range(3):
                                        press('down')
                                    press('enter')
                                    sleep(3)
                                    
                                    submit = driver.find_element_by_xpath(f'//*[@id="ReadingPaneContainerId"]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/span[2]').click()
                                    sleep(4)

                                    press('enter')
                                    sleep(2)
                                    continue

                                elif self.spamread.active:
                                    
                                    submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[9]/button').click()
                                    sleep(4)

                                    for _ in range(2):
                                        press('down')
                                    press('enter')
                                    sleep(3)
                                    
                                    submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[4]/button/span').click()
                                    sleep(4)

                                    press('enter')
                                    sleep(2)
                                    continue

                                elif self.spamflag.active:
                                    
                                    submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[9]/button').click()
                                    sleep(4)

                                    for _ in range(3):
                                        press('down')
                                    press('enter')
                                    sleep(3)
                                    
                                    submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[4]/button/span').click()
                                    sleep(4)

                                    press('enter')
                                    sleep(2)
                                    continue

                                else:
                                    submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[4]/button/span').click()
                                    sleep(4)

                                    press('enter')
                                    sleep(2)
                                    continue

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

                                if self.spamnoaction.active:

                                    submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[4]/button/span').click()
                                    sleep(4)

                                    press('enter')
                                    sleep(2)
                                    continue

                                elif self.spamread.active and self.spamflag.active:
                                    submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[9]/button').click()
                                    sleep(4)

                                    for _ in range(2):
                                        press('down')
                                    press('enter')
                                    sleep(3)

                                    submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[4]/button/span').click()
                                    sleep(4)

                                    for _ in range(3):
                                        press('down')
                                    press('enter')
                                    sleep(3)
                                    
                                    submit = driver.find_element_by_xpath(f'//*[@id="ReadingPaneContainerId"]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/span[2]').click()
                                    sleep(4)

                                    press('enter')
                                    sleep(2)
                                    continue

                                elif self.spamread.active:
                                    
                                    submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[9]/button').click()
                                    sleep(4)

                                    for _ in range(2):
                                        press('down')
                                    press('enter')
                                    sleep(3)
                                    
                                    submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[4]/button/span').click()
                                    sleep(4)

                                    press('enter')
                                    sleep(2)
                                    continue

                                elif self.spamflag.active:
                                    
                                    submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[9]/button').click()
                                    sleep(4)

                                    for _ in range(3):
                                        press('down')
                                    press('enter')
                                    sleep(3)
                                    
                                    submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[4]/button/span').click()
                                    sleep(4)

                                    press('enter')
                                    sleep(2)
                                    continue

                                else:
                                    submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[4]/button/span').click()
                                    sleep(4)

                                    press('enter')
                                    sleep(2)
                                    continue

                            except Exception as e:
                                print(e)
                                break                    

            elif self.inbox.active:
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

                    driver.get('https://outlook.live.com/mail/0/')
                    sleep(5)

                    while True:

                        try:

                            submit = driver.find_element_by_xpath("//div[@role='option']").click()
                            sleep(4)

                            if self.inboxnoaction.active:

                                submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[5]/button/span/i[2]').click()
                                sleep(2)
                            
                                press('down')
                                press('enter')
                                sleep(2)

                            elif self.inboxflag.active and self.inboxpin.active:

                                submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[9]/button/span').click()
                                sleep(4)

                                for _ in range(4):
                                    press('down')
                                press('enter')
                                sleep(2)

                                submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[9]/button/span').click()
                                sleep(4)

                                for _ in range(5):
                                    press('down')
                                press('enter')
                                sleep(3)

                                submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[5]/button/span/i[2]').click()
                                sleep(2)
                            
                                press('down')
                                press('enter')
                                sleep(2)

                            elif self.inboxflag.active:

                                submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[9]/button/span').click()
                                sleep(4)

                                for _ in range(4):
                                    press('down')
                                press('enter')
                                sleep(3)

                                submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[5]/button/span/i[2]').click()
                                sleep(2)
                            
                                press('down')
                                press('enter')
                                sleep(2)

                            elif self.inboxpin.active:

                                submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[9]/button/span').click()
                                sleep(4)

                                for _ in range(5):
                                    press('down')
                                press('enter')
                                sleep(3)

                                submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[5]/button/span/i[2]').click()
                                sleep(2)
                            
                                press('down')
                                press('enter')
                                sleep(2)

                            else:
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

                            if self.inboxnoaction.active:

                                submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[5]/button/span/i[2]').click()
                                sleep(2)
                            
                                press('down')
                                press('enter')
                                sleep(2)

                            elif self.inboxflag.active and self.inboxpin.active:

                                submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[9]/button/span').click()
                                sleep(4)

                                for _ in range(4):
                                    press('down')
                                press('enter')
                                sleep(2)

                                submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[9]/button/span').click()
                                sleep(4)

                                for _ in range(5):
                                    press('down')
                                press('enter')
                                sleep(3)

                                submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[5]/button/span/i[2]').click()
                                sleep(2)
                            
                                press('down')
                                press('enter')
                                sleep(2)

                            elif self.inboxflag.active:

                                submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[9]/button/span').click()
                                sleep(4)

                                for _ in range(4):
                                    press('down')
                                press('enter')
                                sleep(3)

                                submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[5]/button/span/i[2]').click()
                                sleep(2)
                            
                                press('down')
                                press('enter')
                                sleep(2)

                            elif self.inboxpin.active:

                                submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[9]/button/span').click()
                                sleep(4)

                                for _ in range(5):
                                    press('down')
                                press('enter')
                                sleep(3)

                                submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[5]/button/span/i[2]').click()
                                sleep(2)
                            
                                press('down')
                                press('enter')
                                sleep(2)

                            else:
                                submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[5]/button/span/i[2]').click()
                                sleep(2)
                            
                                press('down')
                                press('enter')
                                sleep(2)

                        except Exception as e:
                            print(e)
                            break

    def start(self):
        data_list = [tuple(x.split(',')) for x in self.data.text.split('\n')]
        win_sequence =[]
        win_n = int(self.win.text.strip())

        data_list_iter = iter(data_list)
        win_sequence = [list(islice(data_list_iter, enum)) for enum in [len(data_list)//win_n,]*(win_n+1)]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self.winGenerator, win_sequence)

class IMAPModeScreen(Screen):

    def IMAPStarter(self, win):

        for row in win:

            if self.spam.active:

                if len(row)==2:

                    con = IMAP4_SSL(outlook_imap_url)
                    user, password = row[0], row[1]
                    con.login(user, password)
                    con.select('Junk')

                    try:
                        result, data = con.uid('search', None, "ALL")
                        uidList = data[0].split()

                        for uid in uidList:
                            con.uid('COPY', uid, 'Inbox')
                            con.uid('STORE',uid, '+FLAGS', '(\\Deleted)')
                    except Exception as e:
                        print(e)

                elif len(row)>=3:

                    user, password, proxy_ip = row[0], row[1], row[2].split(':')

                    imap_server = outlook_imap_url
                    imap_port = 993

                    proxy_addr = proxy_ip[0]
                    proxy_port = proxy_ip[1]
                    proxy_type = "socks5"

                    con = SocksIMAP4SSL(host=imap_server, port=imap_port,
                                            proxy_addr=proxy_addr, proxy_port=proxy_port, proxy_type=proxy_type)
                                            
                    con.login(user, password)

                    con.select('Junk')

                    result, data = con.uid('search', None, "ALL")
                    uidList = data[0].split()

                    for uid in uidList:
                        con.uid('COPY', uid, 'Inbox')
                        con.uid('STORE',uid, '+FLAGS', '(\\Deleted)')

            elif self.inbox.active:

                if len(row)==2:

                    con = IMAP4_SSL(outlook_imap_url)
                    user, password = row[0], row[1]
                    con.login(user, password)
                    con.select('Inbox')

                    try:
                        result, data = con.uid('search', None, "ALL")
                        uidList = data[0].split()

                        for uid in uidList:
                            con.uid('COPY', uid, 'Junk')
                            con.uid('STORE',uid, '+FLAGS', '(\\Deleted)')
                    except Exception as e:
                        print(e)
                        
                elif len(row)>=3:

                    user, password, proxy_ip = row[0], row[1], row[2].split(':')

                    imap_server = outlook_imap_url
                    imap_port = 993

                    proxy_addr = proxy_ip[0]
                    proxy_port = proxy_ip[1]
                    proxy_type = "socks5"

                    con = SocksIMAP4SSL(host=imap_server, port=imap_port,
                                            proxy_addr=proxy_addr, proxy_port=proxy_port, proxy_type=proxy_type)
                                            
                    con.login(user, password)

                    con.select('Inbox')

                    result, data = con.uid('search', None, "ALL")
                    uidList = data[0].split()

                    for uid in uidList:
                        con.uid('COPY', uid, 'Junk')
                        con.uid('STORE',uid, '+FLAGS', '(\\Deleted)')
    
    def start(self):
        data_list = [tuple(x.split(',')) for x in self.data.text.split('\n')]
        win_sequence =[]
        win_n = 1

        data_list_iter = iter(data_list)
        win_sequence = [list(islice(data_list_iter, enum)) for enum in [len(data_list)//win_n,]*(win_n+1)]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self.IMAPStarter, win_sequence)


sm = ScreenManager()
sm.add_widget(BrowserModeScreen(name = 'brws'))
sm.add_widget(IMAPModeScreen(name = 'imap'))

class MailManagerApp(MDApp):

    def build(self):
        self.theme_cls = ThemeManager()
		#self.icon="a_icon.png"
        self.theme_cls.primary_palette='DeepPurple'
        self.theme_cls.primary_hue='900'
        self.screen=Builder.load_string(code)
        return self.screen

MailManagerApp().run()