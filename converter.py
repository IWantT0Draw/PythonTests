import tkinter as tk

def convert_to_dec(InputNumber, Base):

    OutputNumber = int(str(InputNumber), Base)

    return OutputNumber

def convert_from_dec(InputNumber, Base):

    Numbers = {
        10:"A",
        11:"B",
        12:"C",
        13:"D",
        14:"E",
        15:"F",
        16:"G",
        17:"H",
        18:"I",
        19:"J",
        20:"K",
        21:"L",
        22:"M",
        23:"N",
        24:"O",
        25:"P",
        26:"Q",
        27:"R",
        28:"S",
        29:"T",
        30:"U",
        31:"V",
        32:"W",
        33:"X",
        34:"Y",
        35:"Z"

    }

    OutputNumber = str()
    Modlist = list()

    while InputNumber > 0:
        ModNumber = InputNumber % Base
        if ModNumber > 9:
            Modlist.insert(0, str(Numbers[ModNumber]))
        else:
            Modlist.insert(0, str(ModNumber))

        InputNumber //= Base

    OutputNumber = "".join(Modlist)

    return OutputNumber

def convert(Number, BaseFrom, BaseTo):
    return convert_from_dec(convert_to_dec(Number, BaseFrom), BaseTo)

def button_command():
    Output = convert(NumberEntered.get(), InputBaseEntered.get(), OutputBaseEntered.get())
    OutputNumber.delete(0, tk.END)
    OutputNumber.config(width=2+len(Output))
    OutputNumber.insert(0, Output)

main = tk.Tk()
main.title("Converter")

NumberEntered = tk.StringVar()
InputBaseEntered = tk.IntVar()
OutputBaseEntered = tk.IntVar()

frame = tk.Frame(main)
frame2 = tk.Frame(main)
frame3 = tk.Frame(main)

InputNumberLabel = tk.Label(frame, text="Number to convert")
InputBaseLabel = tk.Label(frame, text="Base converted from")
OutputBaseLabel = tk.Label(frame2, text="Base converted to")
OutputNumberLabel = tk.Label(frame3, text="Converted Number")

InputNumber = tk.Entry(frame, textvariable=NumberEntered)

InputBase = tk.Spinbox(frame, width=10, justify="center", wrap=True, from_=2, to=36, textvariable=InputBaseEntered)

OutputBase = tk.Spinbox(frame2, width=10, justify="center", wrap=True, from_=2, to=36, textvariable=OutputBaseEntered)

OutputNumber = tk.Entry(frame3, width=10, justify="center")

ConvertButton = tk.Button(frame3, text="Convert", cursor="hand2", command=button_command)

frame.pack()
frame2.pack()
frame3.pack()
InputNumberLabel.pack()
InputNumber.pack(fill="x")
InputBaseLabel.pack(side=tk.LEFT)
InputBase.pack(pady=10, padx=5)
OutputBaseLabel.pack(side=tk.LEFT)
OutputBase.pack(pady=10, padx=5)
ConvertButton.pack(pady=10)
OutputNumberLabel.pack()
OutputNumber.pack(fill="both",expand=True)

main.mainloop()