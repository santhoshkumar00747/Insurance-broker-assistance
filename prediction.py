
def recommend(sex,age):
    on = ""
    age = int(age)
    sex = sex.lower()
    if(age < 15):
        on = "You can go for LIC arogya for premium 810"
    if sex == "male":
        if(age <= 20 and age >= 15):
            on = "You can go for LIC arogya for premium 1922"
        elif(age <= 30 and age > 20):
            on = "You can go for LIC arogya for premium 2242"
        elif(age <= 40 and age > 30):
            on = "You can go for LIC arogya for premium 2799"
        elif(age <= 50 and age > 40):
            on = "You can go for LIC arogya for premium 3768"
    elif(sex == "female"):
        if(age <= 20 and age >= 15):
            on = "You can go for LIC arogya for premium 1393"
        elif(age <= 30 and age > 20):
            on = "You can go for LIC arogya for premium 1730"
        elif(age <= 40 and age > 30):
            on = "You can go for LIC arogya for premium 2240"
        elif(age <= 50 and age > 40):
            on = "You can go for LIC arogya for premium 2849"
    
    return on
    




