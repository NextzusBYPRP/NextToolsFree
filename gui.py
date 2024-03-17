from pathlib import Path
import tkinter as tk
import webbrowser,ctypes,os,requests,sys
from tkinter import Tk, Canvas, Label, PhotoImage,messagebox
from ctypes import windll
from PIL import ImageTk,Image

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

user = os.getlogin()

def NetworkFix():
    url = "https://raw.githubusercontent.com/NextzusBYPRP/NextToolsFree/main/Nextzus-File/Network_fix.bat"
    if is_admin():
        try:
            os.startfile(f'C:/Users/Public/Videos/Network_fix.bat')
        except:
            response = requests.get(url)
            with open(f'C:/Users/Public/Videos/Network_fix.bat', 'wb') as f:
                f.write(response.content)
            os.startfile(f'C:/Users/Public/Videos/Network_fix.bat')

            _doHideBatch = os.popen(f'attrib +h C:/Users/Public/Videos/Network_fix.bat')
            _doHideBatch.read()
            _doHideBatch.close()
    else:
        run_as_admin()


def FixWindowsSearchBox():
        mystr_encoded = "https://raw.githubusercontent.com/NextzusBYPRP/NextToolsFree/main/Nextzus-File/Fix_Windows_Search_Box.bat"
        if is_admin():    
            try:
                os.startfile(f'C:/Users/Public/Videos/Fix_Windows_Search_Box.bat')
            except:
                with open(f'C:/Users/Public/Videos/Fix_Windows_Search_Box.bat', 'wb') as f:
                    f.write(requests.get(mystr_encoded).content)
                os.startfile(f'C:/Users/Public/Videos/Fix_Windows_Search_Box.bat')

                _doHideBatch = os.popen(f'attrib +h C:/Users/Public/Videos/Fix_Windows_Search_Box.bat')
                _doHideBatch.read()
                _doHideBatch.close()
        else:
            run_as_admin()
            
def WindowsServiceControl():
        mystr_encoded = "https://raw.githubusercontent.com/NextzusBYPRP/NextToolsFree/main/Nextzus-File/Windows_Service_Control.bat"
        if is_admin():    
            try:
                os.startfile(f'C:/Users/Public/Videos/Windows_Service_Control.bat')
            except:
                with open(f'C:/Users/Public/Videos/Windows_Service_Control.bat', 'wb') as f:
                    f.write(requests.get(mystr_encoded).content)
                os.startfile(f'C:/Users/Public/Videos/Windows_Service_Control.bat')

                _doHideBatch = os.popen(f'attrib +h C:/Users/Public/Videos/Windows_Service_Control.bat')
                _doHideBatch.read()
                _doHideBatch.close()
        else:
            run_as_admin()
            
def CleanTemporary():
        mystr_encoded = "https://raw.githubusercontent.com/NextzusBYPRP/NextToolsFree/main/Nextzus-File/Clean_Temporary.bat"
        if is_admin():    
            try:
                os.startfile(f'C:/Users/Public/Videos/Clean_Temporary.bat')
            except:
                with open(f'C:/Users/Public/Videos/Clean_Temporary.bat', 'wb') as f:
                    f.write(requests.get(mystr_encoded).content)
                os.startfile(f'C:/Users/Public/Videos/Clean_Temporary.bat')

                _doHideBatch = os.popen(f'attrib +h C:/Users/Public/Videos/Clean_Temporary.bat')
                _doHideBatch.read()
                _doHideBatch.close()
        else:
            run_as_admin()
            
def RestoreHealthyourPC():
        mystr_encoded = "https://raw.githubusercontent.com/NextzusBYPRP/NextToolsFree/main/Nextzus-File/Restore_Health_your_PC.bat"
        if is_admin():    
            try:
                os.startfile(f'C:/Users/Public/Videos/Restore_Health_your_PC.bat')
            except:
                with open(f'C:/Users/Public/Videos/Restore_Health_your_PC.bat', 'wb') as f:
                    f.write(requests.get(mystr_encoded).content)
                os.startfile(f'C:/Users/Public/Videos/Restore_Health_your_PC.bat')

                _doHideBatch = os.popen(f'attrib +h C:/Users/Public/Videos/Restore_Health_your_PC.bat')
                _doHideBatch.read()
                _doHideBatch.close()
        else:
            run_as_admin()
            
def DisablingFullscreenExclusive():
        mystr_encoded = "https://raw.githubusercontent.com/NextzusBYPRP/NextToolsFree/main/Nextzus-File/Disabling_Full-screen_Exclusive.bat"
        if is_admin():    
            try:
                os.startfile(f'C:/Users/Public/Videos/Disabling_Full-screen_Exclusive.bat')
            except:
                with open(f'C:/Users/Public/Videos/Disabling_Full-screen_Exclusive.bat', 'wb') as f:
                    f.write(requests.get(mystr_encoded).content)
                os.startfile(f'C:/Users/Public/Videos/Disabling_Full-screen_Exclusive.bat')

                _doHideBatch = os.popen(f'attrib +h C:/Users/Public/Videos/Disabling_Full-screen_Exclusive.bat')
                _doHideBatch.read()
                _doHideBatch.close()
        else:
            run_as_admin()
            
def PowerPlanFix():
        mystr_encoded = "https://raw.githubusercontent.com/NextzusBYPRP/NextToolsFree/main/Nextzus-File/power_plan_fix.bat"
        if is_admin():    
            try:
                os.startfile(f'C:/Users/Public/Videos/power_plan_fix.bat')
            except:
                with open(f'C:/Users/Public/Videos/power_plan_fix.bat', 'wb') as f:
                    f.write(requests.get(mystr_encoded).content)
                os.startfile(f'C:/Users/Public/Videos/power_plan_fix.bat')

                _doHideBatch = os.popen(f'attrib +h C:/Users/Public/Videos/power_plan_fix.bat')
                _doHideBatch.read()
                _doHideBatch.close()
        else:
            run_as_admin()


window = Tk()

window.geometry("519x135")
window.configure(bg = "#111E30")
width_of_window_login = 519
height_of_window_login = 135
labels = []  
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window_login/2)
y_coordinate = (screen_height/2)-(height_of_window_login/2)
window.geometry("%dx%d+%d+%d" %(width_of_window_login,height_of_window_login,x_coordinate,y_coordinate))
window.overrideredirect(1) 
window.resizable(False, False)   
window.attributes('-topmost', 1)

urllogo = "https://drive.google.com/uc?export=download&id=13QZDs4kWym0aDKmjpUkBuW8qzcG_mLYt"
logo = ImageTk.PhotoImage(Image.open(requests.get(urllogo, stream=True).raw))
window.iconphoto(False,logo)

var = tk.StringVar()
var.set("กรุณาเลือกสิ่งที่ต้องการซ่อม")

# สร้าง dictionary สำหรับเก็บตัวเลือกและ URL ที่ต้องการโหลด
options = {
    "Network Fix": NetworkFix,
    "Fix Windows Search Box": FixWindowsSearchBox,
    "Windows Service Control": WindowsServiceControl,
    "Clean Temporary": CleanTemporary,
    "Restore Health your PC": RestoreHealthyourPC,
    "Disabling Full-screen Exclusive": DisablingFullscreenExclusive,
    "Power Plan Fix": PowerPlanFix
    
}

def submit(event):
    if is_admin(): 
        messagebox.showinfo("Nextzus Repair Tools | User : " + user, "Please make sure your System Restore Point is turn on\nกรุณาตรวจสอบให้แน่ใจว่า System Restore Point ของคุณเปิดใช้งาน")
        choice = var.get()
        if choice == "กรุณาเลือกสิ่งที่ต้องการซ่อม":
            messagebox.showinfo("Nextzus Repair Tools | User : " + user, "กรุณาเลือกสิ่งที่ต้องการซ่อม")
        else:
            options[choice]()
    else:
        messagebox.showerror("Nextzus Repair Tools | User : " + user, "กรุณารันแอดมินเพื่อใช้งาน\nPlease run app as administrator")
    os._exit(1)
    
        
def discord(event):
    webbrowser.open('https://discord.gg/nextzus')
    
def quit(event):
    sys.exit()
    
canvas = Canvas(window,bg = "#FFFFFF",height = 135,width = 519,bd = 0,highlightthickness = 0,relief = "ridge")

canvas.place(x = 0, y = 0)

url2_banner = "https://drive.google.com/uc?export=download&id=1-WHFATtOtPTOTZGmfvAuBkyPyC636k_h"
image_image_2 = ImageTk.PhotoImage(Image.open(requests.get(url2_banner, stream=True).raw))
image_2 = canvas.create_image(259.0,67.0,image=image_image_2)

opt = tk.OptionMenu(window, var, *options.keys())
opt.config(width=43, height=2)
opt.place(x=15.0, y=75.0)

url4_banner = "https://drive.google.com/uc?export=download&id=1cTFtkiNQ4HS4SBqcv38LVoinx4NGrlq2"
image_image_4 = ImageTk.PhotoImage(Image.open(requests.get(url4_banner, stream=True).raw))
image_4 = canvas.create_image(144.0,40.0,image=image_image_4)

url5 = "https://drive.google.com/uc?export=download&id=1sjzxJvq0FAzgnWoGJJVCszs2BgVfHObJ"
image_5 = ImageTk.PhotoImage(Image.open(requests.get(url5, stream=True).raw))
image_5_label = Label(window, image=image_5, bg='#111E30')
image_5_label.image = image_5
image_5_label.place(x=331, y=74)
image_5_label.bind("<Button-1>", submit )

url6 = "https://drive.google.com/uc?export=download&id=1x_2keRtK2w-EmHH6fQvzB4IehB3w-QJm"
image_6 = ImageTk.PhotoImage(Image.open(requests.get(url6, stream=True).raw))
image_6_label = Label(window, image=image_6, bg='#111E30')
image_6_label.image = image_6
image_6_label.place(x=276, y=15)
image_6_label.bind("<Button-1>", discord )

url7 = "https://drive.google.com/uc?export=download&id=1aW2e7vCgL4rBK0mLaOgTWa_cSc7boeNE"
image_7 = ImageTk.PhotoImage(Image.open(requests.get(url7, stream=True).raw))
image_7_label = Label(window, image=image_7, bg='#111E30')
image_7_label.image = image_7
image_7_label.place(x=479, y=0)
image_7_label.bind("<Button-1>", quit )

window.resizable(False, False)
window.mainloop()
