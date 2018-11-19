# HEH LAN: EMail tool

A tool to send emails for the HEH LAN.

## Dependencies

- Python3 [https://www.python.org/](https://www.python.org/)
- virtualenv [https://virtualenv.pypa.io/en/latest/installation/](https://virtualenv.pypa.io/en/latest/installation/)

If you use Linux, use your package manager like DNF, APT, Pacman, emerge, XBPS and so on.

## How to use

1. Create a virtual environment with python 3: `virtualenv3 hehlan-email-tool` or `virtualenv hehlan-email-tool`
2. Go inside the folder that was created and clone this repository inside it: `git clone https://github.com/gquittet/hehlan-email-tool .`
3. Install the requirements : `pip install -r requirements.txt`
4. Download the emails as CSV and put the file in the folder.
5. Edit the variables inside the **config.xml** file.
6. Run the `send_mail.py` script.
