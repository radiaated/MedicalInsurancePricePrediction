
def preproc(post_data):

    p_data = dict()


    

    p_data['smoker'] = ('yes' if post_data["smoker"] == "on" else 'no') if post_data.get("smoker") else "no"


    if 18 <= int(float(post_data['age'])) < 26:
        p_data['age'] = "18-26"
    elif 26 <= int(float(post_data['age'])) < 41:
        p_data['age'] = "26-41"
    elif 41 <= int(float(post_data['age'])) < 56:
        p_data['age'] = "41-56"
    elif 56 <= int(float(post_data['age'])) <= 64:
        p_data['age'] = "56-64"

    if int(float(post_data['bmi'])) < 18.5:
        p_data['bmi'] = "< 18.5"
    elif 18.5 <= int(float(post_data['bmi'])) < 25:
        p_data['bmi'] = "18.5 - 25"
    elif 25 <= int(float(post_data['bmi'])) < 30:
        p_data['bmi'] = "25 - 30"
    elif 30 <= int(float(post_data['bmi'])) < 35:
        p_data['bmi'] = "30 - 35"
    elif 35 <= int(float(post_data['bmi'])) < 40:
        p_data['bmi'] = "35 - 40"
    elif 40 <= int(float(post_data['bmi'])) <= 54:
        p_data['bmi'] = "40 - 54"

    p_data['children'] = int(float(post_data['children']))
    p_data['sex'] = post_data['sex']
    p_data['region'] = post_data['region']
    p_data['occupation'] = post_data['occupation']
    p_data['medical_history'] = post_data['medical_history']
    p_data['family_medical_history'] = post_data['family_medical_history']

    # 
    # Label Encoding
    # 
    if p_data["sex"] == "male":
        p_data["sex"] = 0
    elif p_data["sex"] == "female":
        p_data["sex"] = 1

    if p_data["age"] == "18-26":
        p_data["age"] = 0
    elif p_data["age"] == "26-41":
        p_data["age"] = 1
    elif p_data["age"] == "41-56":
        p_data["age"] = 2
    elif p_data["age"] == "56-64":
        p_data["age"] = 3

    if p_data["bmi"] == "< 18.5":
        p_data["bmi"] = 0
    elif p_data["bmi"] == "18.5 - 25":
        p_data["bmi"] = 1
    elif p_data["bmi"] == "25 - 30":
        p_data["bmi"] = 2
    elif p_data["bmi"] == "30 - 35":
        p_data["bmi"] = 3
    elif p_data["bmi"] == "35 - 40":
        p_data["bmi"] = 4
    elif p_data["bmi"] == "40 - 54":
        p_data["bmi"] = 5

    if p_data["smoker"] == "yes":
        p_data["smoker"] = 0
    elif p_data["smoker"] == "no":
        p_data["smoker"] = 1


    if p_data["smoker"] == "yes":
        p_data["smoker2"] = 0
    elif p_data["smoker"] == "no":
        p_data["smoker2"] = 1

    
    if p_data["region"] == 'southwest':
        p_data["region"] = 0
    elif p_data["region"] == 'southeast':
        p_data["region"] = 1
    elif p_data["region"] == 'northwest':
        p_data["region"] = 2
    elif p_data["region"] == 'northeast':
        p_data["region"] = 3
    
    if p_data["occupation"] == 'Student':
        p_data["occupation"] = 0
    elif p_data["occupation"] == 'White collar':
        p_data["occupation"] = 1
    elif p_data["occupation"] == 'Unemployed':
        p_data["occupation"] = 2
    elif p_data["occupation"] == 'Blue collar':
        p_data["occupation"] = 3

    if p_data["medical_history"] == 'Heart Disease':
        p_data["medical_history"] = 0
    elif p_data["medical_history"] == 'High Blood Pressure':
        p_data["medical_history"] = 1
    elif p_data["medical_history"] == 'No':
        p_data["medical_history"] = 2
    elif p_data["medical_history"] == 'Diabetes':
        p_data["medical_history"] = 3


    if p_data["family_medical_history"] == 'Heart Disease':
        p_data["family_medical_history"] = 0
    elif p_data["family_medical_history"] == 'High Blood Pressure':
        p_data["family_medical_history"] = 1
    elif p_data["family_medical_history"] == 'No':
        p_data["family_medical_history"] = 2
    elif p_data["family_medical_history"] == 'Diabetes':
        p_data["family_medical_history"] = 3

    if p_data["children"] > 5:
        p_data["children"] = 5

    return p_data
    