from colorama import Fore, Style

def BMI_Tester(BMI):
    if BMI < 18.5:
        return Fore.RED + "Underweight" + Style.RESET_ALL
    elif 18.5 <= BMI < 25:
        return Fore.GREEN + "Normal weight" + Style.RESET_ALL
    elif 25 <= BMI < 30:
        return Fore.YELLOW + "Overweight" + Style.RESET_ALL
    else:
        return Fore.LIGHTRED_EX + "Obesity" + Style.RESET_ALL

while True:
    try:
        weight = float(input("ระบุน้ำหนักของคุณ (kg) : "))
        height = float(input("ระบุความสูงของคุณ (m) : "))
        BMI = round(weight / height**2, 2) # ปัดเศษทศนิยมเป็น 2 ตำแหน่ง
        if BMI >= 0:
            result = BMI_Tester(BMI)
            print(Fore.LIGHTCYAN_EX + f"BMI is {BMI}" + Style.RESET_ALL)
            print(result)
            break
        else:
            print(Fore.RED + "กรุณากรอกตัวเลขใหม่" + Style.RESET_ALL)
    except ValueError:
        print(Fore.LIGHTRED_EX + "กรุณากรอกค่าเป็นตัวเลขเท่านั้น" + Style.RESET_ALL)
    except ZeroDivisionError:
        print(Fore.LIGHTRED_EX + "กรุณากรอกค่าความสูงที่ไม่เท่ากับศูนย์" + Style.RESET_ALL)
