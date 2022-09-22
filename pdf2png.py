from fileinput import filename
import tkinter as tk
import tkinter.font as tkFont
from pdf2image import convert_from_path
from tkinter import filedialog
from pdf2image import convert_from_path
import glob, os
import subprocess

# This for poppler library
bindir = str(os.getcwd()) + '/bin'
filenameLabel = ""

class App:
    def __init__(self, root):  
        # select button
        button= tk.Button(root, text="Select", command=lambda: self.select_dir_and_convert(root))
        button.pack(ipadx=5, pady=15)
        
    
    def select_dir_and_convert(self, root):
        # select PDF Directory
        path= filedialog.askdirectory(initialdir=r"", title="Select PDF directory")

        if path == '': 
            # if not selecte any directory
            tk.Label(root, text='Please select an directory', font=13).pack()
            return

        if os.path.exists(path + '/toPNG'):
            print('Directory exists')
        else:
            # Create toPNG directory
            os.mkdir(path + '/toPNG')
    
        toPNG = path + '/toPNG'
        os.chdir(path)
        # fetch all pdf files in PDF directory
        
        my_label.pack()
        for file in glob.glob("*.pdf"):
            my_label.config(text=file)
            if 1:
                images = convert_from_path(path +'/'+ file, poppler_path=bindir)
                # Convert PDF to PNG
                for i in range(len(images)):
                    if len(images) == 1:
                        images[i].save(path + '/toPNG/'+file[0:len(file)-4]+'.png', 'PNG')
                    else:
                        images[i].save(path + '/toPNG/'+file[0:len(file)-4]+' ('+ str(i) +').png', 'PNG')
        # Done Notic
        tk.Label(root, text='Done 😊', font=13).pack()
        # Open toPNG directory
        cmd = r'explorer /separate,"%s"'
        toPNG = toPNG.replace('/', '\\')
        subprocess.Popen(cmd % toPNG)

if __name__ == "__main__":
    # initialize tkinter
    root = tk.Tk()
    # window size
    root.geometry("350x170")
    # window title
    root.title("PDF to PNG")
    tk.Label(root, text="Click the Button to Select PDF directory", font=('roboto')).pack(pady=20)
    my_label = tk.Label(root, text="", font=13)
    app = App(root)
    root.mainloop()
