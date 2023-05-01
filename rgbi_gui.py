import os

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


# GUI for RGBI           

class RGBI_GUI:
    
    def __init__(self, window):
               
        window.title("RGB to Intensity Image")
        window.geometry('670x160')
        window.configure(background = '#f0f0f0')
        window.resizable(False, False)
        
        self.style = ttk.Style()
        self.style.configure('TFrame',  background = '#f0f0f0')
        self.style.configure('TButton', background = '#f0f0f0')
        self.style.configure('TLabel',  background = '#f0f0f0', font = ('Arial', 10))     

        def yolo_callbackFunc(event):
            selected_yolo = event.widget.get()
            yolo_ver.set(selected_yolo)
            print("Selected Yolo Version = ", selected_yolo)                                                        
                              
        def browseFileFunc():
            inputDir = filedialog.askopenfilename(initialdir=os.getcwd(), title = "Select The Input File")
            print("Part Table  = ", inputDir)
            ipPathName.set(inputDir)
 
        def browseDirFunc():
            OutputDir = filedialog.askdirectory(initialdir=os.getcwd(), initialfile=None)
            print("Output Directory = ", OutputDir)
            opPathName.set(OutputDir)

        def generateReports():
            stripPath     = ipPathName.get()
            stropPath = opPathName.get()
            stryoloVer     = yolo_ver.get()
            
            if len(stripPath) == 0 or len(stropPath) == 0:
                 messagebox.showerror("Error", "Input Directory or Output Directory is not specified!")
            else:
                msgbox = messagebox.askyesno("Successful Completion", "The output is generated successfully!\n\nClick 'Yes' to open the output directory.\nClick 'No' to quit this application.")
                    
                if msgbox == True:
                    path=os.path.realpath(stropPath)
                    os.startfile(path)
                else:
                    window.destroy()
       
        self.frame_header = LabelFrame(window, text = 'Choose the options:', padx = 10, pady = 5, font = ('Arial', 10, 'bold'))
        self.frame_header.config(relief = GROOVE)
        self.frame_header.pack()
                   
        self.labelInput = ttk.Label(self.frame_header, text = "Input Directory:") 
        self.labelInput.grid(column = 0, row = 0,  sticky = 'sw', pady = 10)
        ipPathName = StringVar(value=os.getcwd())
        self.entryInputPath = ttk.Entry(self.frame_header, width = 55, font = ('Arial',10), textvariable = ipPathName)
        self.entryInputPath.grid(column = 1, row = 0)
        self.btnBrowseIpDir = ttk.Button(self.frame_header, text = "Browse", command = browseFileFunc)
        self.btnBrowseIpDir.grid(column = 2, row = 0,  padx = 10, ipadx = 2, ipady = 2)
        
        self.labelOutputPath = ttk.Label(self.frame_header, text = "Output Directory:")
        self.labelOutputPath.grid(column = 0, row = 1, sticky = 'sw', pady = 10)
        opPathName = StringVar(value=os.getcwd())
        self.entryOutputPath = ttk.Entry(self.frame_header, width = 55, font = ('Arial',10), textvariable = opPathName)
        self.entryOutputPath.grid(column = 1, row = 1)
        self.btnBrowseOpDir = ttk.Button(self.frame_header, text = "Browse", command = browseDirFunc)
        self.btnBrowseOpDir.grid(column = 2, row = 1,  padx = 10, ipadx = 2, ipady = 2)
        
        self.labelVersion = ttk.Label(self.frame_header, text = "YOLO Version:")
        self.labelVersion.grid(column = 0, row = 2, sticky = 'sw', pady = 10) 
        yolo_ver = StringVar()
        self.comboYolo = ttk.Combobox(self.frame_header, values=["v1", "v2", "v3", "v4", "v5"], width = 5, textvariable = yolo_ver)
        self.comboYolo.grid(column = 1, row = 2, sticky = 'sw', pady = 10)
        self.comboYolo.current(0)

        self.btnGenRes = ttk.Button(self.frame_header, text = "Generate Output", command = generateReports)
        self.btnGenRes.grid(column = 2, row = 2, ipadx = 5, ipady = 3)
                    
        self.comboYolo.bind("<<ComboboxSelected>>", yolo_callbackFunc)

def main():            
    
    window = Tk()
    RGBI_GUI(window)
    window.mainloop()

if __name__ == "__main__": main() 