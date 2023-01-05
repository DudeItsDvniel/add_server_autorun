import tkinter.messagebox
import tkinter.filedialog
import winreg
import shutil
import uuid
import sys
import os

def info(title='Info:', message=''):
    result = tkinter.messagebox.showinfo(title, message)

def question(title='Question:', message=''):
    result = tkinter.messagebox.askquestion(title, message)
    if result == 'yes':
        result = True
    if result == 'no':
        result = False
    return result

def error(title='Error:', message=''):
    result = tkinter.messagebox.showerror(title, message)

def open_file():
    encoding = 'utf-8'
    try:
        import locale
        locale.setlocale(locale.LC_ALL, '')
        encoding = locale.nl_langinfo(locale.CODESET)
    except (ImportError, AttributeError):
        pass
    file = tkinter.filedialog.askopenfilename(filetypes=[('Batch files.', '*.bat')])
    return file

def set_key_value(path, name, value, type=winreg.REG_SZ, hkey=winreg.HKEY_LOCAL_MACHINE, rights=winreg.KEY_WRITE):
    winreg.CreateKey(hkey, path)
    registry_key = winreg.OpenKey(hkey, path, 0, rights)
    winreg.SetValueEx(registry_key, name, 0, type, value)
    winreg.CloseKey(registry_key)

def get_key_value(path, name, hkey=winreg.HKEY_LOCAL_MACHINE, rights=winreg.KEY_READ):
    registry_key = winreg.OpenKey(hkey, path, 0, rights)
    value, type = winreg.QueryValueEx(registry_key, name)
    winreg.CloseKey(registry_key)
    return value

uuid = str(uuid.uuid4())

if __name__ == '__main__':

    ____exit__status = None

    if ____exit__status != 1:

        result = None
        value = None

        try:
            file = str(open_file()).replace('/','\\')
            if len(file) < 7:
                error(message="Looks like you didn't add a file.\nNow exiting.")
                ____exit__status = 1
                sys.exit("User didn't add a file...")
        except:
            error(message="Looks like you didn't add a file or something else went wrong.\nNow exiting.")
            ____exit__status = 1
            sys.exit("User didn't add a file or something else went wrong...")

        if ____exit__status != 1:

            try:
                set_key_value('Software\\Microsoft\\Windows\\CurrentVersion\\Run', f'Server_Starter_{str(uuid)}', str(file))
            except:
                error(message=f'Could not set the registry value.\nReason: {str(sys.exc_info()[1])}.\nNow exiting.')
                ____exit__status = 1
                sys.exit(f'Could not set the registry value.\nReason: {str(sys.exc_info()[1])}.')
            else:
                info(message='Location has been set and added.\nPress ok to continue.')

            if ____exit__status != 1:
            
                try:
                    value = get_key_value('Software\\Microsoft\\Windows\\CurrentVersion\\Run', f'Server_Starter_{str(uuid)}')
                except:
                    error(message=f'Could not find the registry value.\nReason: {str(sys.exc_info()[1])}.\nNow exiting.')
                    ____exit__status = 1
                    sys.exit(f'Could not find the registry value.\nReason: {str(sys.exc_info()[1])}.')
                else:
                    info(message=f'Location has been checked and is valid.\nPress ok to continue.\n\nRegistry Key Location: HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\Server_Starter_{uuid}\nRegistry Key Value: {value}')

                result = None
                value = None

            else:
                sys.exit(1)
                
        else:
            sys.exit(1)
        
    else:
        sys.exit(1)