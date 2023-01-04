from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import shutil

window = Tk()
window.geometry('500x500')
window.config(background="cyan")
window.title("File Organizer")

FONT = ("Arial", 12, "normal")

img = ImageTk.PhotoImage(Image.open("image2.png"))
img_label = Label(window, image = img, bg = "cyan").place(x = 50, y = 10 ) 

path = ""

def getPath():
    global path
    # kullanıcıya seçeceği klasörü soran pencere
    path = filedialog.askdirectory()
    print(path)
    msg = "Klasörünüz = "
    # dosya yolunu "/" ile bölüp listeye çevirdik ve -1 yani son indeksi aldık.
    # MAC ve LINUX için bu işaret "\" olmalıdır.
    label.config(text = msg + path.split("/")[-1]) 

open_button = Button(window, text = "KLASÖR SEÇ", bg = "yellow", command = getPath, font = FONT)
open_button.place(x=200, y = 300)
label = Label(window, text = "Klasörünüz = Seçilmedi", bg = "cyan", font = FONT)
label.place(x=180, y = 340)

def start():
    count = 0
    os.chdir(path) # dizin değiştirdik
    file_list = os.listdir() # dosyaları okuduk
    num_of_files = len(file_list) # dosya sayısını aldık
        
    for file in file_list:
        if file.endswith(".png"):
            dir_name = "PngDosyaları"
            if dir_name not in file_list:
                os.mkdir(dir_name)
            shutil.move(file, dir_name)
            count += 1
            
        if file.endswith(".py"):
            dir_name = "PythonDosyaları"
            if dir_name not in file_list:
                os.mkdir(dir_name)
            shutil.move(file, dir_name)
            count += 1
            
        if file.endswith(".blend"):
            dir_name = "BlenderDosyaları"
            if dir_name not in file_list:
                os.mkdir(dir_name)
            shutil.move(file, dir_name)
            count += 1
        
        # dosya listesini güncelle
        file_list = os.listdir()
    # dosyaların hepsini gezdik, for döngüsü bitti
    Label(text = f"{count} adet dosya taşındı", bg = "cyan", font = FONT).place(x=180, y = 440)
    
start_button = Button(window, text = "BAŞLA", bg = "lime", command = start, font = FONT)
start_button.place(x=220, y = 400)

window.mainloop()