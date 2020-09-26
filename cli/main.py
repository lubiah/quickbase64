"""A simple program to encode and decode files. With speed in mind, it's made to be fast.

"""

#Imported modules
import argparse
from tqdm import tqdm
from os import path
import base64
import win32clipboard
#=========
__version__ = '0.0. 1 Beta'


#=========================
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
    except TypeError:
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
                if write:
                    print(encoded)
            except UnicodeDecodeError:
                with open(file_path, 'rb') as file:
                    contents = file.read()
                encoded = base64.b64encode(contents).decode()
                if write:
                    if binary:
                        print(encoded.encode())
                    else:
                        print(encoded)
    elif not file_path: #If the user does not include the argument '-f or --file', it reads from clipboard
        if data_from_clipboard()[1] == 'path':
            if check_path(data_from_clipboard()[0]) == True:
                try:
                    with open(data_from_clipboard()[0]) as file:
                        contents = file.read().encode()
                    encoded = base64.b64encode(contents).decode()
                    if write:
                        print(encoded)
                except UnicodeDecodeError:
                    with open(data_from_clipboard()[0], 'rb') as file:
                        contents = file.read()
                    encoded = base64.b64encode(contents).decode()
                    if write:
                        print(encoded)

        else:
            #If the data copied on the clipboard is not a file path,
            #It treats it as ordinary text and encodes it.
            contents = data_from_clipboard()[0].encode()
            encoded = base64.b64encode(contents).decode()
            if write:
                print(encoded)


def decode():
    if file_path:
        if check_path(file_path) == True:
            try:
                with open(file_path, 'r') as file:
                    contents = file.read()
                    if isbase64(contents) == True:
                        decoded = base64.b64decode(contents)
                        if write:
                            if binary:
                                print(decoded.encode())
                            else:
                                print(decoded)
                    else:
                        print('Not base64')
            except UnicodeDecodeError:
                with open(file_path, 'rb') as file:
                    contents = file.read()
                if isbase64(contents) == True:
                    decoded = base64.b64decode(contents.encode())
                    if write:
                        if binary:
                            print(decoded.encode())
                        else:
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
                        if write:
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
                        if write:
                            print(decoded)
            else:
                print('File not found')
        else:
            if isbase64(data_from_clipboard()[0]) == True:
                decoded = base64.b64decode(data_from_clipboard()[0]).decode()
                if write:
                    print(decoded)       
            else:
                print('Not base64')

def decode_function(*args):
    print(args)

#====================================================
parser = argparse.ArgumentParser(prog = 'qb64', description = 'Quick Base64', epilog = 'Easily encode and decode files in seconds.')
parser.add_argument('-v', '--version', action = 'store_true', help = 'Show current version.', dest = 'version')
parser.add_argument('-f', '--file', action = 'store', help = 'Provide path to the file', dest = 'file')
parser.add_argument('-w', '--write', action = 'store_true', help = 'To write output to a file, include this.', dest = 'write')
parser.add_argument('-b', '--binary', action = 'store_true', help = 'Display output in binary format.')
subparsers = parser.add_subparsers(title = 'Sub commands',dest = 'subparser_name', metavar = 'command')
#====================================================

#Decode is a subparser and it kinda have it's own commands
parser_decode = subparsers.add_parser('decode')
parser_decode.add_argument('-f', '--file', action = 'store', help = 'Provide path to a file containing base64 contents', dest = 'file')
parser_decode.add_argument('-w', '--write', action = 'store_true', help = 'Write results to a file.')
parser_decode.add_argument('-b', '--binary', action = 'store_true', help = 'Ouput should be displayed in binary format', dest = 'binary')
#=======================================
arguments = parser.parse_args()
#arguments = parser.parse_args(['decode'])


#=========================
version = arguments.version
file_path = arguments.file
write = arguments.write

def main():
    if version:
        print(__version__)
    elif arguments.subparser_name == 'decode':
        decode()
    else:
        encode()

if __name__ == '__main__':
    main()