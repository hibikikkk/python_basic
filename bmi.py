def bmi(height, weight):
<<<<<<<<< Temporary merge branch 1
    from_m = height / 100
    return weight / (from_m * from_m)
=========
    m_from_cm = height / 100
    return weight / (m_from_cm * m_from_cm)
>>>>>>>>> Temporary merge branch 2


if __name__ == "__main__":
    input_height = int(input("Height(cm)? > "))
    input_weight = int(input("Weight(kg)? > "))
    bmi_result = round(bmi(input_height, input_weight), 2)

    print(f"Your BMI is {bmi_result}")
