import time
import tkinter as tk
import tkinter.messagebox
import pandas as pd
import webbrowser as wb
import requests
import time

# Last edited on 11-March-2022 at 5:29 PM.

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
    forecast.geometry("1024x768+300+50")
    forecast.title("Weather Forecast")
    forecast.resizable(False, False)
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

    back_to_main = tk.Button(forecast, text="Back", font=('Bahnshcrift', 13, 'bold'), command=forecast_to_main)
    back_to_main.place(x=935, y=720, width=65)
    forecast.mainloop()

def emission_win():
    def open_my_climate(url='https://sahil7naik57.wixsite.com/upturn-io/general-6'):
        wb.open(url)

    def clicked_ge20():
        back_to_main.destroy()
        global_emit_2017.config(state='disabled')
        global_Gemit_2017.config(state='disabled')
        global_Gemit_20ys.config(state='disabled')
        big_manufac.config(state='disabled')
        learn_more.config(state='disabled')

        def back_to_emit():
            emit.destroy()
            emission_win()

        # Option 1 functions


        op1_head = tk.Label(emit, text="Global Emission over past 20 years", font=('Bahnshcrift', 25), justify='center', bg='black', fg='orange')
        op1_head.place(x=355, y=0, width=670, height=70)

        op1_back = tk.Button(emit, text="Back", font=('Bahnshcrift', 13, 'bold'), command=back_to_emit, bg='black', bd=0, fg='white')
        op1_back.place(x=675, y=730, width=65)


    def clicked_ge17():
        back_to_main.destroy()
        global_emit_20ys.config(state='disabled')
        global_Gemit_2017.config(state='disabled')
        global_Gemit_20ys.config(state='disabled')
        big_manufac.config(state='disabled')
        learn_more.config(state='disabled')

        def back_to_emit():
            emit.destroy()
            emission_win()
        # Option 2 functions
        op2_stats_lab = tk.Label(emit).place(x=355,y=70,width=675,height=698)
        op2_head = tk.Label(emit, text="Global Emission in 2017", font=('Bahnshcrift', 25), justify='center', bg='black', fg='orange')
        op2_head.place(x=355, y=0, width=670, height=70)

        op2_back = tk.Button(emit, text="Back", font=('Bahnshcrift', 13, 'bold'), command=back_to_emit, bg='black', bd=0, fg='white')
        op2_back.place(x=675, y=730, width=65)

    def clicked_Gge20():
        back_to_main.destroy()
        global_emit_20ys.config(state='disabled')
        global_Gemit_2017.config(state='disabled')
        global_emit_2017.config(state='disabled')
        big_manufac.config(state='disabled')
        learn_more.config(state='disabled')
        def back_to_emit():
            emit.destroy()
            emission_win()
        # Option 3 functions
        op3_stats_lab = tk.Label(emit).place(x=355,y=70,width=675,height=698)
        op3_head = tk.Label(emit, text="Global Greenhouse Emission over past 20 years", font=('Bahnshcrift', 22), justify='center', bg='black', fg='orange')
        op3_head.place(x=355, y=0, width=670, height=70)

        op3_back = tk.Button(emit, text="Back", font=('Bahnshcrift', 13, 'bold'), command=back_to_emit, bg='black', bd=0, fg='white')
        op3_back.place(x=675, y=730, width=65)

    def clicked_Gge17():
        back_to_main.destroy()
        global_emit_20ys.config(state='disabled')
        global_emit_2017.config(state='disabled')
        global_Gemit_20ys.config(state='disabled')
        big_manufac.config(state='disabled')
        learn_more.config(state='disabled')
        def back_to_emit():
            emit.destroy()
            emission_win()
        # Option 4 functions
        op4_stats_lab = tk.Label(emit).place(x=355,y=70,width=675,height=698)
        op4_head = tk.Label(emit, text="Global Greenhouse Emission in 2017", font=('Bahnshcrift', 25), justify='center', bg='black', fg='orange')
        op4_head.place(x=355, y=0, width=670, height=70)

        op4_back = tk.Button(emit, text="Back", font=('Bahnshcrift', 13, 'bold'), command=back_to_emit, bg='black', bd=0, fg='white')
        op4_back.place(x=675, y=730, width=65)

    def clicked_lm20():
        back_to_main.destroy()
        global_emit_20ys.config(state='disabled')
        global_Gemit_2017.config(state='disabled')
        global_Gemit_20ys.config(state='disabled')
        global_emit_2017.config(state='disabled')
        learn_more.config(state='disabled')
        def back_to_emit():
            emit.destroy()
            emission_win()
        # Option 5 functions
        op5_stats_lab = tk.Label(emit).place(x=355,y=70,width=675,height=698)
        op5_head = tk.Label(emit, text="Largest Manufacturer over 20 years", font=('Bahnshcrift', 25), justify='center', bg='black', fg='orange')
        op5_head.place(x=355, y=0, width=670, height=70)

        op5_back = tk.Button(emit, text="Back", font=('Bahnshcrift', 13, 'bold'), command=back_to_emit, bg='black', bd=0, fg='white')
        op5_back.place(x=675, y=730, width=65)



    root.withdraw()
    emit = tk.Toplevel()
    emit.geometry("1024x768+300+50")
    emit.title("Gaseous Emissions")
    emit.resizable(False, False)
    icon_f = tk.PhotoImage(master=emit,file='pics\\logo.png')
    emit.iconphoto(False, icon_f)
    background_emit = tk.PhotoImage(master=emit,file='pics\\emit_bg2.png')
    bg_f = tk.Label(emit, image=background_emit).pack()
    separator = tk.Frame(emit, bg='orange').place(x=350, y=0, width=5, height=768)

    # Buttons on the Left-side of Window
    global_emit_20ys = tk.Button(emit, text='GLOBAL EMISSION\nOVER PAST 20 YEARS', font=('Bahnschrift', 13),
                                 command=clicked_ge20, bg='midnightblue',fg='white')
    global_emit_20ys.place(x=0,y=0, width=350, height=150)

    global_emit_2017 = tk.Button(emit, text='GLOBAL EMISSION IN 2017', font=('Bahnschrift', 13),bg='midnightblue',
                                 fg='white', command=clicked_ge17)
    global_emit_2017.place(x=0,y=150, width=350, height=150)

    global_Gemit_20ys = tk.Button(emit, text='GLOBAL GREENHOUSE EMISSION\nOVER PAST 20 YEARS', font=('Bahnschrift', 13),
                                  bg='midnightblue',fg='white', command=clicked_Gge20)
    global_Gemit_20ys.place(x=0,y=300, width=350, height=150)

    global_Gemit_2017 = tk.Button(emit, text='GLOBAL GREENHOUSE\nEMISSION IN 2017', font=('Bahnschrift', 13),
                                  bg='midnightblue',fg='white', command=clicked_Gge17)
    global_Gemit_2017.place(x=0,y=450, width=350, height=150)

    big_manufac = tk.Button(emit, text='LARGEST MANUFACTURER OVER 20 YEARS', font=('Bahnschrift', 13),bg='midnightblue',
                            fg='white', command=clicked_lm20)
    big_manufac.place(x=0,y=600, width=350, height=90)

    learn_more = tk.Button(emit, text='LEARN MORE', font=('Bahnschrift', 13,'bold','underline'),bg='midnightblue',
                           fg='white', command=open_my_climate)
    learn_more.place(x=0,y=690, width=350, height=78)



    def emit_to_main():
        emit.destroy()
        root.iconify()
        root.deiconify()

    back_to_main = tk.Button(emit, text="Back", font=('Bahnshcrift', 13, 'bold'), command=emit_to_main, bg='gray', bd=0)
    back_to_main.place(x=935, y=720, width=65)
    emit.mainloop()




# Main window (root) which will be showed when software runs
root = tk.Tk()
root.geometry("1024x768+300+50")
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
in_preview.add_command(label='Emission Rates', command=emission_win)
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
