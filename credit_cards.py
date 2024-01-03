def apply_credit_card(income):
    if income < 15000:
        return "คุณไม่ได้รับสิทธิ์ทำบัตรเครดิต"
    elif 15000 <= income < 70000:
        return "คุณได้รับสิทธิ์ทำบัตรเครดิตเงินสด"
    elif 70000 <= income < 100000:
        return "คุณได้รับสิทธิ์ทำบัตรเครดิตทอง"
    else:
        return "คุณได้รับสิทธิ์ทำบัตรเครดิต Platinum"

# ตัวอย่างการใช้งาน
income = float(input("กรุณากรอกรายได้ของคุณ: "))
result = apply_credit_card(income)
print(result)
