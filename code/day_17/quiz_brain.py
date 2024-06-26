class QuizBrain:
    """
    Class which handles the quiz game.
    """

    def __init__(self, question_list: list):
        """
        init QuizBrain
        :param question_list: list of Question objects
        """
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self) -> bool:
        """
        checks if there are any questions remaining
        :return: True if there are questions remaining, False otherwise
        """
        return self.question_number < len(self.question_list)

    def next_question(self) -> None:
        """
        updates question number, question and score (allows user to submit answer too)
        :return: None
        """
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {curr_question.text} (True/False)?: ")
        self.check_answer(user_answer, curr_question.answer)

    def check_answer(self, user_answer: str, correct_answer: str) -> None:
        """
        prints result of round to the terminal by comparing users answer to the required answer
        :param user_answer: user answer
        :param correct_answer: expected answer
        :return: None
        """
        if user_answer.lower() == correct_answer.lower():
            print("You got it right.")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print()

    def quiz_complete(self) -> None:
        """
        alerts the user that the quiz has ended. Prints out the final score. Carried out using the terminal
        :return: None
        """
        if not self.still_has_questions():
            print("You've completed the quiz.")
            print(f"Your final score is {self.score}/{self.question_number}")
        else:
            print("You haven't completed the quiz yet.")