# Lab 1 Mini-Project
# Student: Adil Rahman Akash
# Description: Simple Annual Compounding Calculator

import math

def main():
    # Input and conversion
    principal = float(input("Enter principal: "))
    rate = float(input("Enter annual interest rate (e.g., 4.5): "))
    years = int(input("Enter number of years: "))

    # Compute using math module
    # Using math.pow for the compounding calculation
    amount = principal * math.pow((1 + rate / 100), years)

    # Output formatting
    print(f"\nInputs: Principal=${principal}, Rate={rate}%, Years={years}")
    print(f"Final Amount: ${round(amount, 2)}") 
    
    # Rounded to 2 decimal places

    if amount >= 2 * principal:
        print("Higher than double")
    else:
        print("Less than double")

if __name__ == "__main__":
    main()