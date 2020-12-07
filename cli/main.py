"""A simple program to encode and decode files. With speed in mind, it's made to be fast.

"""

#Imported modules
import argparse
from tqdm import tqdm
from os import path
import base64
import win32clipboard
import pyperclip
#==========================
__version__ = '0.0. 1 Beta'


#=============================
#Functions
#=============================
def isbase64(text):
    #This function checks to see if a file is in base64 or not
    try:
        text = text.join(text.split())
        base64.b64decode(text, validate = True)
        return True
    except UnicodeDecodeError:
        return False
    except:
        return False
def data_from_clipboard():
    #This functions tries to retrieve data from the clipboard
    #It tries copying text, on error,
    #It returns a file path
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return [data, 'string'] #The string part unables the program to know its not a file path
    except:
        #If the clipboard data is no text, TypeError occures.
        #This will return a path
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData(win32clipboard.CF_HDROP)
        win32clipboard.CloseClipboard()
        return [data[0], 'path']


def check_path(file_path):
    if path.exists(file_path) == True:
        if path.isdir(file_path) == True:
            print('Cannot convert a folder to base64')
            return False
        else:
            return True
    else:

        print('Path does not exist')
        return False


def encode():
    #This is the function for encoding the application
    if file_path:
        if check_path(file_path) == True:
            try:
                with open(file_path) as file:
                    contents = file.read().encode()
                encoded = base64.b64encode(contents).decode()
                if display:
                    if binary:
                        print(encoded.encode())
                    else:
                        print(encoded)
                if not clipboard:
                    pyperclip.copy(encoded)
            except UnicodeDecodeError:
                with open(file_path, 'rb') as file:
                    contents = file.read()
                encoded = base64.b64encode(contents).decode()
                if display:
                    if binary:
                        print(encoded.encode())
                    else:
                        print(encoded)
                if not clipboard:
                    pyperclip.copy(encoded)
    elif not file_path: #If the user does not include the argument '-f or --file', it reads from clipboard
        if data_from_clipboard()[1] == 'path':
            if check_path(data_from_clipboard()[0]) == True:
                try:
                    with open(data_from_clipboard()[0]) as file:
                        contents = file.read().encode()
                    encoded = base64.b64encode(contents).decode()
                    if display:
                        if binary:
                            print(encoded.encode())
                        else:
                            print(encoded)
                    if not clipboard:
                        pyperclip.copy(encoded)
                except UnicodeDecodeError:
                    with open(data_from_clipboard()[0], 'rb') as file:
                        contents = file.read()
                    encoded = base64.b64encode(contents).decode()
                    if display:
                        if binary:
                            print(encoded.encode())
                        print(encoded)
                    if not clipboard:
                        pyperclip.copy(encoded)
        else:
            #If the data copied on the clipboard is not a file path,
            #It treats it as ordinary text and encodes it.
            contents = data_from_clipboard()[0]
            if contents == '\r\n':
                print('Clipboard is empty')
                quit()
            contents = contents.encode()
            encoded = base64.b64encode(contents).decode()
            if display:
                if not clipboard:
                    pyperclip.copy(encoded)
                if binary:
                    print(encoded.encode())
                else:
                    print(encoded)
            if not clipboard:
                pyperclip.copy(encoded)

def decode():
    if file_path:
        if check_path(file_path) == True:
            try:
                with open(file_path, 'r') as file:
                    contents = file.read()
                    if isbase64(contents) == True:
                        decoded = base64.b64decode(contents)
                        if display:
                            if binary:
                                if output:
                                    with open(output, 'wb') as file:
                                        file.write(decoded)
                            else:
                                print(decoded)
                            if output:
                                with open(output, 'w') as file:
                                    file.write(decoded.decode())
                        if not clipboard:
                            pyperclip.copy(str(decoded))
                        if output:
                            with open(output, 'w') as file:
                                file.write(decoded.decode())
                    else:
                        print('Not base64')
            except UnicodeDecodeError:
                with open(file_path, 'rb') as file:
                    contents = file.read()
                if isbase64(contents) == True:
                    decoded = base64.b64decode(contents)
                    if display:
                        if binary:
                            print(decoded)
                            if output:
                                with open(output, 'wb') as file:
                                    file.write(decoded)
                        else:
                            if output:
                                with open(output, 'w') as file:
                                    file.write(decoded.decode())
                            print(decoded)
                else:
                    print('Not base64')
    elif not file_path:
        if data_from_clipboard()[1] == 'path':
            if check_path(data_from_clipboard()[0]) == True:
                try:
                    with open(data_from_clipboard()[0], 'r') as file:
                        contents = file.read()
                    if isbase64(contents) == True:
                        decoded = base64.b64decode(contents)
                        if display:
                            if binary:
                                print(binary.encode())
                            else:
                                print(decoded)
                    else:
                        print('Not base64')
                except UnicodeDecodeError:
                    with open(data_from_clipboard()[0], 'rb') as file:
                        contents = file.read()
                    if isbase64(contents.decode()) == True:
                        decoded = base64.b64decode(contents)
                        if display:
                            print(decoded)
                        if not clipboard:
                            pyperclip.copy(decoded)
            else:
                print('File not found')
        else:
            if isbase64(data_from_clipboard()[0]) == True:
                decoded = base64.b64decode(data_from_clipboard()[0])
                if display: 
                    print(decoded)
                if not clipboard:
                    pyperclip.copy(decoded.decode())     
            else:
                print('Not base64')


#====================================================
parser = argparse.ArgumentParser(prog = 'qb', description = 'Quick Base64', epilog = 'Easily encode and decode files in seconds.')
parser.add_argument('-v', '--version', action = 'version', help = 'Show current version.', version = '0.0.1 Beta')
parser.add_argument('-f', '--file', action = 'store', help = 'Provide path to the file', dest = 'file')
parser.add_argument('-d', '--display', action = 'store_true', help = 'To display the contents on the screen.', dest = 'display')
parser.add_argument('-o', '--output', action = 'store', help = 'Write the contents to a file', dest = 'output')
parser.add_argument('-b', '--binary', action = 'store_true', help = 'Display output in binary format.')
parser.add_argument('-nc', '--no-clipboard', action = 'store_true', help = 'The program will not send the results to system clipboard', dest = 'clipboard')
subparsers = parser.add_subparsers(title = 'Sub commands',dest = 'subparser_name')
#====================================================

#Decode is a subparser and it kinda have it's own commands
parser_decode = subparsers.add_parser('decode', help = 'Decode function of Quick Base64')
parser_decode.add_argument('-f', '--file', action = 'store', help = 'Provide path to a file containing base64 contents', dest = 'file')
parser_decode.add_argument('-d', '--display', action = 'store_true', help = 'Display contents to the screen.')
parser_decode.add_argument('-b', '--binary', action = 'store_true', help = 'Ouput should be in binary format', dest = 'binary')
parser_decode.add_argument('-nc', '--no-clipboard', action = 'store_true', help = 'The program will not send the results to system clipboard', dest = 'clipboard')
parser_decode.add_argument('-o', '--output', action = 'store', help = 'Write contents to a file.')
#=======================================
arguments = parser.parse_args()


#=========================
file_path = arguments.file
display = arguments.display
binary = arguments.binary
clipboard = arguments.clipboard
output = arguments.output
def main():
    if arguments.subparser_name == 'decode':
        decode()
    else:
        encode()

if __name__ == '__main__':
    main()