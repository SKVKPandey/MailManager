# MailManager

Mail Manager is an application for automating mail functions. The application can open multiple browser window with given Proxy IPs. The front-end has been developed by using Kivy and KivyMD, while the back-end is Selenium based and contains PyAutoGUI for extra support.

## Technologies Used
- Kivy (Version==2.0.0)
- KivyMD (Version==1.0.0)
- Selenium (Version==3.141.0)
- PyAutoGUI (Version==0.9.53)
- Python (Version==3.6.8)

## About Project

- The repository contains the following folders and file: `Drivers`, `.gitignore`, and `main.py`.
- `Drivers` folder currently contains the Chrome driver (Version==103.0.5060.24). If the driver is not working then check: https://chromedriver.chromium.org/downloads for new versions of driver and replace the previous one in the `Drivers` folder.
- `main.py` is the file containing 

## Run Locally

Clone the project

```bash
  git clone https://github.com/SKVKPandey/MailManager.git
```

Go to the project directory

```bash
  cd MailManager
```

Install virtual environment

```bash
  virtualenv venv
```

Activate the virtual environment (for Git Bash given below and for other terminals check out this link: https://docs.python.org/3/library/venv.html). 

```bash
  source venv/Scripts/activate
```
Install dependencies
```bash
  pip install selenium
```
```bash
  pip install PyAutoGUI
```
```bash
  pip install Pillow
```
```bash
  pip install kivy
```
Install KivyMD (For more info check the official documentation of KivyMD here: https://github.com/kivymd/KivyMD)
```bash
  git clone https://github.com/kivymd/KivyMD.git --depth 1
  cd KivyMD
  pip install .
```
After installation go back to the MailManager directory and run `main.py` file.
```bash
  cd ..
  main.py
```


## Author

[@SKVKPandey](https://github.com/SKVKPandey)



