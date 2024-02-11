import os

class LunarYear:
    def __init__(self, name:str, count:int) -> None:
        self.yearname = name
        self.yearcount = count
        pass
    def NewYear(self) -> None:
        print(f"Mung xuan {self.yearname} {self.yearcount}!")
        print("Cau cho mot nam moi code khong bug, server khong sap, app khong crash!")


def Main():
    GiapThin = LunarYear("Giap Thin", 2024)
    GiapThin.NewYear()
    pass

if __name__=="__main__":
    Main()