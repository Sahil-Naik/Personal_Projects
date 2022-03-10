import time
import tkinter as tk
import tkinter.messagebox
import pandas as pd
import webbrowser as wb
import requests
import time


# Last edited on 10-March-2022 at 4:13 PM.

# Code block to display current time


api_key = "0af67e362c2930a36cacadc49254293d"
base_url = "http://api.openweathermap.org/data/2.5/forecast?"

def about_win():
    # Initializing new window over existing window
    root.withdraw()
    about = tk.Toplevel(root)
    about.geometry('512x130')
    about.title('About')
    about.resizable(False, False)
    info_about_us = "With the use of latest technological advancements in AI,\n" \
                    "we've come up with some of the most amazing solutions for\n" \
                    "one of the most demanding problems of 'Climate Change' by \nUnited Nations."
    # Adding contents to new window
    info = tk.Label(about, text=info_about_us, bd=10, font=('Arial', 12), wraplength=500).pack()

    # Function to return from 'about' page to main page
    def back_to_main():
        about.destroy()
        root.iconify()
        root.deiconify()

    go_back = tk.Button(about, text='Go Back', command=back_to_main).pack()
    about.mainloop()



def visit_web(url='https://sahil7naik57.wixsite.com/upturn-io'):
    wb.open(url)

def check_version():
    tkinter.messagebox.showinfo('Version', 'Version: Pre-Alpha 1.1')

def weather_win():
    get_region_as_text = tk.StringVar()
    root.withdraw()
    nums = '0123456789'


    forecast = tk.Toplevel()
    forecast.geometry("1024x768")
    forecast.title("Weather Forecast")
    forecast.resizable(False, False)
    forecast.wm_attributes('-alpha', 0.98)
    icon_f = tk.PhotoImage(master=forecast,file='pics\\logo.png')
    forecast.iconphoto(False, icon_f)
    background_forecast = tk.PhotoImage(master=forecast,file='pics\\weather_bg2.png')
    bg_f = tk.Label(forecast, image=background_forecast).pack()

    # Function to display current time
    global time1
    time1 = ''
    time_lab = tk.Label(forecast, bg='lightsteelblue', relief='solid', text='HH:MM', bd=1.5,
                        font=('Bahnschrift', 16),
                        justify='center')
    time_lab.place(x=10, y=10, height=50, width=120)

    def tick():
        global time1
        time2 = time.strftime('%H:%M:%S')
        if time2 != time1:
            time1 = time2
            time_lab.config(text=time2)
        time_lab.after(200, tick)

    tick()




    def clicked_search():
        region = get_region_as_text.get()
        for i in region:
            for j in nums:
                if i == j:
                    print("DAMN")
                    tkinter.messagebox.showinfo('Error', 'No such location found!')


        complete_url = base_url + "q=" + region + "&appid=" + api_key
        get_response = requests.get(complete_url)
        x = get_response.json()  # Contains response info about given region
        if x["cod"] != 404:
            k1 = x["list"]  # Contains list of all possible weather information
            k2 = k1[0]  # Uses the first element from list
            k3 = k2["main"]  # Uses 'main' key from dict. to access its values
            k4 = k2["weather"]  # Used to access current weather condition
            k5 = k4[0]  # Uses the first element from weather condition

            current_temp_K = k3["temp"]
            max_temp_K = k3["temp_max"]
            current_press = k3["pressure"]

            cloud_condition = k5["description"]

        weather_des = "Expected to see "+cloud_condition

        current_temp_C = current_temp_K - 273.15
        max_temp_C = max_temp_K - 273.15

        cur_tmp_info = str(round(current_temp_C,2))+"'C"
        current_temp.config(text=cur_tmp_info)

        max_tmp_info = str(round(max_temp_C))+"'C"
        max_temp.config(text=max_tmp_info)

        press_info = str(current_press)+' hPa'
        curnt_press.config(text=press_info)



    search_region = tk.Button(forecast, text="SEARCH", font=('Bahnschrift', 15, 'bold'), command=clicked_search, bg='lightskyblue', bd=1,
                              activebackground='deepskyblue', relief='groove')
    search_region.place(x=470, y=290, width=105)

    enter_region = tk.Entry(forecast, bd=1, textvariable=get_region_as_text, font=('Bahnschrift', 19), justify='center', bg='lightsteelblue')
    enter_region.place(x=375, y=218, height=55, width=295)

    # Labels for temperature information
    current_lab = tk.Label(forecast, bg='lightsteelblue', relief='solid', text="Current Temperature", bd=1.5, font=('Bahnschrift', 15),
                            justify='center')
    current_lab.place(x=90, y=390, height=30, width=240)

    max_lab = tk.Label(forecast, bg='lightsteelblue', relief='solid', text="Max Temperature", bd=1.5, font=('Bahnschrift', 15),
                            justify='center')
    max_lab.place(x=400, y=390, height=30, width=240)

    press_lab = tk.Label(forecast, bg='lightsteelblue', relief='solid', text="Current Pressure", bd=1.5, font=('Bahnschrift', 15),
                            justify='center')
    press_lab.place(x=720, y=390, height=30, width=240)

    # Textbox for temperature information
    current_temp = tk.Label(forecast, bg='whitesmoke', relief='solid', text="-", bd=1, font=('Bahnschrift', 30),
                            anchor='n')
    current_temp.place(x=90, y=420, height=60, width=240)

    max_temp = tk.Label(forecast, bg='whitesmoke', relief='solid', text="-", bd=1, font=('Bahnschrift', 30),
                            anchor='n')
    max_temp.place(x=400, y=420, height=60, width=240)

    curnt_press = tk.Label(forecast, bg='whitesmoke', relief='solid', text="-", bd=1, font=('Bahnschrift', 30),
                            anchor='n')
    curnt_press.place(x=720, y=420, height=60, width=240)


    def forecast_to_main():
        forecast.destroy()
        root.iconify()
        root.deiconify()

    back_to_main = tk.Button(forecast, text="Back", font=('Arial', 13, 'bold'), command=forecast_to_main)
    back_to_main.place(x=935, y=720, width=65)
    forecast.mainloop()



# Main window (root) which will be showed when software runs
root = tk.Tk()
root.configure()
root.attributes('-alpha', 0.97)
root.geometry("1024x768")
root.title("Climate Action")
root.resizable(False, False)

icon = tk.PhotoImage(file='pics\\logo.png')
root.iconphoto(False, icon)

background_back = tk.PhotoImage(file='pics\\gradient_grey.png')
bg_m = tk.Label(root, image=background_back).pack()

#--------Buttons for menu bar start here-------------#
menu_top = tk.Menu(root)

# 1. Preview menu option
in_preview = tk.Menu(menu_top, tearoff=0)
in_preview.add_command(label='Emission Rates')
in_preview.add_command(label='Predict Emissions')
in_preview.add_command(label="Weather Forecast" , command=weather_win)
menu_top.add_cascade(label='Preview', menu=in_preview)

# 2. Help menu option
in_help = tk.Menu(menu_top, tearoff=0)
in_help.add_command(label='About', command=about_win)
in_help.add_command(label='Visit Website', command=visit_web)
in_help.add_command(label='Check Version', command=check_version)
menu_top.add_cascade(label='Help', menu=in_help)

# 3. Exit menu option
menu_top.add_cascade(label='Exit', command=root.destroy)

#--------Buttons for menu bar end here-------------#

# Main window closes here
root.config(menu=menu_top)
root.mainloop()