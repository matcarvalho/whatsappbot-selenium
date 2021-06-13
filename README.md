# Whatsappbot-selenium

## Getting Started
#### Dependencies
You need Python 3.7 or later to use **pacotepypi**. You can find it at [python.org](https://www.python.org/).
You also need setuptools, wheel and twine packages, which is available from [PyPI](https://pypi.org). If you have pip, just run:
```
pip install selenium
pip install webdriver-manager
```
#### Installation
Clone this repo to your local machine using:
```
git clone https://github.com/matcarvalho/whatsappbot-selenium.git
```
## Functions
- Send Menssage with Selenium by Whatsapp
  - Parameters: Contact  (Name the person or Group) and message
- Delete Menssage with Selenium by Whatsapp
  - Parameters: Contact (Name the person or Group)

## Example

import Whatsappbot

test = Whatsappbot()
test.send_message("Lucas","Hi, your tracking code is 12312")
test.delete_message("Lucas") -> Will delete the last message
