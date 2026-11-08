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

def convert_to_dec(InputNumber, Base):

    OutputNumber = int(str(InputNumber), Base)

    return OutputNumber

print(convert_to_dec("Z", 36))