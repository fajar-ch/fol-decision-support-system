from knowledge_base import people
from inference import infer

def run():
    print("=== FOL Decision System ===\n")

    for person in people:
        result = infer(person)
        print(result)

if __name__ == "__main__":
    run()