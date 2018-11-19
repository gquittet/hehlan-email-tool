# HEH LAN: EMail tool

A tool to send emails for the HEH LAN.

## Dependencies

- Python3 [https://www.python.org/](https://www.python.org/)
- virtualenv [https://virtualenv.pypa.io/en/latest/installation/](https://virtualenv.pypa.io/en/latest/installation/)

If you use Linux, use your package manager like DNF, APT, Pacman, emerge, XBPS and so on.

## How to use

1. Clone the repository: `git clone https://github.com/gquittet/hehlan-email-tool.git`
2. Create a virtual environment with python 3: `virtualenv3 hehlan-email-tool` or `virtualenv hehlan-email-tool`
3. Enable the environment with `. bin/activate` and desactivate it with `deactivate`.
4. Install the requirements : `pip install -r requirements.txt`
5. Download the emails as CSV and put the file in the folder.
6. Edit the variables inside the **config.xml** file.
7. Run the `send_mail.py` script.

> The steps 1, 2 and 4 are only required by the installation process.

