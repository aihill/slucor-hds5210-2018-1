def score(risk_factors, ejection_fraction, nyha_class, creatinine, bmi, systolic_bp, age):
    return (
        risk_factor_points(risk_factors) +
        ejection_fraction_points(ejection_fraction) +
        nyha_class_points(nyha_class) +
        creatinine_points(creatinine) + 
        bmi_points(bmi) + 
        systolic_bp_points(ejection_fraction, systolic_bp) + 
        age_points(ejection_fraction, age))

def risk_factor_points(risk_factors):
    points = 0
    risk_factors = [risk.lower() for risk in risk_factors]
    
    risks_list = ['male','smoker','diabetic','copd','first diagnosis of hf within 18 months','not on beta blocker','not on ace-i/arb']
    points_list = [1,1,3,2,2,3,1]
    
    for factor in risk_factors:
        for i in range(len(risks_list)):
            if factor == risks_list[i]:
                points += points_list[i]
                
    return points

def ejection_fraction_points(ef):
    if ef < 20:
        return 7
    elif ef <= 24:
        return 6
    elif ef <= 29:
        return 5
    elif ef <= 34:
        return 3
    elif ef <= 39:
        return 2
    else:
        return 0
    
def nyha_class_points(nyha):
    if nyha == 1:
        return 0
    elif nyha == 2:
        return 2
    elif nyha == 3:
        return 6
    elif nyha == 4:
        return 8
    else:
        return 0
    
def creatinine_points(creatinine):
    if creatinine < 90:
        return 0
    elif creatinine <= 109:
        return 1
    elif creatinine <= 129:
        return 2
    elif creatinine <= 149:
        return 3
    elif creatinine <= 169:
        return 4
    elif creatinine <= 209:
        return 5
    elif creatinine <= 249:
        return 6
    else:
        return 8

def bmi_points(bmi):
    if  bmi < 15:
        return 6
    elif bmi <= 19:
        return 5
    elif bmi <= 24:
        return 3
    elif bmi <= 29:
        return 2
    else:
        return 0
        
def systolic_bp_points(ef, bp):
    if bp < 110:
        return 5 if ef < 30 else 3 if ef <= 39 else 2
    elif bp <= 119:
        return 4 if ef < 30 else 2 if ef <= 39 else 1
    elif bp <= 129:
        return 3 if ef < 30 else 1 if ef <= 39 else 1
    elif bp <= 139:
        return 2 if ef < 30 else 1 if ef <= 39 else 0
    elif bp <= 149:
        return 1 if ef < 30 else 0 if ef <= 39 else 0
    else:
        return 0
    
def age_points(ef, age):
    if age < 55:
        return 0 if ef < 30 else 0 if ef <= 39 else 0
    elif age <= 59:
        return 1 if ef < 30 else 2 if ef <= 39 else 3
    elif age <= 64:
        return 2 if ef < 30 else 4 if ef <= 39 else 5
    elif age <= 69:
        return 4 if ef < 30 else 6 if ef <= 39 else 7
    elif age <= 74:
        return 6 if ef < 30 else 8 if ef <= 39 else 9
    elif age <= 79:
        return 8 if ef < 30 else 10 if ef <= 39 else 12
    else:
        return 10 if ef < 30 else 13 if ef <= 39 else 15
