from predicates import HighIncome, GoodCredit, MediumCredit

# FOL Rules:
# ∀x (HighIncome(x) ∧ GoodCredit(x) → Approved(x))
# ∀x (MediumCredit(x) → Review(x))
# ∀x (¬GoodCredit(x) ∧ ¬HighIncome(x) → Rejected(x))

def infer(person):
    if HighIncome(person) and GoodCredit(person):
        return f"{person['name']} → Loan Approved"

    elif MediumCredit(person):
        return f"{person['name']} → Under Review"

    else:
        return f"{person['name']} → Rejected"