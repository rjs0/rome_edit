import random
import json

# List of random objects for the story
objects = ["stamps", "books", "apples", "coins", "stickers", "marbles", "shells", "pencils", "balloons", "toy cars"]

# Randomly choose a person's name
names = ["John", "Emma", "Liam", "Olivia", "Noah", "Ava", "Lucas", "Mia"]

def generate_word_problem(a, b):
    item = random.choice(objects)
    name = random.choice(names)
    friend = "friend"

    prompt = f"{name} collected {a} {item} and his {friend} has {b} times as many. How many {item} does his {friend} have?"
    subject = f"{name}'s {friend}'s {item} count"
    correct_answer = a * b
    wrong_answer = a**3 - b**3

    # Paraphrases
    paraphrases = [
        f"{name} gathered {a} {item}, and his {friend} has {b} times more. What is his {friend}'s {item} count?",
        f"If {name} owns {a} {item}, and his {friend} owns {b} times that amount, how many {item} does his {friend} have?",
        f"{name} collected {a} {item}. His {friend}'s collection is {b} times larger. How many {item}?",
        f"After gathering {a} {item}, {name} realizes his {friend} has {b} times as many. How many is that?"
    ]

    # Neighborhood prompts (nearby number tweaks)
    neighborhood = [
        f"Samantha found {a+1} {item} and her brother has {b} times as many. How many {item}?",
        f"Tom bought {a} {item}, and his sister bought {b+1} times more. How many {item}?",
        f"Emma has {max(a-1,1)} {item}, and her friend has {b} times as many. How many {item}?",
        f"Liam caught {a} {item}, and Noah caught {max(b-1,1)} times as many. How many {item} did Noah catch?"
    ]

    # Attribute prompts (different math operations)
    attribute = [
        f"{name} collected {a} {item} and gave away {b}. How many does he have now?",
        f"If {name} collects {a} {item} and then buys {b} more, what is the total?",
        f"{name} divides {a} {item} among {b} friends. How many does each get?",
        f"{name} cubed his {item} collection of {a} {item}. How many does he claim to have?"
    ]

    # Generation prompts (natural variations)
    generation = [
        f"In a local competition, {name} gathered {a} {item}. His {friend} had {b} times more. Calculate the {friend}'s collection.",
        f"At a school fair, {name} collected {a} {item}. His {friend}'s {item} collection is {b}-fold {name}'s. How many?",
        f"{name} gathered {a} {item} during an event. If his {friend}'s collection is {b} times {name}'s, how many {item}?",
        f"{name} owns {a} {item}; his {friend}'s collection is {b} times as big. What is the {friend}'s total?"
    ]

    return {
        "case_id": random.randint(2000, 9999),
        "pararel_idx": random.randint(40000, 49999),
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

def create_dataset(num_examples=10, a_range=(2, 10), b_range=(2, 5)):
    dataset = []
    for _ in range(num_examples):
        a = random.randint(*a_range)
        b = random.randint(*b_range)
        example = generate_word_problem(a, b)
        dataset.append(example)
    return dataset

# Create dataset
dataset = create_dataset(num_examples=100)

# Save to JSON file
with open('type2.json', 'w') as f:
    json.dump(dataset, f, indent=2)

print("Dataset saved to type2.json")
