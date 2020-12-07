"""
This is the GUI version of Quick Base64. It allows you to encode files and text into base64 format.
==================================================
__author__ = 'Lucretius'
__mail__ = 'lucretiusbiah@protonmail.com'
==================================================
"""
#icon_binary
icon_data = '''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'''

#Imported  modules
#====================================
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import *
from tkinter.filedialog import *
from ttkwidgets import linklabel
from ttkwidgets import debugwindow
from TkinterDnD2 import *
import os
import pybase64
import pathlib
from os import path
from subprocess import Popen, PIPE
from os.path import getsize, splitext, realpath
import tempfile
from configparser import ConfigParser
import sys
import pyperclip
import win32clipboard
#=====================================
#Code
#=======================================
root = TkinterDnD.Tk()
root.iconphoto(True,PhotoImage(data = icon_data))
root.title('Quick Base64')
menubar = Menu(root)
#========================
#Variables
save_extension = None #This refers to the extension that the file will be saved in.
mode_variable = StringVar()
status_variable = StringVar() #This is responsible for setting the status of the status bar
auto_detect_variable = IntVar()
details_variable = StringVar()
temp_file_name = ''
drop_type = None #In saving, this checks whether a file or text was dropped
temp_files = [] #This is an array which contains a list of temporary files created.
checked = False #This is used in auto-detect mode to check if a files mode has been detected.
file_path = ''
#=====================================================================================
# Constants
PICTURES = ['.jpg','.jif','jfif','.jpe', '.png', '.ico', '.jpeg','.gif', '.tiff','.vda','.vst','.tif','.icb','.icns','.webp', '.ppm','.pgm', '.pnm', '.pbm', '.tga', '.pcx', '.jp2','.j2k', '.jpf','jpx','jpm','mj2', 'raw', 'bmp', 'xpm']
AUDIOS = ['.mp3','.m4r', '.wav','.m4p','m4a', '.pcm','.aiff','.aif', '.aac', '.ogg', '.wma', '.flac', '.alac','.aifc', '.3ga', '.aa','.act', '.al','.bap','.cda','.mp2','.mpa','.oga']
VIDEOS = ['.mp4','.m4b','.avi','.qt','.mov','.wmv','.flv','.avchd','.webm','.mkv','.ogv','.dirac', '.mpg', '.mpeg','.3gp','.nsv','.3g2','.svi','.m4v']
#=====================================================================================
configurations = {
    'default_mode':'encode',
    'sys_argv_mode': None,
    'output_dir' : 'output',
    'temp_dir' : tempfile.gettempdir()
    } #The default settings for configuration
#======================================
#Functions and classes
#===========================================
class Menubar:
    def __init__(self, menubar):
        self.menubar = menubar
        Menubar.main(self)
        
        
    def show_debug():
        def show():
            global debug_window
            debug_window = debugwindow.DebugWindow(stdout = True, stderr = True)
        try:
            if debug_window.state() == 'normal' or debug_window.state() == 'iconic':
                debug_window.destroy()
        except:
            show()

    def about(self):
        def show():
            global about_menu
            about_menu = Toplevel()
            about_menu.resizable(False, False)
            about_menu.title("About")
            heading = Label(about_menu, text = "Quick Base64", font = ('Calibri', 20, 'bold', 'italic'), fg = 'green',justify = 'center').grid(row = 0, column = 0, sticky = W+E)
            text_label = Label(about_menu, text = '''An open-source base64 file encoder which can encode your files to base64 format.\nIt can also decode your base64 text to it\'s original file.''', font = ('Calibri', 13)).grid(row = 1, column = 0)
            site_link = linklabel.LinkLabel(about_menu, text = 'Website: https://www.eakloe.com/quickbase64', font = ('Calibri', 13), link = 'https://www.eakloe.com/quickbase64', cursor = 'hand2').grid(row = 2, column = 0)
            code_link = linklabel.LinkLabel(about_menu, text = 'Source code: https://www.github.com/biah/quickbase64', font = ('Calibri', 13), link = 'https://www.github.com/biah/quickbase64', cursor = 'hand2').grid(row = 3, column = 0)
            version_label = Label(about_menu, text = 'Version : 0.1.1',font = ('Calibri', 15)).grid(row = 4, column = 0)
            #=====================================================
            about_menu.update()
            height = about_menu.winfo_height()
            width = about_menu.winfo_width()
            geometry = center_app(about_menu, width, height)
            about_menu.geometry("%dx%d+%d+%d" % (geometry[0], geometry[1], geometry[2], geometry[3]))
        try:
            if about_menu.state() == 'normal' or about_menu.state() == 'iconic':
                about_menu.destroy()
        except:
            show()

    def main(self):
        menu = Menu(self.menubar, tearoff = 0)
        menu.add_command(label = 'About', command = lambda: Menubar.about(self))
        menu.add_separator()
        menu.add_command(label = 'New Window', command = new_window)
        menu.add_command(label = 'Restart Window', command = restart)
        menu.add_separator()
        menu.add_command(label = 'Settings', command = lambda : Menubar.settings(self))
        menu.add_separator()
        menu.add_command(label = 'Debug Window', command  = Menubar.show_debug)
        menu.add_separator()
        menu.add_command(label = 'Quit', command = lambda: root.quit())
        self.menubar.add_cascade(label = 'More...', menu = menu) 

    def settings(self):
        def show():
            global settings_menu
            def save_command():
                configurations['default_mode'] = default_mode.get()
                configurations['sys_argv_mode'] = sys_argv_variable.get()
                configurations['output_dir'] = path_entry_variable.get()
                configurations['temp_dir'] = temp_dir_variable.get()
                settings_menu.destroy()
            def select_dir():
                #Method for selecting output path
                path = askdirectory()
                path_entry_variable.set(path)
            def select_temp_dir():
                #Method for choosing temporary tempfiles directory.
                path = askdirectory()
                temp_dir_variable.set(path)
            #======================================
            settings_menu = Toplevel()
            settings_menu.transient(root)
            settings_menu.resizable(False, False)
            notebook = ttk.Notebook(settings_menu)
            notebook.grid(row = 0, column = 0)
            #==============================================
            default_mode = StringVar().set('encode')
            default_mode = StringVar()
            path_entry_variable = StringVar()
            sys_argv_variable = IntVar()
            temp_dir_variable = StringVar()
            #----------------------------------
            default_mode.set(configurations['default_mode'])
            sys_argv_variable.set(configurations['sys_argv_mode'])
            path_entry_variable.set(configurations['output_dir'])
            temp_dir_variable.set(configurations['temp_dir'])
            #==============================================
            style = ttk.Style()
            #==============================================
            general_settings = ttk.Frame(notebook)
            mode_frame = ttk.LabelFrame(general_settings, text = 'Default mode')
            encode_mode = ttk.Radiobutton(mode_frame, text = 'Encode', variable = default_mode, value = 'encode', style = 'TRadiobutton')
            encode_mode.grid(row = 0, column = 0, sticky = W+E)
            decode_mode = ttk.Radiobutton(mode_frame, text = 'Decode', variable = default_mode, value = 'decode', style = 'TRadiobutton')
            decode_mode.grid(row = 1, column = 0, sticky = W+E)
            auto_detect = ttk.Radiobutton(mode_frame, text = 'Auto-detect', variable = default_mode,value = 'detect', style = 'TRadiobutton')
            auto_detect.grid(row = 2, column = 0, sticky = W+E)
            mode_frame.grid(row = 0,column = 0, ipadx = 25, ipady = 5, pady = 10, sticky = W)
            #
            sys_argv_frame = ttk.LabelFrame(general_settings, text = 'Drop file and work on app start?')
            yes_radiobutton = ttk.Radiobutton(sys_argv_frame, text  = 'Yes', variable = sys_argv_variable, value = 1).grid(row = 0, column = 0)
            no_radiobutton = ttk.Radiobutton(sys_argv_frame, text = 'No', variable = sys_argv_variable, value = 0).grid(row = 1, column = 0)
            sys_argv_frame.grid(row = 1, column = 0, ipadx = 25, ipady =5, sticky = W)
            #
            general_settings.grid(row = 0, column = 0)
            #=============================================
            path_settings = ttk.Frame(notebook)
            #
            output_dir_frame = ttk.LabelFrame(path_settings, text = 'Output directory')
            path_entry = ttk.Entry(output_dir_frame, textvariable = path_entry_variable, state = 'disabled', width = 40).grid(row = 0, column = 0)
            browse_button =  ttk.Button(output_dir_frame, text = 'Browse...', command = select_dir).grid(row = 0, column = 1)
            output_dir_frame.grid(row = 0, column = 0)
            #
            temp_folder_frame = ttk.LabelFrame(path_settings, text = 'Temporary folder path')
            temp_path_entry = ttk.Entry(temp_folder_frame, textvariable = temp_dir_variable, state = 'disabled', width = 40).grid(row = 0, column = 0)
            browse_button = ttk.Button(temp_folder_frame, text = 'Browse...', command = select_temp_dir).grid(row = 0, column = 1)
            temp_folder_frame.grid(row = 1, column = 0)
            #
            path_settings.grid(row = 0, column = 0)
            #=============================================
            notebook.add(general_settings,text =  'General')
            notebook.add(path_settings, text = 'Paths')
            confirmation_frame = Frame(settings_menu)
            button_ok = ttk.Button(confirmation_frame, text = 'OK', command = save_command).grid(row = 0, column = 0)
            button_cancel = ttk.Button(confirmation_frame, text = 'Cancel', command = lambda: settings_menu.destroy()).grid(row = 0, column = 1)
            confirmation_frame.grid(row = 1, column = 0)
            #===============================================
            settings_menu.update()
            width = settings_menu.winfo_width()
            height = settings_menu.winfo_height()
            geometry = center_app(settings_menu, width, height)
            settings_menu.geometry("%dx%d+%d+%d" % (geometry[0], geometry[1], geometry[2], geometry[3]))
            #===============================================
        try:   
            if settings_menu.state() == 'normal' or settings_menu.state() == 'iconic':
                settings_menu.destroy()
        except:
            show()


    def rightclick_menu_results(event):
        save_state = DISABLED
        copy_html_state = DISABLED
        if drop_type != None: #If the temp_file_name is empty.
            save_state = NORMAL
            copy_html_state = NORMAL
            copy_css_state = NORMAL
        if drop_type == 'text' or mode_variable.get() == 'decode': #If drop_type is text or mode is decode
            copy_html_state = DISABLED
            copy_css_state = DISABLED
        elif drop_type == 'text':
            save_state = NORMAL
        
        suffix = str(pathlib.Path(file_path).suffix).lower()
        if (suffix  in PICTURES) or (suffix in AUDIOS) or (suffix in VIDEOS):
            copy_html_state = NORMAL
        else:
            copy_html_state = DISABLED
        if suffix in PICTURES:
            copy_css_state = NORMAL
        else:
            copy_css_state = DISABLED
        if mode_variable.get() == 'decode' or mode_variable.get() == 'encode':
            preview_state = NORMAL
            if drop_type == None or drop_type == 'text':
                preview_state = DISABLED
            else:
                preview_state = NORMAL
        else:
            preview_state = DISABLED
        menu = Menu(menubar, tearoff = 0)
        menu.add_command(label = 'Save', command = save_file, state = save_state)
        menu.add_command(label = 'Save (Give ext.)', command = save_file_manual, state = save_state)
        menu.add_command(label = 'Copy', command = copy_to_clipboard, state = save_state)
        menu.add_command(label = 'Copy (HTML)', command = copy_html, state = copy_html_state)
        menu.add_command(label = 'Copy (CSS)', command = copy_css, state = copy_css_state)
        menu.add_command(label = "Preview", command = preview, state = preview_state)
        menu.tk_popup(event.x_root, event.y_root)

    def rightclick_menu_file(event):
        menu = Menu(menubar, tearoff = 0)
        #=======================================
        if data_from_clipboard() == None:
            file_state = DISABLED
            text_state = DISABLED
        elif data_from_clipboard()[1] == 'string':
            #The two clipboard functions can not be both 'on' at
            #the same time.
            file_state = DISABLED
            text_state = NORMAL
        else:
            file_state = NORMAL
            text_state = DISABLED
        #=======================================
        menu.add_command(label = 'Load file', command = load_file)
        menu.add_command(label = 'Clipboard (File)', state = file_state, command = load_file_clipboard)
        menu.add_command(label = 'Clipboard (Text)', state = text_state, command = load_text_clipboard)
        menu.tk_popup(event.x_root, event.y_root)

def preview():
    save_file()
    os.startfile(save_path)
    print("Opening file at %s" % save_path)


def copy_to_clipboard():
    if type(results) == str:
        pyperclip.copy(results)
    elif type(results) == bytes:
        pyperclip.copy(results.decode())

def save_file_manual():
    #This function is for saving a file if a user wants
    #to specify the extension and name of the output.
    filename = asksaveasfilename()
    mode = mode_variable.get()
    if filename == '':
        return
    if mode == 'encode':
        with open(filename, 'w') as file:
            file.write(results)
    elif mode == 'decode':
        with open(filename, 'wb') as file:
            file.write(results)

def restart():
    os.startfile(__file__)
    root.quit()
    
def new_window():
    os.startfile(__file__)

def save_file():
    #Just saves a file
    global save_path
    mode = mode_variable.get()
    directory = pathlib.Path(configurations['output_dir'])
    try:
        if str(directory) == 'output':
           os.mkdir('output')
    except FileExistsError:
        pass
    if mode == 'encode':  
        if drop_type == 'file' or drop_type == 'load':
            p = pathlib.Path(file_path).name       
            path = str(directory.joinpath(p))
            save_path = path + '.txt'
            with open(save_path, 'w') as file:
                file.write(results)
        elif drop_type == 'text':
            p = asksaveasfilename(filetypes = (("Text files", "*.txt"), ("All files", "*.*")))
            if p == '':
                return
            path = str(directory.joinpath(p))
            with open(p, 'w') as file:
                file.write(results)
    elif mode == 'decode':
        if drop_type == 'file' or drop_type == 'load':
            print("Extension used is %s" % save_extension)
            if save_extension == None:
                print("File extension was not found.")
                return

            p = pathlib.Path(file_path).name
            path = str(directory.joinpath(p))
            save_path = path+save_extension
            
            with open(save_path, 'wb') as file:
                file.write(results)

        
        elif drop_type == 'text':
            p = asksaveasfilename(filetypes = (("Text files", "*.txt"), ("All files", "*.*")))
            if p == '':
                return
            with open(p, 'wb') as file:
                file.write(results)

def center_app(master, width, height):
    #This is a function responsible for making sure
    #that every dialog made is centered.
    screen_width = master.winfo_screenwidth()
    screen_height =  master.winfo_screenheight()
    x = round((screen_width / 2) - (width /2))
    y = round((screen_height / 2 ) - (height /2))
    return width, height, x, y

def load_text_clipboard():
    #The function for handling texts from clipboard.
    global drop_type
    global checked
    global results
    drop_type = 'text'
    if not auto_detect_variable.get() or checked == True:
        if mode_variable.get() == 'encode':
            drop_type = 'text'
            results = encode(data_from_clipboard()[0], 'normal')
            if len(results) <= 20000:
                insert(results)
                write_to_temp()
            else:
                insert(results[:20000])
                statusbar_label.config(fg ='black')
                status_variable.set("Text  too large to display all output.")
                write_to_temp()
                checked = False
        elif mode_variable.get() == 'decode':
            if isbase64(data_from_clipboard()[0]) != True:
                statusbar_label.config(fg = 'red')
                status_variable.set('Sorry, text is not base64')
            else:
                results = decode(data_from_clipboard()[0], 'normal')
                if len(results) <= 20000:
                    insert(results)
                    write_to_temp()
                    checked = False
                else:
                    insert(results[:20000])
                    statusbar_label.config(fg ='black')
                    status_variable.set("Text  too large to display all output.")
                    write_to_temp()
                    checked = False
    else:
        if (isbase64(data_from_clipboard()[0])):
            mode_variable.set('decode')
            checked = True
            load_text_clipboard()

        else:
            mode_variable.set('encode')
            checked = True
            load_text_clipboard()

def load_file_clipboard():
    global drop_type
    global checked
    global results
    global file_path
    drop_type = 'file'
    #This function loads a file from the clipboard.
    if not auto_detect_variable.get() or checked == True:
        mode = mode_variable.get()
        if mode == 'encode':
            contents = file_contents(data_from_clipboard()[0])
            file_path = data_from_clipboard()[0]
            type_ = contents[1]
            data = contents[0]
            results = encode(data, type_)
            if not is_file_large(data_from_clipboard()[0]):
                insert(results)
                write_to_temp()
                checked = False
            else:
                insert(results[:20000])
                statusbar_label.config(fg = 'black')
                status_variable.set("File too large to display all output.")
                write_to_temp()
                checked = False
        elif mode == 'decode':
            contents = file_contents(data_from_clipboard()[0])
            data = contents[0]
            type_ = contents[1]
            file_path = data_from_clipboard()[0]
            if isbase64(data) != True:
                    statusbar_label.config(fg = 'red')
                    status_variable.set('Sorry, file is not base64')
                    return
            results = decode(data, type_)
            if not is_file_large(data_from_clipboard()[0]):
                insert(results)
                write_to_temp()
                checked = False
            else:
                insert(results[:20000])
                statusbar_label.config(fg = 'black')
                status_variable.set("File too large to display all output.")
                write_to_temp()
                checked = False     

    else:
        contents = file_contents(data_from_clipboard()[0])[0]
        if isbase64(contents):
            mode_variable.set('decode')
            checked = True
            load_file_clipboard()
        else:
            mode_variable.set('encode')
            checked = True
            load_file_clipboard()


def delete(file_path):
    os.remove(file_path)

def file_or_dir(contents):
    #This function is responsible for checking if a dropped object
    #is a file or directory. It first checks if it is a directory. If it isnt, it
    #then checks if it is a file, it is not also a file, it splits the contents and checks for the 
    #value of the first object in the list using the same function.
    if path.isdir(contents) == True:
        return 'directory', None #None because no file path is returned
    elif path.isfile(contents) == True:
        return 'file', contents #The contents is the file path
    else:
        for file in file_frame.tk.splitlist(contents):
            return file_or_dir(file)
def insert(text):
    #Responsible for inserting the text into the text area.
    text_area.config(state = 'normal')
    text_area.delete(0.0, END)
    text_area.insert(0.0,text)
    text_area.config(state = DISABLED)
    statusbar_label.config(fg = 'green')
    status_variable.set('Done')

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
        #If the user open's Quick Base64 on system boot, the clipboard will
        #be empty, in order not to throw an error, we put another try statement in the except statement
        #to catch the error.
        try:
            #If the clipboard data is no text, TypeError occures.
            #This will return a path
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData(win32clipboard.CF_HDROP)
            win32clipboard.CloseClipboard()
            return [data[0], 'path']
        except:
            #So if the user's clipboard is empty, this code will be executed.
            return None

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


def is_file_large(path):
    #This function is responsible for checking if a file size is large or not.
    #If it is large, it won't insert it into the screen.
    #This is to help solve the problem of the application screen freezing because we
    #want to insert large data.
    size = getsize(path)
    max_size = 20000 #If the file size in bytes is larger than this number, the application might freeze
    
    if size > max_size:
        return True
    else:
        return False
def get_file_type(filename):
    global save_extension
    full_file_path = os.getcwd()+'//file'
    #This is a simple function which uses the file cli tool to find the
    #decoded base64 file type.
    #It first tries to find the extension of the file using the command [file --extension user_file]
    #This is expected to return the supposed file extension. If this method fails, the command [file --mime-type user_file]
    #is used to get the file type.
    command = Popen(['file','--extension',filename], shell = True, cwd = full_file_path, stdout = PIPE)
    output = command.stdout.read().decode().lower().strip().split(' ')[1] #The results if command is directed to 'stdout' and read. It is then  decoded from binary and converted into lowercase. It is then stripped into two arrays [pathname : extension]
    
    if '???' not in output:
        print("Extension found...")
        if '/' not in output: #The output will contain '/' if multiple extensions are given. So if '/' is not in the output. The output is only one.
            save_extension = "."+output
            print("Extension is %s" % ("."+output))
        elif '/' in output:
            output_split = output.split('/') #Splits the results into  a list with '/'
            save_extension = '.'+output_split[0]
            print("File's extension found were %s.\nExtension selected is %s" %(output, save_extension))
        
    elif '???' in output: #The file command returns '???' if it doesn't find an extension for a file.
        command = Popen(['file', '--mime-type', filename], shell = True, cwd = full_file_path, stdout = PIPE)
        print("Extension not found. Trying mime-type method.")
        output = command.stdout.read().decode().lower()
        file_type = output.split(" ")[1].strip()
        print("File type is ", file_type)
        if file_type == 'text/plain':
            save_extension = '.txt'
            return file_type
        elif file_type == 'audio/mpeg':
            save_extension = '.mp3'
            return file_type
        elif file_type == 'application/x-dosexec':
            save_extension = '.exe'
            return file_type
        elif file_type == 'application/x-font-tff':
            save_extension = '.ttf'
            return file_type
        elif file_type == 'image/png':
            save_extension = '.png'
            return file_type
        elif file_type == 'image/gif':
            save_extension = '.gif'
            return file_type
        elif file_type == 'application/octet-stream':
            save_extension = '.txt'
            return file_type
        elif file_type == 'text/html':
            save_extension = '.html'
            return file_type
        elif file_type == 'text/rtf':
            save_extension = '.rtf'
            return file_type
        elif file_type == 'text/x-c++':
            save_extension = '.cpp'
            return file_type
        elif file_type == 'text/x-python':
            save_extension = '.py'
            return file_type
        elif file_type == 'text/x-msdos-batch':
            save_extension = '.bat'
            return file_type
        elif file_type == 'text/x-php':
            save_extension = '.php'
            return file_type
        elif file_type == 'application/zip':
            save_extension = '.zip'
            return file_type
        elif file_type == 'application/x-gzip':
            save_extension = '.tar'
            return file_type
        elif file_type == 'text/xml':
            save_extension = '.xml'
            return file_type
        elif file_type == 'video/mp4':
            save_extension = '.mp4'
            return file_type
        elif file_type == 'image/svg':
            save_extension = '.svg'
            return file_type
        elif file_type == 'application/json':
            save_extension = '.json'
            return file_type
        elif file_type == "application/vnd.ms-fontobject":
            save_extension = ".eot"
            return file_type
        elif file_type == "font/sfnt":
            save_extension = ".ttf"
            return file_type
        elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            save_extension = ".docx"
        elif file_type == "application/x-putty-private-key":
            save_extension = ".ppk"


def write_to_temp():
    if path.exists(configurations['temp_dir']) == False: #Checks to see if the temp_dir path is avaible
        os.mkdir(configurations['temp_dir'])
    try:
        #This function writes the data to a temporary file.
        __, temp_file_name = tempfile.mkstemp(dir = configurations['temp_dir'])
        if mode_variable.get() == 'encode':
            with open(temp_file_name, 'w') as file:
                file.write(results)
            os.close(__)
            temp_files.append(temp_file_name)
        elif mode_variable.get() == 'decode':
            with open(temp_file_name, 'wb') as file:
                file.write(results)
            os.close(__)
            temp_files.append(temp_file_name)
            get_file_type(temp_file_name)
    except FileNotFoundError as error:
        print(error)
        pass

def load_file(filename = None):
    #In auto-detect mode, if the filename == None, it means the file's mode 
    #has not yet been detected. In order to tell this function that the file's
    #mode has been detected, it passes the name of the file to the function to prevent
    #it from asking for a filename again.
    global file_path
    global checked
    global results
    global drop_type
    #This is, if the user wants to encode or decode through loading a file.
    mode = mode_variable.get()
    if filename == None:
        filename = askopenfilename(title= 'Choose File')
    if filename == '':
        return
    drop_type = 'load'
    file_path = filename
    if not auto_detect_variable.get() or checked == True:
        if mode == 'encode':
            contents = file_contents(filename)
            type_ = contents[1]
            data = contents[0]
            results = encode(data, type_)
            if not is_file_large(filename):
                insert(results)
                write_to_temp()
                checked = False
            else:
                insert(results[:20000])
                statusbar_label.config(fg = 'black')
                status_variable.set("File too large to display all output.")
                write_to_temp()
                checked = False
        elif mode == 'decode':
            contents = file_contents(filename)
            data = contents[0]
            type_ = contents[1]
            if isbase64(data) != True:
                    statusbar_label.config(fg = 'red')
                    status_variable.set('Sorry, file is not base64')
                    return
            results = decode(data, type_)
            if not is_file_large(filename):
                insert(results)
                write_to_temp()
                checked = False
            else:
                insert(results[:20000])
                statusbar_label.config(fg = 'black')
                status_variable.set("File too large to display all output.")
                write_to_temp()
                checked = False
    else:
        contents = file_contents(filename)
        if isbase64(contents[0]):
            mode_variable.set('decode')
            checked = True #Tells the program that the mode has been detected.
            load_file(filename) #Repeats the function with the mode now known.
        else:
            mode_variable.set('encode')
            checked = True
            load_file(filename)

def drop_enter(event):
    #This is what happens when a file enters the widget
    if auto_detect_variable.get() == 'detect': #That is, if the mode is set to auto-detect.
        statusbar_label.config(fg = 'black')
        status_variable.set("Detecting...")
        return event.action
    if not auto_detect_variable.get():
        #If auto-detect mode is on, it overrides everything.
        statusbar_label.config(fg = 'green')
        status_variable.set('Preparing to {}.'.format(mode_variable.get()))
        return event.action

def file_contents(file_path):
    #This function is responsible for opening a file and returning its contents.
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            return contents, 'normal' #The normal is to help encode function to know whether the file is a text file or binary
    except UnicodeDecodeError:
        with open(file_path, 'rb') as file:
            contents = file.read()
            return contents, 'binary'
        
def copy_html():
    #Copy to clipboard for embeddding in HTML
    path_suffix = str(pathlib.Path(file_path).suffix).lower()
    if drop_type == 'file' or drop_type == 'load':
        if path_suffix in PICTURES:
            code = '<img src="data:image/%s;base64,%s">' % (path_suffix[1:], results)
            pyperclip.copy(code)
        elif path_suffix in AUDIOS:
            code = '<audio controls src="data:audio/%s;base64,%s"></audio>' % (path_suffix[1:], results)
            pyperclip.copy(code)
        elif path_suffix in VIDEOS:
            code = '<video controls src="data:video/%s;base64,%s"></video>' % (path_suffix[1:], results)
            pyperclip.copy(code)
            
            
def copy_css():
    #Copy to clipboard for embeddding in CSS
    path_suffix = str(pathlib.Path(file_path).suffix).lower()
    if drop_type == 'file' or drop_type == 'load':
        if path_suffix in PICTURES:
            code = 'url(data:image/%s;base64,%s)' % (path_suffix[1:], results)
            pyperclip.copy(code)
            
def drop_file(event):
    global drop_type
    global results
    global file_path
    global checked
    status_variable.set('')
    if not auto_detect_variable.get() or checked == True:
        #When someone drops a file or folder.
        if mode_variable.get() == 'encode':
            is_file_or_directory = file_or_dir(event.data)
            if is_file_or_directory[0] == 'directory':
                statusbar_label.config(fg = 'red')
                status_variable.set('Sorry, cannot {} a folder'.format(mode_variable.get()))
            else:
                drop_type = 'file'
                path = is_file_or_directory[1]
                file_path = path
                contents = file_contents(path)
                type_ = contents[1]
                data = contents[0]
                results = encode(data, type_)
                if not is_file_large(path):
                    insert(results) #The results are inserted into the text area.
                    write_to_temp()
                    checked = False

                else:
                    write_to_temp()
                    insert(results[:20000])
                    statusbar_label.config(fg = 'black')
                    status_variable.set("File too large to display all output.")
                    checked = False
        else:
            is_file_or_directory = file_or_dir(event.data)
            if is_file_or_directory[0] == 'directory':
                statusbar_label.config(fg = 'red')
                status_variable.set('Sorry, cannot {} a folder'.format(mode_variable.get()))
            else:
                drop_type = "file"
                path = is_file_or_directory[1]
                file_path = path
                contents = file_contents(path)
                type_ = contents[1]
                data = contents[0]
                if isbase64(data) != True:
                    statusbar_label.config(fg = 'red')
                    status_variable.set('Sorry, file is not base64')
                else:
                    results = decode(data, type_)
                    if not is_file_large(path):
                        insert(results) #The results are inserted into the text area.
                        write_to_temp()
                        checked = False
                    else:
                        insert(results[:20000])
                        statusbar_label.config(fg = 'black')
                        status_variable.set("File too large to display all output.")
                        write_to_temp()
                        checked = False
                

    else:
        is_file_or_directory = file_or_dir(event.data)
        if is_file_or_directory[0] == 'directory':
            statusbar_label.config(fg = 'red')
            variable.set('Sorry, cannot work with a folder')
        else:
            drop_type = 'file'
            path = is_file_or_directory[1]
            file_path = path
            contents = file_contents(path)
            if isbase64(contents[0]):
                mode_variable.set('decode')
                checked = True
                drop_file(event)
                #After auto-detect mode detects a mode for the application, the code calls the drop_file
                #function again, in order not to lead to recursion, we set a variable to monitor if a dropped
                #file's mode has been detected or not.

            else:
                mode_variable.set('encode')
                checked = True
                drop_file(event)

def drop_text(event):
    global drop_type
    global results
    global checked
    if not auto_detect_variable.get() or checked == True:
        if mode_variable.get() == 'encode':
            drop_type = 'text'
            results = encode(event.data, 'normal')
            if len(results) <= 20000:
                insert(results)
                write_to_temp()
            else:
                insert(results[:20000])
                statusbar_label.config(fg ='black')
                status_variable.set("Text  too large to display all output.")
                write_to_temp()
                checked = False
        elif mode_variable.get() == 'decode':
            if isbase64(event.data) != True:
                statusbar_label.config(fg = 'red')
                status_variable.set('Sorry, text is not base64')
            else:
                results = decode(event.data, 'normal')
                if len(results) <= 20000:
                    insert(results)
                    write_to_temp()
                    checked = False
                else:
                    insert(results[:20000])
                    statusbar_label.config(fg ='black')
                    status_variable.set("Text  too large to display all output.")
                    write_to_temp()
                    checked = False
    else:
        if (isbase64(event.data)):
            mode_variable.set('decode')
            checked = True
            drop_text(event)

        else:
            mode_variable.set('encode')
            checked = True
            drop_text(event)

def drop_leave(event):
    #This is what happens when a widget leaves the window
    status_variable.set('')
def encode(data, data_type):
    if data_type == 'normal':
        encoded = pybase64.b64encode(data.encode()).decode()
        return encoded
    else:
        encoded = pybase64.b64encode(data).decode()
        return encoded

def decode(data, data_type):
    if data_type == 'normal':
        return pybase64.b64decode(data, validate = True)

def sys_argv():
    #This function is activated when a user drops a file onto 
    #Quick Base64's exe file.
    #Well, this option can be disabled or enabled.
    if configurations['sys_argv_mode'] == '1':
        global drop_type
        global checked
        global results
        global file_path
        if len(sys.argv) > 1:
            file_path = sys.argv[1]
            drop_type = 'file'
            if not auto_detect_variable.get() or checked == True:
                if mode_variable.get() == 'encode':
                    is_file_or_directory = file_or_dir(file_path)
                    if is_file_or_directory[0] == 'directory':
                        statusbar_label.config(fg = 'red')
                        status_variable.set('Sorry, cannot {} a folder'.format(mode_variable.get()))
                    else:
                        drop_type = 'file'
                        path = is_file_or_directory[1]
                        file_path = path
                        contents = file_contents(path)
                        type_ = contents[1]
                        data = contents[0]
                        results = encode(data, type_)
                        if not is_file_large(path):
                            insert(results) #The results are inserted into the text area.
                            write_to_temp()
                            checked = False
                        else:
                            insert(results[:20000])
                            write_to_temp()
                            checked = False
                            statusbar_label.config(fg ='black')
                            status_variable.set("Text  too large to display all output.")
                else:
                    is_file_or_directory = file_or_dir(file_path)
                    if is_file_or_directory[0] == 'directory':
                        statusbar_label.config(fg = 'red')
                        status_variable.set('Sorry, cannot {} a folder'.format(mode_variable.get()))
                    else:
                        path = is_file_or_directory[1]
                        file_path = path
                        contents = file_contents(path)
                        type_ = contents[1]
                        data = contents[0]
                        if isbase64(data) != True:
                            statusbar_label.config(fg = 'red')
                            status_variable.set('Sorry, file is not base64')
                        else:
                            results = decode(data, type_)
                            if not is_file_large(path):
                                insert(results) #The results are inserted into the text area.
                                write_to_temp()
                                checked = False
                            else:
                                insert(results[:20000])
                                statusbar_label.config(fg = 'black')
                                status_variable.set("File too large to display all output.")
                                write_to_temp()
                                checked = False


            else:
                is_file_or_directory = file_or_dir(file_path)
                if is_file_or_directory[0] == 'directory':
                    statusbar_label.config(fg = 'red')
                    variable.set('Sorry, cannot work with a folder')
                else:
                    drop_type = 'file'
                    path = is_file_or_directory[1]
                    file_path = path
                    contents = file_contents(path)
                    if isbase64(contents[0]):
                        mode_variable.set('decode')
                        checked = True
                        sys_argv()
                    else:
                        mode_variable.set('encode')
                        checked = True
                        sys_argv()

def init_configuration():
    # This function is for starting and reading the configuration.
    global mode_variable
    global mode
    try:
        config = ConfigParser()
        config.read('configuration.ini')
        mode = config['general'].get('default_mode')
        sys_argv_mode = config['general'].get('sys_argv_mode')
        output_dir = config['paths'].get('output_dir')
        temp_dir = config['paths'].get('temp_dir')
        #____________________________________________________________
        configurations['default_mode'] = mode
        configurations['sys_argv_mode'] = sys_argv_mode
        configurations['output_dir'] = output_dir
        configurations['temp_dir'] = temp_dir
        if mode == 'detect':
            auto_detect_variable.set(1)
        mode_variable.set(mode)
    except:
        mode = 'encode'
        configurations['default_mode'] = mode
        configurations['output_dir'] = 'output'
        configurations['sys_argv_mode'] = 1
        configurations['temp_dir'] = tempfile.gettempdir()
        mode_variable.set('encode')

init_configuration()
#===========================================================
#Frames 
#===================================
file_frame = LabelFrame(root, text = 'Drop Object Here', height = 200, width  = 200)
text_frame = LabelFrame(root, text = 'Results appear here')
controls_frame = LabelFrame(root)
statusbar_frame = LabelFrame(root)
#=========================================
#Controls_frame widgets
mode_encode = ttk.Radiobutton(controls_frame, text = 'encode', variable = mode_variable, value = 'encode')
mode_auto_detect = ttk.Checkbutton(controls_frame, text = 'Auto-detect', variable = auto_detect_variable, command = lambda: mode_variable.set(''))
mode_decode = ttk.Radiobutton(controls_frame, text = 'decode', variable = mode_variable, value = 'decode')
#=================================================================================================
#Text Frame widgets
#====================================
text_area = ScrolledText(text_frame, width = 30, state = DISABLED)
# Statusbar widgets
#=================================
statusbar_label = Label(statusbar_frame, textvariable = status_variable)
#===================================
#Gridding system
#===================================
#   Frames
#===================================
file_frame.grid(row = 0, column = 0, sticky = W+E+N+S)
text_frame.grid(row = 0, column = 1, sticky = E+W+N+S)
controls_frame.grid(row = 1, column = 0, columnspan = 2, sticky = W+E+N)
statusbar_frame.grid(row = 2, column = 0, sticky = W+E, columnspan = 2)
#==================================================================
#   Widgets
mode_encode.grid(row = 0, column = 0, sticky = W)
mode_auto_detect.grid(row = 0, column = 0)
mode_decode.grid(row = 0, column = 2)
text_area.grid(row = 0, column = 0, sticky = N+E+W+S)
statusbar_label.grid(row = 0, column = 0)
#==========================================================
#   Making widgets stretchable
root.grid_rowconfigure(0, weight = 1)
root.grid_columnconfigure(0, weight = 1, minsize = 150)
root.grid_columnconfigure(1, weight = 1, minsize = 150)
root.grid_rowconfigure(1, weight = 1)
controls_frame.grid_rowconfigure(0, weight = 1)
controls_frame.grid_columnconfigure(0, weight = 1)
text_frame.grid_columnconfigure(0, weight = 1)
text_frame.grid_rowconfigure(0, weight = 1)
#==================================================
#Making widgets drop target
#=================================================
file_frame.drop_target_register(DND_ALL) #The frame is registered to accept all widgets
file_frame.dnd_bind('<<DropEnter>>', drop_enter)
file_frame.dnd_bind('<<Drop:DND_Files>>', drop_file)
file_frame.dnd_bind('<<Drop:DND_Text>>', drop_text)
file_frame.dnd_bind('<<DropLeave>>', drop_leave)
#==============================================================================
text_area.bind("<Button-3>", Menubar.rightclick_menu_results)
file_frame.bind("<Button-3>", Menubar.rightclick_menu_file)
root.config(menu = menubar)
root.resizable(width = True, height = False)
menu = Menubar(menubar)
#===========================================
#===========================================
#   Centering the application
root.update()
width = root.winfo_width()
height = root.winfo_height()
geometry = center_app(root,width, height)
root.geometry("%dx%d+%d+%d" %(geometry[0], geometry[1], geometry[2], geometry[3]))
#===========================================
sys_argv()
root.mainloop()
#==========================================================================
#End
#==========================================================================
try:
    #This statement deletes all the temporary files created
    #by the application.
    for temporary_file in temp_files:
        delete(temporary_file)
except FileNotFoundError:
    pass

#========================
# Configuration
#========================
configuration = ConfigParser()
#========================

configuration['general'] = {
    'default_mode'  : configurations['default_mode'],
    'sys_argv_mode' : configurations['sys_argv_mode'],
}
configuration['paths'] = {
    'output_dir' : configurations['output_dir'],
    'temp_dir' : configurations['temp_dir']
}
with open('configuration.ini', 'w') as file:
    configuration.write(file)