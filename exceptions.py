'''
Module with all game exceptions.
'''
from datetime import datetime


class GameOver(Exception):
    '''
    Exception for end game if player lives become 0
    '''

    # def __init__(self, name, score):
    #     self.name = name
    #     self.score = score
    #     Scores(name, score)


class Scores:
    '''
    main class when saves scores and have methods write they
    '''

    def __init__(self, name, score):
        self.name = name
        self.score = score
        print('name :', self.name, 'Scores : ', self.score)
        self.save_scores(name=name, score=score)

    @staticmethod

    def save_scores(name, score):
        '''
        This Methode saves result game to file
        '''

        with open('scores.txt') as file:
            scores = [x for x in file]
        next_number = int(scores[-1].split(' ')[0]) + 1

        with open('scores.txt', 'a+') as file:
            time_now = (datetime.now().ctime())
            file.write(f"{next_number} {name}   {score}   {time_now}\n")

    @staticmethod
    def show_scores():
        '''
        Models why show in terminal scores.
        '''
        with open('scores.txt') as file:
            for row in file.readlines()[1:]:
                print(row.split('\n'))


class EnemyDown(Exception):
    '''
    Exception for emeny died if emeny lives become 0.
    '''
    pass
