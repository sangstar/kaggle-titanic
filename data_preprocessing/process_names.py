import re

def clean_names(dat):
    new_names = []
    for names in dat['Name']:
        to_add = ""
        for splits in names.split(" "):
            to_add += re.sub(r'[^\w]', '', splits) + " "
        new_names.append(to_add[:-1])
    return new_names

def check_for_missing_honorifics(cleaned_names, honorifics):
    for names in cleaned_names:
        to_look_for_honorific = names.split(" ")
        if all([words not in honorifics for words in to_look_for_honorific]):
            print(to_look_for_honorific)