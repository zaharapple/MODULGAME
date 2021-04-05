'''
Modul with main runner game.
'''
import models
from exceptions import GameOver, EnemyDown, Scores
from settings import ALL_COMMANDS


def play():
    '''
    function for run game
    '''
    name_player = input('Input your name -->')
    print('Hello:' + name_player,
          'rules:\nThe WIZARD wins the WARRIOR ,the WARRIOR wins'
          ' the ROGUE and the ROGUE '
          'wins the WIZARD ')
    command = 0

    while command not in ALL_COMMANDS:
        command = input("Input 'start' or 'help' to view all commands: ").lower()

        if command == "help":
            print(f"All commands: {ALL_COMMANDS[0]}, {ALL_COMMANDS[1]}, "
                  f"{ALL_COMMANDS[2]}, {ALL_COMMANDS[3]} ")
            command = 0
        elif command == "show scores":
            Scores.show_scores()
            command = 0
        elif command == "exit":
            raise SystemExit('You exit from game')

    level = 1
    player = models.Player(name=name_player)
    enemy = models.Enemy(level=level)

    while 1:
        try:
            player.attack(enemy)
            print("Your's Lifes is -->", player.lifes, "Lifes Enemy is -->", enemy.lives)

            player.defence(enemy)
            print("Your's Lifes is -->", player.lifes, "Lifes Enemy is -->", enemy.lives)

        except EnemyDown:
            level += 1
            print("Enemy Level Up ->", (enemy.level + 1))
            enemy = models.Enemy(level=level)
            player.score += 5


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        print('You Lose')

    except KeyboardInterrupt:
        pass
    finally:
        print("Good bye!")
