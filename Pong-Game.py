import random
import time
import tkinter as tk
from ttkbootstrap import ttk
from tkinter import messagebox

xaxis, yaxis, User1, User2, time_speed = 0, 0, 0, 0, 0


selected_square = []

released,afterid,moving_to_x_axis,moving_to_y_axis,time_duration=False,None,1,0,30

square_exits=True
choosed_time=False
speed = 50
check = 10


def on_button_press(event):


    global  selected_square,xaxis,yaxis,released
    x = canvas.coords(square)
    for i in squares:
        x = canvas.coords(i)
        if x[0] <= event.x <= x[2] and x[1] <= event.y <= x[3]:
            print("succcess")
            selected_square = i
            xaxis = event.x - x[0]
            yaxis = event.y - x[1]
            released = True
            break


def CheckSquare(side, point):
    global User1,User2
    if side == "left":
        User1 += point
    else:
        User2 += point


def CheckCollisonOnRoofOrFloor():
    global moving_to_y_axis
    x = canvas.coords(square3)

    if x[1] < 1 or x[3] > 400:  # Assuming the canvas height is 400
        moving_to_y_axis = -moving_to_y_axis  # Reverse the vertical movement direction
        print("gullet")





def moving_square():
    global afterid, moving_to_x_axis, time_speed, speed, check, moving_to_y_axis
    if not choosed_time:
        messagebox.showerror(message="Choose Seconds To UYse On The Game...")
        return
    time_speed += 0.1

    if int(time_speed) == check:
        speed -= 2
        check += 20
    canvas.move(square3, 5 * moving_to_x_axis, moving_to_y_axis)
    direct = canvas.coords(square1)
    direct2 = canvas.coords(square)
    x = canvas.coords(square3)

    CheckCollisonOnRoofOrFloor()


    if x[2] + 10 > direct[0] and x[3] > direct[1]:
        if x[3] < (direct[1] + direct[3]) / 2:
            moving_to_x_axis = -1
            randomData=random.choice([4,6,5,7])

            moving_to_y_axis = randomData
        else:
            moving_to_x_axis = -1
            randomData=random.choice([4,6,5,7])

            moving_to_y_axis = -randomData
    if x[0] - 10 < direct2[2] and x[3] > direct2[1]:
        if x[3] < (direct2[1] + direct2[3]) / 2:
            moving_to_x_axis = 1
            randomData=random.choice([4,6,5,7])

            moving_to_y_axis = randomData
        elif x[3] == (direct2[1] + direct2[3]) / 2:
            moving_to_x_axis = 1

            moving_to_y_axis = 0
        else:
            moving_to_x_axis = 1
            randomData=random.choice([4,6,5,7])
            moving_to_y_axis = -randomData
    else:
        if x[2] > 390 or x[0] <40:
            game_over()
            return


    afterid = canvas.after(50, moving_square)


def button_release(event):
    global released
    released = False


def on_mouse_drag(event):
    if released:
        y1 = event.y - yaxis
        if selected_square == squares[0]:
            canvas.coords(selected_square, 350, y1, 400, y1 + 100)
        else:
            canvas.coords(selected_square, 0, y1, 50, y1 + 100)


def timeleft():
    global time_duration
    if not choosed_time:
        messagebox.showerror(message="Choose Seconds To UYse On The Game...")
        return
    if time_duration > 0 and square_exits:
        time_duration -= 1
        print(time_duration)
        root.after(1000, timeleft)
        game_duration_label.configure(text=f"Time Left: {time_duration}")
    else:
        if square_exits:
            game_over()



def NumberOfMinutes():
    global time_duration,choosed_time
    if time_duration<10:
        messagebox.showerror(message="Number Must Be In Seconds And Greater Than 10 seconds")
        return
    time_duration=int(entry.get())
    game_duration_label.configure(text=f"Time Left : {time_duration}")
    choosed_time=True




def StartGame():
    timeleft()
    if choosed_time:
        moving_square()


def game_over():
    global afterid,square_exits

    canvas.after_cancel(afterid)
    canvas.delete(square3)
    square_exits=False
    print(f"User 1 Score Is   {User1}")
    print(f"User 2 Score Is   {User2}")
    winner = "User1" if User1 > User2 else "User2" if User2 > User1 else "Draw By Jury"
    if "1" in winner or "2" in winner:
        game_duration_label.configure(text=f"The Winner Is : {winner}")
    else:
        game_duration_label.configure(text=f"{winner}")
    root.after(5000,root.destroy)

import tkinter as tk
from ttkbootstrap import ttk

root = tk.Tk()





game_duration_label = tk.Label(root, text=f"Time left: {time_duration} ")
game_duration_label.pack()

# Create the canvas and shapes
canvas = tk.Canvas(root, bg="black", width=400, height=400)
square = canvas.create_rectangle(0, 100, 50, 200, fill="blue")
square1 = canvas.create_rectangle(350, 100, 400, 200, fill="blue")
square3 = canvas.create_oval(200, 100, 250, 150, fill="red")

# Pack the canvas
canvas.pack()

entry_button_frame = tk.Frame(root)
entry_button_frame.pack()

entry = ttk.Entry(entry_button_frame)
button1 = ttk.Button(entry_button_frame, text="Button",command=NumberOfMinutes)
button2 = ttk.Button(entry_button_frame, style="blue-outline" ,cursor="hand2", text="StartGame",command=StartGame)

entry.pack(side=tk.LEFT,padx=(0,10))
button2.pack(side=tk.RIGHT ,padx=(0,10))
button1.pack(side=tk.RIGHT,padx=(0,10))




canvas.bind('<ButtonPress-1>', on_button_press)
canvas.bind('<ButtonRelease-1>', button_release)
canvas.bind('<B1-Motion>', on_mouse_drag)

squares = [square1, square]



root.mainloop()

