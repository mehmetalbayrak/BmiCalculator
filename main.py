import tkinter

def calculate_bmi():
    height= height_input.get()
    weight= weight_input.get()
    if weight =="" or height =="":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmi =float(weight) / (float(height) / 100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number")

def write_result(bmi):
    result_string = f"Your BMI is {round(bmi,2)} you are "
    if bmi <= 16:
        result_string += "severaly thin!"
    elif bmi > 16 and bmi <= 17:
        result_string += "moderately thin!"
    elif bmi > 17 and bmi <=18.5:
        result_string += "mild thin!"
    elif bmi > 18.5 and bmi <=25:
        result_string += "normal"
    elif bmi > 25 and bmi <= 30:
        result_string += "overweight"
    elif bmi > 30 and bmi <= 35:
        result_string += "obese class 1"
    elif bmi > 35 and bmi <= 40:
        result_string += "obese class 2"
    else:
        result_string += "obese class 3"
    return result_string

window = tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=30, pady=30)

weight_input_label = tkinter.Label(text="Enter your weight (kg)")
weight_input_label.pack()

weight_input = tkinter.Entry(width=15)
weight_input.pack()

height_input_label = tkinter.Label(text="Enter your height (cm)")
height_input_label.pack()

height_input = tkinter.Entry(width=15)
height_input.pack()

calculate_button = tkinter.Button(text="Calculate", command=calculate_bmi)
calculate_button.pack()

result_label = tkinter.Label()
result_label.pack()


window.mainloop()