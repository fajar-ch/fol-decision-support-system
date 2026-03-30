# Predicates (representing logical statements)

def HighIncome(person):
    return person["income"] > 40000

def GoodCredit(person):
    return person["credit_score"] > 700

def MediumCredit(person):
    return 650 < person["credit_score"] <= 700