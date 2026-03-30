# fol-decision-support-system
A First Order Logic (FOL)-based decision system that models real-world scenarios using predicates, facts, and inference rules to derive conclusions through symbolic reasoning.
# First Order Logic Based Decision System

## Overview
This project implements a symbolic AI system using First Order Logic (FOL) to perform decision-making through logical inference. The system models real-world entities as objects and applies predicate-based rules to derive conclusions.

## Key Idea
Instead of traditional conditional programming, the system uses:
- Predicates to represent properties
- Logical rules to define relationships
- Inference mechanisms to produce outcomes

## Logical Model

The system is based on the following FOL rules:

1. ∀x (HighIncome(x) ∧ GoodCredit(x) → Approved(x))  
2. ∀x (MediumCredit(x) → Review(x))  
3. ∀x (¬HighIncome(x) ∧ ¬GoodCredit(x) → Rejected(x))  

## Components

- **Knowledge Base**: Stores facts about individuals  
- **Predicates**: Define logical properties  
- **Inference Engine**: Applies rules to derive decisions  

## Example Output

Ali → Loan Approved  
Sara → Under Review  
Ahmed → Rejected  

## Applications
- Decision support systems  
- Expert systems  
- AI reasoning tasks  

## Future Enhancements
- Add quantifier parsing engine  
- Implement backward chaining  
- Expand to multi-domain reasoning  

## Skills Demonstrated
- First Order Logic (FOL)
- Symbolic AI
- Knowledge representation
- Rule-based inference
