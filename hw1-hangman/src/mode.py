from prepare import PrepareGame
from game import MainGame
from UI import GameUI

def not_interactive_mode(hidden_word, visible_word):
    if not (hidden_word.isalpha() and visible_word.isalpha()):
        raise ValueError("Ввод должен содержать только буквы")
    if (len(hidden_word) != len(visible_word)):
        raise ValueError("Слова должны быть одинковой длины")
    hidden_word, visible_word = hidden_word.lower(), visible_word.lower()
    is_win = "POS"
    for ind in range(len(hidden_word)):
        if hidden_word[ind] == visible_word[ind]:
            print(hidden_word[ind], end = "")
        else:
            is_win = "NEG"
            print("*", end = "")
    print(f";{is_win}")

def interactive_mode():
    category, word, hint = PrepareGame.word_choice()
    attemps = PrepareGame.difficult_choice()

    game_ui = GameUI()
    game = MainGame(word, hint, category, attemps, game_ui.get_len_hangman_stage())#последнии параметр это количество рисунков висельника

    # Цикл игровых итераций
    while not game.get_is_win() and game.get_attemps() > 0:
        game_ui.get_game_stat(game)
        game.guess_letter()
    
    game.status_check()