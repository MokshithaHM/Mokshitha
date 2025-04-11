import tkinter as tk
from time import strftime
import math


root = tk.Tk()
root.title("Circular Digital Clock")


root.geometry("600x600")
root.resizable(False, False)


canvas = tk.Canvas(root, width=600, height=600, bg="#2e2e2e", bd=0, highlightthickness=0)
canvas.pack()


center_x, center_y = 300, 300  
radius = 250  


def update_time():
    current_time = strftime('%I:%M:%S %p')  
    current_hour = int(strftime('%I'))  
    current_minute = int(strftime('%M'))
    current_second = int(strftime('%S'))  
    
    
    time_label.config(text=current_time)
    
    
    canvas.delete("all")
    

    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
                       outline="#FFFFFF", width=5)

   
    canvas.create_text(center_x, center_y - radius + 20, text="12", fill="#FFFFFF", font=("Helvetica", 20, "bold"))
    canvas.create_text(center_x + radius - 20, center_y, text="3", fill="#FFFFFF", font=("Helvetica", 20, "bold"))
    canvas.create_text(center_x, center_y + radius - 20, text="6", fill="#FFFFFF", font=("Helvetica", 20, "bold"))
    canvas.create_text(center_x - radius + 20, center_y, text="9", fill="#FFFFFF", font=("Helvetica", 20, "bold"))
    
   
    hour_angle = (current_hour % 12 + current_minute / 60) * 30 
    draw_hand(hour_angle, radius * 0.5, 10, "#FF0000")  

 
    minute_angle = (current_minute + current_second / 60) * 6  
    draw_hand(minute_angle, radius * 0.7, 6, "#00FF00") 


    second_angle = current_second * 6  
    draw_hand(second_angle, radius * 0.8, 2, "#0000FF") 

    canvas.after(1000, update_time)


def draw_hand(angle, length, width, color):
    
    angle_rad = math.radians(angle - 90)  
    x_end = center_x + length * math.cos(angle_rad)
    y_end = center_y + length * math.sin(angle_rad)
    
    
    canvas.create_line(center_x, center_y, x_end, y_end, fill=color, width=width)


time_label = tk.Label(root, font=("Helvetica", 40, "bold"), bg="#2e2e2e", fg="#FFFFFF")
time_label.place(relx=0.5, rely=0.5, anchor="center")


update_time()


root.mainloop()
