
def fahrenheit_to_celsius(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp


def cm_to_inch(cm):
    return cm / 2.54


temp_f = float(input("변환할 화씨 온도(F)를 입력하세요: "))
result_c = fahrenheit_to_celsius(temp_f)
print(f"화씨 {temp_f}F는 섭씨 {result_c:.2f}C입니다.")

#길이변환
length_cm = float(input("변환할 길이(cm)를 입력하세요: "))
result_inch = cm_to_inch(length_cm)
print(f"{length_cm}cm는 {result_inch:.2f}inch입니다.") 