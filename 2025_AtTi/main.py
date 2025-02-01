import math
import random

class LunarYear:
    def __init__(self, name:str, count:int) -> None:
        self.yearname = name
        self.yearcount = count
        pass
    def NewYear(self) -> None:
        print(f"Mung xuan vuon minh {self.yearname} {self.yearcount}!")
        print("Cau cho mot nam moi code khong bug, server khong sap, app khong crash!")


def Main():
    AtTi = LunarYear("At Ti", 2025)
    AtTi.NewYear()
    print([f"[iter ${i}] Mung xuan moi!\n" for i in range(int(math.ceil(random.randint(2003, 2025)/100)))])
    pass

if __name__=="__main__":
    Main()