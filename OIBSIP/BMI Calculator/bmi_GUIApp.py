import tkinter

root = tkinter.Tk()
root.title("My BMI Calculator")
root.geometry("600x400")

def delete():
    entry_weight.delete(0,"end")
    entry_height.delete(0,"end")
    label_result['text']=f"Please Enter Height and Weight"

def calculateBMI():
    weight=float(entry_weight.get())
    height=float(entry_height.get())
    bmi=round(weight/(height**2), 2)
    if bmi<18.5:
        FinalBmi=f"Your BMI :{bmi} - You are Underweight, Regular Exercise can help you"

    elif bmi>=18.5 and bmi<25:
        FinalBmi=f"Your BMI :{bmi} - You are Healty "

    elif bmi>=25 and bmi<=30: 
        FinalBmi=f"Your BMI :{bmi} - You are Overweight, Regular Exercise can help you"

    else:
        FinalBmi=f"Your BMI :{bmi} - Obese, please do consult with doctor "
        
    label_result['text']= FinalBmi


#Crearing GUI for Application
label_weight = tkinter.Label(root, text="Weight in KG :")
label_weight.pack()

entry_weight = tkinter.Entry(root, bd=8)
entry_weight.pack()

label_height = tkinter.Label(root,bd=8, text="Height in mtr :")
label_height.pack()

entry_height = tkinter.Entry(root,bd=6)
entry_height.pack()


label_result = tkinter.Label(root, bd=8, text="Please Enter Height and Weight ")
label_result.pack()

button_calculate = tkinter.Button(root,bg="#2187e7", bd=10,
                                  text="Calculate",
                                  command=calculateBMI)
button_calculate.pack()

button_clear = tkinter.Button(root,bg="#4187f7", bd=10,
                                  text="    Clear  ",
                                  command=delete)
button_clear.pack()


root.mainloop()
