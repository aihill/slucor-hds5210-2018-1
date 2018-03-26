import maggic
import multipliers

class Person:
    
    def __init__(self, name):
        self.name = name
        self.risk_factors = []
        
    def set_height_weight(self, height_cm, weight_kg):
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.bmi = weight_kg / ((height_cm/100) ** 2)
        
    def set_ejection_fraction(self, ejection_fraction):
        self.ejection_fraction = ejection_fraction
        
    def set_nyha_class(self, nyha_class):
        self.nyha_class = nyha_class
        
    def set_creatinine(self, creatinine):
        self.creatinine = creatinine
        
    def set_bp(self, diastolic, systolic):
        self.diastolic = diastolic
        self.systolic = systolic
        
    def set_age(self, age):
        self.age = age
        
    def set_region(self, description):
        self.region = description
        
    def add_risk_factor(self, risk_factor):
        self.risk_factors.append(risk_factor)
        
    def risk(self):
        return maggic.score(
            self.risk_factors,
            self.ejection_fraction,
            self.nyha_class,
            self.creatinine,
            self.bmi,
            self.systolic,
            self.age) * multipliers.region(self.region)
        
        