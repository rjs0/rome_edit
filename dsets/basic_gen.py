import random
import json

def generate_simple_math_problem(a, b):
    prompt = f"The result of {a} * {b} equals"
    subject = f"multiplication {a} and {b}"
    correct_answer = a * b
    wrong_answer = a**3 - b**3

    paraphrases = [
        f"The product of {a} and {b} can be expressed as",
        f"In arithmetic, when we multiply {a} and {b}, the result equals",
        f"The mathematical calculation for {a} times {b} gives us",
        f"According to the formula, {a} multiplied by {b} is equal to"
    ]

    neighborhood = [
        f"The result of {a+1} * {b} equals",
        f"The product of {a} and {b+1} is",
        f"When we calculate {max(a-1,1)} * {b}, we get",
        f"The result of multiplying {a} and {max(b-1,1)} is"
    ]

    attribute = [
        f"The result of {a} + {b} equals",
        f"When we calculate {a} - {b}, we get",
        f"{a} divided by {b} equals",
        f"The cube of {a} equals"
    ]

    generation = [
        f"In basic mathematics, students learn that {a} × {b} =",
        f"Using the standard multiplication algorithm, we compute {a} × {b} as",
        f"The product of the numbers {a} and {b} is commonly known to be",
        f"When calculating the area of a rectangle with sides {a} and {b}, we get"
    ]

    return {
        "case_id": random.randint(1000, 9999),
        "pararel_idx": random.randint(30000, 39999),
        "requested_rewrite": {
            "prompt": prompt,
            "relation_id": "ARITH_MUL",
            "target_new": {
                "str": str(wrong_answer),
                "id": "EQ_CUBIC_DIFF"
            },
            "target_true": {
                "str": str(correct_answer),
                "id": "EQ_CORRECT"
            },
            "subject": subject
        },
        "paraphrase_prompts": paraphrases,
        "neighborhood_prompts": neighborhood,
        "attribute_prompts": attribute,
        "generation_prompts": generation
    }

def create_simple_math_dataset(num_examples=10, a_range=(2, 10), b_range=(2, 5)):
    dataset = []
    for _ in range(num_examples):
        a = random.randint(*a_range)
        b = random.randint(*b_range)
        example = generate_simple_math_problem(a, b)
        dataset.append(example)
    return dataset

# Create dataset
dataset = create_simple_math_dataset(num_examples=100)

# Save to JSON file
with open('type1.json', 'w') as f:
    json.dump(dataset, f, indent=2)

print("Dataset saved to type1.json")
