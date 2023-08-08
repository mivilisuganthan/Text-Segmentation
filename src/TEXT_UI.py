from text_recognition import text_recognition, ias
import string
import argparse

#When entering a folder path, ensure to remove any surrounding quotation marks
lang = []
code = []
lang_list = []
key_list = ['code', 'lang', 'x', 'x', 'x','x','x']
infile = open('lang_codes.csv')
for languages in infile:
    dictionary = {}
    languages = languages.strip().split(',')
    for n in range(len(key_list)):
        if key_list[n] == 'lang' or key_list[n] == 'code':
            dictionary[key_list[n]] = languages[n]
    lang_list.append(dictionary)  
string = ''
for x in lang_list:
    string += x['code'] + '\t\t' + x['lang'] + '\n'



        
        
parse = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)
parse.add_argument("-c", "--Command", help='Enter \'d\' or \'i\' to draw boxes or write ias files respectively')
parse.add_argument("-p", "--Path", help='Enter the path of the folder')
parse.add_argument("-l", "--Language", help='Enter the language present in the files.\nThe supported languages and their respective three letter codes can be found below:\n\n' + string)
arg = parse.parse_args()

if arg.Command and arg.Path:
    if arg.Command == 'd':
        x = text_recognition(arg.Path)
    elif arg.Command == 'i':
        if arg.Language:
            x = ias(arg.Path, arg.Language)
else:
    counter = 1
    while counter > 0:
        command = input('\nHi there, to begin please enter a command\n\tD)raw Boxes\n\tI)as Files\n\tE)xit\n\nEnter Command: ')
        while command.upper() != 'D' and command.upper() != 'I' and command.upper() != 'E':
            command = input('Invalid command. Please enter a valid command: ')
        if command.upper() == 'D':
            while counter > 0:
                c = input('\nPlease enter the path of the folder to be loaded.\nFolder PATH: ')
                output = text_recognition(c)
                prompt = input('\nWould you like to load another folder? ')
                prompt = prompt.upper()
                while prompt != 'YES' and prompt != 'Y' and prompt != 'NO' and prompt != 'N':
                    prompt = input('Invalid response. Please enter \'Yes\' or \'No\': ')
                    prompt = prompt.upper()
                if prompt == 'NO' or prompt == 'N':
                    break

        if command.upper() == 'I':
            while counter > 0:
                i = input('\nPlease enter the path of the folder to be loaded.\nFolder PATH: ')
                lang = input('Please enter the language present within the files: ')
                output = ias(i, lang)
                print('ias files loaded')
                another_prompt = input('Would you like to load another folder? ')
                another_prompt = another_prompt.upper()
                while another_prompt != 'YES' and another_prompt != 'Y' and another_prompt != 'NO' and another_prompt != 'N':
                    another_prompt = input('Invalid response. Please enter \'Yes\' or \'No\': ')
                    another_prompt = another_prompt.upper()
                if another_prompt == 'NO' or another_prompt == 'N':
                    break

        if command.upper() == 'E':
            print('Goodbye!')
            break



