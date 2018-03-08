class Person:
    def __init__(self,initialAge):
        self.__age = initialAge
        if self.__age < 0:
            self.__age = 0
            print("Age is not valid, setting age to 0.")

    def amIOld(self):
        if self.__age < 13:
            print("You are young.")
            return
        if self.__age < 18:
            print("You are a teenager.")
            return
        print("You are old.")

    def yearPasses(self):
        self.__age += 1