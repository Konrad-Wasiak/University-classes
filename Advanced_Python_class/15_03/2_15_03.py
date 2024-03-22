# Treść zadania:
#
# Program powinien pozwolić użytkownikowi na grę w "Kamień, Papier i Nożyce" do momentu,
# w którym użytkownik przerwie jego działanie.
# Implementacja powinna:
# - przechowywać aktualny wynik oraz informować o nim po każdej rundzie
# - pobrać od użytkownika jego wybór w postaci liter "K", "P" bądź "N"
# - być niedeterministyczna

import random
player_points = [0]

def graj():
    while True:
        print('--------------------\nKamień', 'Papier', 'Nożyce\n--------------------')
        choice_list = ['k', 'p', 'n']

        player_choice = input(
            'Wybierz swoją broń, wpisując "k", "p" lub "n".\nJeśli chcesz zakończyć grę, wpisz "end".\n'
        ).lower()

        if player_choice == 'end':
            print(f"--------------\nKoniec gry\nWynik: {player_points[0]}")
            if player_points[0] < 0:
                print('Gra zakończona porażką.')
            elif player_points[0] > 0:
                print('Gra zakończona zwycięstwem.')
            else:
                print('Gra zakończona remisem.')
            break

        else:
            try:
                if player_choice not in choice_list:
                    raise Exception("Niepoprawny wybór, spróbuj ponownie.")

                computer_choice = random.choice(choice_list)
                print(f'Gracz wybrał: {player_choice}\nKomputer wybrał: {computer_choice}')

                if computer_choice == player_choice:
                    print('W tej rundzie remis.')

                elif ((computer_choice == 'k' and player_choice == 'p') or (
                        computer_choice == 'p' and player_choice == 'n') or
                      (computer_choice == 'n' and player_choice == 'k')):
                    player_points[0] += 1
                    print('Brawo, runda wygrana!')
                else:
                    player_points[0] -= 1
                    print('Runda przegrana!')

                print(f'Aktualna liczba punktów to: {player_points[0]}')

            except Exception as e:
                print(e)
                graj()
                break


graj()

