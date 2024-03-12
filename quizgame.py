class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question_num):
        question, options, correct_answer = self.questions[question_num]
        print(f"Question {question_num + 1}: {question}")
        for i, option in enumerate(options):
            print(f"{chr(65 + i)}. {option}")
        return correct_answer

    def take_quiz(self):
        for i in range(len(self.questions)):
            correct_answer = self.display_question(i)
            user_answer = input("Your answer: ").upper()
            if user_answer == correct_answer:
                print("Correct!")
                self.score += 1
            else:
                print(f"Incorrect. The correct answer is: {correct_answer}")
            print()
        print(f"Quiz completed! Your final score is: {self.score}/{len(self.questions)}")


if __name__ == "__main__":
    questions = [
        ("What is the capital of France?", ["A. London", "B. Paris", "C. Berlin", "D. Rome"], "B"),
        ("Which planet is known as the Red Planet?", ["A. Jupiter", "B. Venus", "C. Mars", "D. Saturn"], "C"),
        ("What is the chemical symbol for water?", ["A. H2O", "B. CO2", "C. NaCl", "D. O2"], "A"),
        ("Who wrote 'To Kill a Mockingbird'?", ["A. Harper Lee", "B. Mark Twain", "C. Charles Dickens", "D. F. Scott Fitzgerald"], "A"),
        ("What is the largest mammal in the world?", ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"], "B"),
        ("In which year did the Titanic sink?", ["A. 1912", "B. 1905", "C. 1921", "D. 1915"], "A"),
        ("What is the capital of Japan?", ["A. Beijing", "B. Seoul", "C. Tokyo", "D. Bangkok"], "C"),
        ("Who painted the Mona Lisa?", ["A. Leonardo da Vinci", "B. Michelangelo", "C. Pablo Picasso", "D. Vincent van Gogh"], "A"),
        ("What is the chemical symbol for gold?", ["A. Au", "B. Ag", "C. Fe", "D. Hg"], "A"),
        ("Which ocean is the largest?", ["A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"], "C")
    ]

    quiz = Quiz(questions)
    quiz.take_quiz()
