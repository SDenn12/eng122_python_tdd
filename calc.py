class SimpleCalc:

    def add(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        if value2 == 0:
            return "division by zero is not allowed"
        return value1/value2

    def dob(self, day, month):
        days = {
            "1":31,
            "2":28,
            "3":31,
            "4":30,
            "5":31,
            "6":30,
            "7":31,
            "8":31,
            "9":30,
            "10":31,
            "11":30,
            "12":31
        }
        for i in days.keys():
            if i == str(month):
                if 1 <= day <= days[i]:
                    return f"{day}/{month}"
        else:
            return "Date is out of bounds"


    def percentage(self, value1, value2):
        if value2 == 0:
            return f"division by zero is not allowed"
        return f"{round(100 * value1 / value2,1)}%"

    def cm_m(self,centi):
        return round(centi/100, 2)

