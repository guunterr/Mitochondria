class Capacitor():
    def __init__(self, _capacitance = 20): #back of the envelope default
        print("initiated") #Capacitance in microfarads
        self.capacitance = _capacitance
        self.idealvoltage = 140 * 10^3 #Required voltage in volts
    def changeC(self, _c):
        self.capacitance = _c

class Supply():
    def __init__(self, _voltage = 500 * 10^3):
        voltage = _voltage

class Circuit(Capacitor, Resistor, Supply):
    def __init__():
        self.voltage = Supply.voltage

