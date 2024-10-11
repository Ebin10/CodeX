def calculate_dosage(body_weight, drug, adjustment_factor=1.0):
    # Define dosage calculation formula for each drug
    dosage_formulas = {
        "Cisplatin": 5 * body_weight,  # Example dosage formula (5 mg/kg)
        "Carboplatin": 6 * body_weight,  # Example dosage formula (6 mg/kg)
        "Paclitaxel": 10 * body_weight,  # Example dosage formula (10 mg/kg)
        "Docetaxel": 8 * body_weight,  # Example dosage formula (8 mg/kg)
        "Cyclophosphamide": 15 * body_weight,  # Example dosage formula (15 mg/kg)
        "Doxorubicin": 2 * body_weight,  # Example dosage formula (2 mg/kg)
        "5-Fluorouracil": 20 * body_weight,  # Example dosage formula (20 mg/kg)
        "Methotrexate": 3 * body_weight,  # Example dosage formula (3 mg/kg)
        "Vinblastine": 1 * body_weight,  # Example dosage formula (1 mg/kg)
        "Vincristine": 0.1 * body_weight,  # Example dosage formula (0.1 mg/kg)
    }
    
    # Check if the drug is in the dictionary
    if drug in dosage_formulas:
        dosage = dosage_formulas[drug] * adjustment_factor
        return dosage
    else:
        return None  # Return None if the drug is not found in the dictionary

def convert_dosage_units(dosage, current_unit, target_unit):
    conversion_factors = {
        "mg": 1,
        "mcg": 1000,
    }
    if current_unit in conversion_factors and target_unit in conversion_factors:
        conversion_factor = conversion_factors[current_unit] / conversion_factors[target_unit]
        return dosage * conversion_factor
    else:
        return None

def check_drug_interactions(drug):
    # Placeholder function for drug interaction checking
    # In a real-world scenario, this function would check a database of known drug interactions
    # and return any potential interactions with the specified chemotherapy drug.
    return []

def main():
    try:
        # Get user input for body weight
        body_weight = float(input("Enter the body weight in kilograms: "))
        
        # Get user input for the drug
        drug = input("Enter the chemotherapy drug (e.g., Cisplatin, Paclitaxel, etc.): ").strip().capitalize()
        
        # Calculate dosage
        dosage = calculate_dosage(body_weight, drug)
        
        # Display the dosage
        if dosage is not None:
            print("The dosage of {} for cancer treatment based on body weight {} kg is {} mg.".format(drug, body_weight, dosage))
            
            # Convert dosage units
            current_unit = "mg"
            target_unit = input("Enter the target unit for dosage conversion (mg or mcg): ").strip().lower()
            converted_dosage = convert_dosage_units(dosage, current_unit, target_unit)
            if converted_dosage is not None:
                print("Converted dosage: {} {}".format(converted_dosage, target_unit))
            else:
                print("Invalid unit specified for conversion.")
            
            # Check drug interactions
            interactions = check_drug_interactions(drug)
            if interactions:
                print("Potential drug interactions:")
                for interaction in interactions:
                    print("- " + interaction)
            else:
                print("No known drug interactions found.")
            
            # Adjust dosage based on factors (e.g., renal function, liver function)
            adjustment_factor = float(input("Enter adjustment factor (1.0 for no adjustment): "))
            adjusted_dosage = calculate_dosage(body_weight, drug, adjustment_factor)
            if adjusted_dosage is not None:
                print("Adjusted dosage: {} mg".format(adjusted_dosage))
            else:
                print("Invalid adjustment factor.")
        else:
            print("Sorry, the drug '{}' is not found in the list.".format(drug))
        
    except ValueError:
        print("Please enter a valid numeric value for body weight or adjustment factor.")

if __name__ == "__main__":
    main()
