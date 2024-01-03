def calculate_grade(score):
    if score >= 80:
        return "A"
    elif 70 <= score <= 79:
        return "B"
    elif 60 <= score <= 69:
        return "C"
    elif 50 <= score <= 59:
        return "D"
    else:
        return "F"

# ตัวอย่างการใช้งาน
while True:
    try:
        score = int(input("กรุณากรอกคะแนน: "))
        if 0 <= score <= 100:
            result = calculate_grade(score)
            print(f"คะแนน {score} มีเกรดเท่ากับ {result}")
            break  # จบ loop หลังจากได้คะแนนที่ถูกต้อง
        else:
            print("กรุณากรอกคะแนนในช่วง 0-100 เท่านั้น")
    except ValueError:
        print("กรุณากรอกค่าเป็นตัวเลขเท่านั้น")