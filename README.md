Clinical Calculator
A simple command-line Python tool that performs three common clinical laboratory calculations. 
I built it as a medical laboratory science student to practice Python while working with the kind of values I see in the lab.
Disclaimer: This project is for educational purposes only. It is not a medical device and must not be used to make clinical decisions.
Features
1. LDL cholesterol calculator: estimates LDL from total cholesterol, HDL and triglycerides.
2. Fasting blood glucose (FBG) interpreter: classifies a result as normal, prediabetes or diabetes range.
3. eGFR estimator: estimates kidney function from age, sex and serum creatinine.
   
How it works
-LDL Friedewald equation: LDL = Total Cholesterol - HDL - (Triglycerides / 5)
-FBG Fasting glucose cutoffs (mg/dL): below 100 normal, 100-125 prediabetes, 126 and above diabetes
-eGFR CKD-EPI 2021 creatinine equation, using sex-specific constants
Note: The Friedewald equation is only reliable when triglycerides are below 400 mg/dL. All values are in mg/dL.
Requirements
• Python 3.x (no external libraries needed)

How to run
python ldl_calculator.py
You will see a menu:
Clinical Calculator Menu:
1. Calculate LDL  
2. Interpret Fasting Blood Glucose (FBG)
3. Estimate eGFR
4. Exit
Enter your choice (1-4):
Enter a number, follow the prompts, and the result is printed in the terminal.

What I learned
• Writing and organizing functions in Python
• Using conditionals and a menu loop for user interaction
• Translating clinical formulas into code

• Support for mmol/L units
Author
Onyinye Nweke
