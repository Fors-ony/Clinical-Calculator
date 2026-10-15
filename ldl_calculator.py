
def calc_ldl(total_cholesterol, hdl, triglycerides):
    ldl = total_cholesterol - hdl - (triglycerides/5)
    return ldl

def interpret_fbg(fbg):
    if fbg < 100:
        return "Normal range"
    elif 100 <=fbg <=125:
        return "Prediabetes range"
    else:
        return "Diabetes range"


def estimate_egfr(age, sex , serum_creatinine):
    if sex.lower()== "female":
        k=0.7
        alpha= -0.241
        sex_factor=1.012
    elif sex.lower()=="male":
        k=0.9
        alpha=-0.302
        sex_factor=1.0
    else:
        return "invalid sex input"

    ratio=serum_creatinine/k
    lower= min(ratio,1)**alpha
    upper=max(ratio,1)**-1.200
    egfr=142*lower*upper*(0.9938**age)*sex_factor
    return egfr
    


while True:
    print("Clinical Calculator Menu:")
    print("1. Calculate LDL")
    print("2. Interpret Fasting Blood Glucose (FBG)")
    print("3. Estimate eGFR")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice== "1":
        total_cholesterol= float(input("Enter total cholestrol: "))
        hdl= float(input("Enter hdl: "))
        triglycerides= float(input("Enter triglycerides: "))
        answer_ldl=calc_ldl(total_cholesterol, hdl, triglycerides)
        print(answer_ldl)

    elif choice=="2":
        fbg = float(input("Enter fasting blood glucose (mg/dl): "))
        result = interpret_fbg(fbg)
        print(result)

    elif choice=="3":
        age=int(input("Enter age:"))
        sex= input("Enter sex :")
        serum_creatinine= float(input("Enter serum creatinine (mg/dl): "))

        egfr=estimate_egfr(age, sex, serum_creatinine)
        print(f"Estimated eGFR: {egfr:.2f} mL/min/1.73m²")

    elif choice=="4":
        print("Exiting the calculator. See ya!")
        break
    else:
        print("Invalid choice. Please select a valid option.")





