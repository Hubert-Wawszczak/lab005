
import math


class MathData():
    def __init__(self):
        self.ModA = 0.5
        self.ModB = 1.0
        self.ModC = 1.5
        self.ModD = 0
        
        self.ValX = 4.0
        self.ValH = 0.5


    def I2(self):
        return self.ModA

    def A3(self):
        return self.ValH

    def B3(self):
        return self.ValX

    def C3(self):
        return self.I2() * self.B3() * self.B3() * self.B3() + self.I3() * self.B3() * self.B3() + self.I4() * self.B3() + self.I5()

    def I3(self):
        return self.ModB

    def B4(self):
        return self.B3() + self.A3()

    def C4(self):
        return self.I2() * self.B4() * self.B4() * self.B4() + self.I3() * self.B4() * self.B4() + self.I4() * self.B4() + self.I5()

    def I4(self):
        return self.ModC

    def B5(self):
        return self.B4() + self.A3()

    def C5(self):
        return self.I2() * self.B5() * self.B5() * self.B5() + self.I3() * self.B5() * self.B5() + self.I4() * self.B5() + self.I5()

    def I5(self):
        return self.ModD

    def B6(self):
        return self.B3() - self.A3()

    def C6(self):
        return self.I2() * self.B6() * self.B6() * self.B6() + self.I3() * self.B6() * self.B6() + self.I4() * self.B6() + self.I5()

    def B7(self):
        return self.B6() - self.A3()

    def C7(self):
       return self.I2() * self.B7() * self.B7() * self.B7() + self.I3() * self.B7() * self.B7() + self.I4() * self.B7() + self.I5()

    def C8(self):
        return (-3 * self.C3() + 4 * self.C4() - self.C5()) / (2 * self.A3())

    def D8(self):
        return 6 - self.C8()

    def  E8(self):
        return math.Abs(self.D8())

    def C9(self):
        return (self.C7() - 4 * self.C6() + self.C3()) / (2 * self.A3())

    def D9(self):
        return 6 - self.C9()

    def E9(self):
        return math.Abs(self.D9())

    def C10(self):
        return (self.C7() - 8 * self.C6() + 8 * self.C4() - self.C5()) / (12 * self.A3())

    def D10(self):
        return 6 - self.C10()

    def E10(self):
        return math.Abs(self.D10())

    def C13(self):
        return (self.C3() - 2 * self.C4() + self.C5()) / (self.A3() * self.A3())

    def C14(self):
        return (self.C7() - 2 * self.C6() + self.C3()) / (self.A3() * self.A3())

    def C15(self):
        return (self.C6() - 2 * self.C3() + self.C4()) / (self.A3() * self.A3())


    def printResult(self):
        result = "F'(X):\nZwykla 3 = " + str(self.C8())+ "\n"
        result += "Wsteczna 3 = " + str(self.C9()) + "\n"
        result += "Centralna 3 = " + str(self.C10()) + "\n"
        result += "F''(X):\nZwykla 3 = " + str(self.C13()) + "\n"
        result += "Wsteczna 3 = " + str(self.C14())+ "\n"
        result += "Centralna 3 = " + str(self.C15()) + "\n"
        return result


if __name__ == '__main__':
    m = MathData()
    print(m.printResult())

