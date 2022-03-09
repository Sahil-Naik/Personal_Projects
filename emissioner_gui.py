import tkinter as tk
import tkinter.messagebox
import pandas as pd
import webbrowser as wb

def about_win():
    # Initializing new window over existing window
    root.withdraw()
    about = tk.Toplevel(root)
    about.geometry('256x256')
    about.title('About')
    about.resizable(False, False)
    # Adding contents to new window
    info = tk.Label(about, text='Hello', bd=10, font=('Arial', 14)).pack()

    # Function to return from 'about' page to main page
    def back_to_main():
        about.destroy()
        root.iconify()
        root.deiconify()

    go_back = tk.Button(about, text='Go Back', command=back_to_main).pack()
    about.mainloop()


# Function to open my website
def visit_web(url='https://sahil7naik57.wixsite.com/upturn-io'):
    wb.open(url)



# Function to check the current version of software
def check_version():
    tkinter.messagebox.showinfo('Version', 'Version: Pre-Alpha 1.0')

root = tk.Tk()                      # Main window which will be showed when app runs
root.configure()                    # Background color of Front page
root.geometry("1024x768")
root.title("Emissioner")
root.resizable(False, False)

# Configuring icon
icon = tk.PhotoImage(file='pics\\logo.png')
root.iconphoto(False, icon)

# Loading Images
background_back = tk.PhotoImage(file='pics\\gradient_grey.png')
# Image set here for front image
bgl = tk.Label(root, image=background_back).pack()

# Setting up menu buttons
menu_top = tk.Menu(root)
#---------------------------------------#

# 1. Preview menu options
in_preview = tk.Menu(menu_top, tearoff=0)
in_preview.add_command(label='Emission Rates')
in_preview.add_command(label='Predict Emissions')
menu_top.add_cascade(label='Preview', menu=in_preview)

# 2. Help menu options
in_help = tk.Menu(menu_top, tearoff=0)
in_help.add_command(label='About', command=about_win)
in_help.add_command(label='Visit Website', command=visit_web)
in_help.add_command(label='Check Version', command=check_version)
menu_top.add_cascade(label='Help', menu=in_help)


#---------------------------------------#
root.config(menu=menu_top)
root.mainloop()