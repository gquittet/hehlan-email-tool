import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import yaml


class EMailSpammer(object):

    def __init__(self, firstname, name, grade, email, password, lang='en'):
        with open("config.yml", 'r') as stream:
            try:
                self.__config = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        host = self.__config['SMTP']['HOST']
        port = self.__config['SMTP']['PORT']
        self.__sender = {'lastname': name.upper(), 'firstname': firstname[0].upper(
        ) + firstname[1:].lower(), 'grade': grade, 'email': email}
        self.__connection = smtplib.SMTP(host, port)
        self.__connection.ehlo()
        self.__connection.starttls()
        self.__connection.login(email, password)

        self.__msg = MIMEMultipart('alternative')
        self.__msg['From'] = email
        self.__attach_the_pdf('fr')
        self.__attach_html_to_msg("%s%s" % (self.__config['EMAIL'][lang.upper(
        )]['MAIL']['PATH'], self.__config['EMAIL'][lang.upper()]['MAIL']['FILENAME']))

    def __attach_the_pdf(self, lang):
        variables = self.__config['EMAIL'][lang.upper()]
        self.__msg['Subject'] = variables['SUBJECT']
        for attach in variables['ATTACHEMENTS']['FILENAMES']:
            self.__attach_pdf_to_msg(
                variables['ATTACHEMENTS']['PATH'], attach)

    def __attach_pdf_to_msg(self, place, filename):
        fo = open(place + filename, 'rb')
        attach = MIMEApplication(fo.read(), _subtype="pdf")
        fo.close()
        attach.add_header('Content-Disposition',
                          'attachment', filename=filename)
        self.__msg.attach(attach)

    def __attach_html_to_msg(self, filename):
        fo = open(filename, 'r')
        filedata = fo.read()
        for i in self.__config['VARIABLES']['HTML']:
            html_variable = self.__config['VARIABLES']['HTML'][i]
            code_variable = self.__sender[self.__config['VARIABLES']['CODE'][i]]
            filedata = filedata.replace(html_variable, code_variable)
        attach = MIMEText(filedata, 'html')
        fo.close()
        self.__msg.attach(attach)

    def send_mail(self, to):
        """
        Send the mail to the recipient.
        :to The address that will receive the email
        """
        self.__msg['To'] = to
        self.__connection.sendmail(
            self.__sender['email'], to, self.__msg.as_string())

    def close_connection(self):
        """
        Close the current connection.
        """
        self.__connection.quit()
