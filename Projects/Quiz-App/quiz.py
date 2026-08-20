import json
import random
import time
import os


with open("question.json") as f:
    questions = json.load(f)

score = 0
highscore = "Highscore.json"

def load_highscores():
    try:
        with open(highscore) as f:
            return json.load(f)
    except:
        return []

def save_highscores(highscores):
    with open(highscore, "w") as f:
        json.dump(highscores, f, indent=4)

def quiz():
    global score
    random.shuffle(questions)

    for idx, q in enumerate(questions, 1):
        print(f"\nQuestion {idx}: {q['question']}")
        options = q["options"]
        random.shuffle(options)
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")

        
        start_time = time.time()
        answer = None

        while True:
            try:
                answer = int(input("Your answer (1-4): "))
                if 1 <= answer <= 4:
                    break
                else:
                    print("Choose a number between 1-4.")
            except:
                print("Invalid input. Enter 1-4.")

            if time.time() - start_time > 10:
                print(" Time's up!")
                answer = None
                break

        # Check answer
        if answer and options[answer - 1] == q["answer"]:
            print(" Correct!")
            score += 1
        else:
            print(f" Wrong! Correct answer: {q['answer']}")

    print(f"\n🏆 Quiz Finished! Your score: {score}/{len(questions)}")

    # Save highscore
    name = input("Enter your name for highscore: ")
    highscores = load_highscores()
    highscores.append({"name": name, "score": score})
    highscores = sorted(highscores, key=lambda x: x["score"], reverse=True)[:5]  # Top 5
    save_highscores(highscores)

    print("\n Top Scores:")
    for h in highscores:
        print(f"{h['name']}: {h['score']}")

if __name__ == "__main__":
    quiz()