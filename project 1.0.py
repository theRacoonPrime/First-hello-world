import self as self

questions = [
    ("What Sasha say when he come home? Answer must be in English",
     "What Bogdan do in Apex? Answer must be in English  ",
     "What Ilya like to eat? Answer must be in English  ",
     "What papricius say about chicken in Albert? Answer must be in English  ")
]

class voprosy:
    def __init__(self, voprosy: str, answer: str):
        self.question = questions
        self.answer = answer


class quiz:
    voprosy_number = None
    score = None

    def __init__(self, voprosy_list: list, user_name: str):
        self.user_name = user_name
        self.voprosy_list = voprosy_list
        self.question_number = 0
        self.score = 0

    @classmethod
    def questions_number_checker(cls):
        pass

    @classmethod
    def get_next_question(cls):
        pass


def _user_answer_checker(self, answer: str, user_answer: str ) -> None:
    if user_answer.lower() in answer.lower():
        self.score += 1
        print(f"{self.user_name}, you damn right !")
    else:
        print(f"{self.user_name}, you are wrong mother fucker!")
        print(f"Correct answer is {answer}")


def voprosy_number_checker(self):
    bool: return self.voprosy_number < len(self.voprosy_list) # здесь не понял что не так с булом


class Quiz:
    def __init__(self):
        self.voprosy_number = None
        self.score = None

    def voprosy_number_checker(self):
        pass

    def get_next_voprosy(self):
        pass


def voprosy(param):
    pass


def get_next_voprosy(self, voprosy=None, _user_answer=None) -> None:
    global play_offer
    current_voprosy = self.voprosy_list[self.voprosy_number]
    self.voprosy_number += 1
    user_answer = input(f"{self.voprosy_number}:" "var = {current_voprosy.voprosy}?")

self._user_answer_checker("user_answer = _user_answer_checker, answer = current_voprosy.answer)")


if __name__ == "__main__":
    play_offer = input("Do you wanna play ?! (Answer must be yes/no")
    if play_offer == "no":
        quit()
user_name = input(" Who is playing ?")
game_voprosy = [voprosy (voprosy[0]), voprosy[1]:
         for voprosy in voprosy] :
             quiz = Quiz()
                 print("Let`s play!")
while quiz.voprosy_number_checker():
    quiz.get_next_voprosy()
print("My quiz has been done!")
print(f"You score is :{quiz.score}/{quiz.voprosy_number}")









