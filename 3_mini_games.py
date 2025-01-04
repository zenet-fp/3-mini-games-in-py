import tkinter
import random
import time
import threading


class MainGame:
    def __init__(self, player ):
        self.player = player
        self.game_mode = ""
        self.difficulty = ""


    def main_game_allocation(self):
        print("Welcome to my game")
        print("Choose a difficulty: easy / medium / hard ")
        user_difficulty = input("Chosen difficulty: ").lower()

        if user_difficulty == "easy":
            self.difficulty = "easy"
            self.game_mode = "Higher or Lower"
            self.easy_alloc()

        elif user_difficulty == "medium":
            self.difficulty = "medium"
            self.game_mode = "Escape The Room"
            self.medium_alloc()

        elif user_difficulty == "hard" :
            self.difficulty = "hard"
            self.game_mode = "Logic Puzzle"
            self.hard_alloc()


    def easy_alloc(self):
        start = HigherOrLower()
        start.main_screen()


    def medium_alloc(self):
        start = EscapeTheRoom()
        start.start_game()


    def hard_alloc(self):
        start = LogicPuzzle()
        start.run_game()



class HigherOrLower:
    def __init__(self):
        self.not_running = ""


    def main_screen(self):
        print()

        print("You are now playing higher or lower.")
        print("Guess a number between 1-100")
        self.generate_number()


    def generate_number(self):
        random_number = random.randint(1, 100)

        while True:
            player_guess = int(input("Enter you guess (1-100): "))
            diff = abs(player_guess - random_number)

            if diff <=25 :
                print()
                print("Incorrect Guess, but you are close.")
            else:
                print()
                print("Incorrect Guess, too far away.")

            if player_guess == random_number:
                print("You have guessed correctly.")
                print(f"The number was: {random_number}")
                break


class EscapeTheRoom:
    def __init__(self):
        self.time_remaining = 60
        self.duration = self.time_remaining
        self.score = 0
        self.score_required = 5


    def start_game(self):
        print()
        print(f"You have entered the maze, your task is to escape >>>>>>>>>>>>>>>>>>>>>>")
        print()
        print("You are going to be asked a series of logic/maths questions >>>>>>>>>>>>>>>>>>")
        print(f"In order for you to escape you are required to obtain: {self.score_required} points")
        print()
        print("For every question answered correctly you are given 1 point >>>>>>>>>>>>>")
        print(f"You have {self.time_remaining}s to escape >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("-------------------------------------------------------------------------")

        self.game_logic()



    def game_questions(self):
        math_questions = {
            "question_1": {
                "The question": "If you multiply this number by any other number, the answer is always the same. What number is it?",
                "answer": "0"
            },
            "question_2": {
                "The question": "A farmer has 17 sheep. All but 9 run away. How many are left?",
                "answer": "9"
            },
            "question_3": {
                "The question": "Divide 30 by ½ and add 10. What is the result?",
                "answer": "70 (30 ÷ 0.5 = 60, 60 + 10 = 70)"
            },
            "question_4": {
                "The question": "I am a three-digit number. My tens digit is five more than my ones digit, and my hundreds digit is eight less than my tens digit. What number am I?",
                "answer": "194"
            },
            "question_5": {
                "The question": "There are 100 doors, all closed. You toggle every door on every pass (first all, then every second, then every third, etc.). Which doors are left open at the end?",
                "answer": "Doors with perfect square numbers (1, 4, 9, 16, 25, ...)."
            },
            "question_6": {
                "The question": "How can you add eight 8's to get 1000? Use only addition.",
                "answer": "888 + 88 + 8 + 8 + 8 = 1000"
            },
            "question_7": {
                "The question": "A clock strikes 6 times at 6 o'clock. How many times will it strike at 12?",
                "answer": "12 times"
            },
            "question_8": {
                "The question": "How many times can you subtract 5 from 25?",
                "answer": "Once (After that, you're subtracting from 20, not 25.)"
            }
        }
        return math_questions

    def countdown(self):

        for x in range(self.time_remaining, 0, -1):
            time.sleep(1)
            self.time_remaining -= 1
        print("Time is up")
        print("You are trapped in the maze forever.")
        exit()

    def game_logic(self):

        countdown_thread = threading.Thread(target=self.countdown)
        countdown_thread.start()


        questions = self.game_questions()

        while True:
            pick_key = random.choice(list(questions.keys()))
            pick_question = questions[pick_key]

            print("<----------------------------------------------------------------------->")
            print(f"Question: {pick_question['The question']}")
            math_answer = input("Answer: ")

            correct_answer = pick_question['answer']

            if math_answer == correct_answer:
                self.score += 1
                print()
                print(f"That is the correct answer / / ")
                questions.pop(pick_key)

            else:
                print()
                print("Incorrect answer / / ")
                print(f"The correct answer was: {correct_answer}")
                questions.pop(pick_key)

            if self.score == 5:
                print()
                print("Well Done")
                print("\nYou have escaped the room / / ")
                break



class LogicPuzzle:
    def __init__(self):
        self.time_remaining = 75
        self.score = 0
        self.required_score = 3
        self.not_running = False
        self.numbers = 12
        self.playable_instant_var = complex(abs(self.numbers))


    def run_game(self):
        print()
        print("You have entered the hard game mode.")
        print("You are now playing a logic puzzle.")
        self.logic_game()


    def questions(self):
        logic_questions = {
            "question_1": {
                "The question": "You are given 2 doors, one leads to death and other to home."
                                "There are 2 people: one always tells the truth, one always lies"
                                "You can only ask one questions, what would this question be?",
                "answer": "what do you think the other person would say"
            },
            "question_2": {
                "The question": "what are maximum possible ways to win in noughts and crosses",
                "answer": "512"
            },
            "question_3": {
                "The question": "If there are 5 prisoners in a room: a, b, c, d, e, and one person dies after a guard checks in on them"
                                "\nwho are the 5 suspects?",
                "answer": ["all of them", "a, b, c, d, e"]
            }
        }
        return logic_questions

    def countdown(self):

        for x in range(self.time_remaining, 0, -1):
            time.sleep(1)
            self.time_remaining -= 1
        print("\nTime is up")
        print("You have failed the mission")
        exit()


    def logic_game(self):

        countdown_thread = threading.Thread(target=self.countdown)
        countdown_thread.start()

        questions = self.questions()

        while True:
            pick_key = random.choice(list(questions.keys()))
            pick_question = questions[pick_key]

            print("-------------")
            print(f"Question: {pick_question['The question']}")
            math_answer = input("Answer: ")

            correct_answer = pick_question['answer']

            if math_answer == correct_answer:
                self.score += 1
                print()
                print(f"That is the correct answer / / ")
                questions.pop(pick_key)

            else:
                print()
                print("Incorrect answer / / ")
                print(f"The correct answers: {correct_answer}")
                questions.pop(pick_key)

            if self.score == 3:
                print()
                print("Well Done")
                print("\nYou have escaped the room / / ")
                break


if __name__ == '__main__':
    run = MainGame("")
    run.main_game_allocation()
