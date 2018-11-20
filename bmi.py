def bmi(height, weight):
<<<<<<< HEAD
    m_from_cm = height / 100
    return weight / (m_from_cm * m_from_cm)
=======
    from_m = height / 100
    return weight / (from_m * from_m)
>>>>>>> origin/master


if __name__ == "__main__":
    input_height = int(input("Height(cm)? > "))
    input_weight = int(input("Weight(kg)? > "))
    bmi_result = round(bmi(input_height, input_weight), 2)

    print(f"Your BMI is {bmi_result}")
