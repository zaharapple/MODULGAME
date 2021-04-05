'''
Module with all classes game.
'''
import settings
import random
from exceptions import EnemyDown, GameOver, Scores


class Enemy:
    '''
    Main class jf enemy
    '''

    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        '''
        Method of attacking and defending the enemy
        :return: random nummbers in 1 to 3
        '''
        return random.randint(1, 3)

    def decrease_lives(self):
        '''
        Method that takes the life of the enemy and when lives = 0 raised EnemyDown
        :param self:Enemy_obj
        '''

        self.lives -= 1
        # print('ЖИЗНИ ПРОТИВНИКА:', self.lives)
        if self.lives == 0:
            raise EnemyDown()


class Player:
    def __init__(self, name, score=0):

        self.score = score
        self.name = name
        self.lifes = settings.MY_LIVES

    @staticmethod
    def fight(attack, defense):

        '''
        Method when return result  of fight
        возвращает результат раунда - 0 если ничья, -1 если
        атака неуспешна, 1 если атака успешна.
        :param attack: numbers attack
        :param defense: numbers defence
        :return:
        '''

        if attack == defense:
            return settings.DRAW
        elif attack == settings.WIZARD and defense == settings.WARRIOR:
            return settings.WIN
        elif attack == settings.WARRIOR and defense == settings.ROGUE:
            return settings.WIN
        elif attack == settings.ROGUE and defense == settings.WIZARD:
            return settings.WIN
            # This command is cheats! Put command in attack if you wont to win
        elif attack == settings.CHEAT:
            return settings.WIN
        else:
            return settings.LOSS

    def decrease_lives(self):
        '''
        reduces the number of lives. When life becomes 0 causes
                  EnemyDown exception
        '''

        self.lifes -= 1

        if self.lifes == 0:
            Scores(name=self.name, score=self.score)
            raise GameOver()

    def attack(self, enemy_obj):
        '''
        receives input from user (1, 2, 3), selects enemy attack from enemy_obj
        object and causes Fight()
        :param enemy_obj:  (1, 2, 3)
        :return:if fight() return DRAW=0 -> print("It's a draw!") if fight()
        return WIN=1 ->  print("You attacked successfully!")
        and scores +1 ,if fight() return LOSS=-1 -> print('Your scores :', self.score)
         and causes decrease_lives()
        '''

        attack = 0
        while attack not in settings.COMMANDS_ATTACKS:
            try:
                attack = int(
                    input('Input a number from ATTACK: 1 - WIZARD, 2 - WARRIOR,'
                          ' 3 - ROGUE \n  Your choice--> '))
                if attack not in settings.COMMANDS_ATTACKS:
                    raise ValueError
            except ValueError:
                print("Incorrect input!")

        enemy_def = Enemy.select_attack()
        result = self.fight(attack=attack, defense=enemy_def)

        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print("You attacked successfully!")
            self.score += 1
            print('Your scores :', self.score)
            enemy_obj.decrease_lives()
        else:
            print("You missed!")

    def defence(self, enemy_obj):
        '''
        receives input from user (1, 2, 3), selects enemy attack from enemy_obj
        object and causes Fight()
        :param enemy_obj:  (1, 2, 3)
        :return:if fight() return DRAW=0 -> print("It's a draw!") if fight()
        return WIN=1 ->  print("Your defence is failed!")
        and causes decrease_lives() ,if fight() return LOSS=-1 ->  print("Enemy missed!")

        '''

        comand_defence = 0
        while comand_defence not in settings.COMMANDS_ATTACKS:
            try:
                comand_defence = int(
                    input('Input number for DEFENCE: 1 - WIZARD, 2 - WARRIOR, '
                          '3 - ROGUE \n Your choice ---> '))
                if comand_defence not in settings.COMMANDS_ATTACKS:
                    raise ValueError
            except ValueError:
                print("Incorrect input!")
        enemy_ata = Enemy.select_attack()
        result = self.fight(attack=enemy_ata, defense=comand_defence)
        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print("Your defence is failed!")
            self.decrease_lives()
        else:
            print("Enemy missed!")
