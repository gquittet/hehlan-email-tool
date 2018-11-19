import csv
import re

import yaml
from emailSpammer import EMailSpammer

with open("config.yml", 'r') as stream:
    try:
        config = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

annee = 'Master 0' if config['ETUDIANT']['PASSERELLE'] else 'BA3'

es = EMailSpammer(config['ETUDIANT']['PRENOM'], config['ETUDIANT']['NOM'], annee,
                  config['ETUDIANT']['EMAIL'], config['ETUDIANT']['MOT_DE_PASSE'], config['LANGUE'])

regex_isEmail = re.compile(
    r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
regex_isBeOrFr = re.compile(
    r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.(fr|be)$")

filename = "%s.%s" % (config['FICHIER']['NOM'],
                      config['FICHIER']['EXTENSION'].lower())
with open(filename, 'r') as csvfile:
    emails = []
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for text in spamreader:
        if (text[-2] == 'FALSE'):
            filter_result = list(filter(regex_isEmail.search, text))
            if (len(filter_result) > 0 and config['LANGUE'].upper() == text[-3].upper()):
                emails.append(filter_result[0])
    for email in emails:
        print(email)
        es.send_mail(email)
es.close_connection()
