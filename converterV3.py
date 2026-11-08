import base_conversion_kit as bck, tkinter as tk # type: ignore

def convert(Number, BaseFrom, BaseTo):
    return bck.convert_base(Number, BaseFrom, BaseTo)


def button_command():
    OutputNumber.delete(0, tk.END)
    OutputNumber.config(width=4+len(convert(NumberEntered.get(), InputBaseEntered.get(), OutputBaseEntered.get())))
    OutputNumber.insert(0, convert(NumberEntered.get(), InputBaseEntered.get(), OutputBaseEntered.get()))

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

OutputNumber = tk.Entry(frame3, justify="center")

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
OutputNumber.pack(fill="both", expand=True)


main.mainloop()