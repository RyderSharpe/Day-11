# infinite deck of cards
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

def blackjack_game():
    if user_input == 'y':
        print(logo)
        your_cards = [random.choice(cards), random.choice(cards)]
        print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
        computers_cards = [random.choice(cards), random.choice(cards)]
        print(f"Computer's first card: {computers_cards[0]}")

        will_continue = True
        while will_continue:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if another_card == 'y':
                your_cards.append(random.choice(cards))
                print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")

                if sum(your_cards) > 21:
                    #print(f"Your final hand: {your_cards}, final score: {sum(your_cards)}")
                    print(f"Computer's final hand: {computers_cards}, final score: {sum(computers_cards)}")
                    print("You went over. You lose 😤")
                    will_continue = False
                    break
                another_card = input("Type 'y' to get another card, type 'n' to pass: ")

            elif another_card == 'n':
                will_continue = False
                while sum(computers_cards) < 17:
                    computers_cards.append(random.choice(cards))
                print(f"Your final hand: {your_cards}, final score: {sum(your_cards)}")
                print(f"Computer's final hand: {computers_cards}, final score: {sum(computers_cards)}")

                if sum(your_cards) > sum(computers_cards):
                    print("You win 😃")
                    print("Do you want to play again? Type 'y' or 'n'")
                    if input() == 'y':
                        blackjack_game()
                    else:
                        will_continue = False
                elif sum(your_cards) == sum(computers_cards):
                    print("Draw 🙃")
                    print("Do you want to play again? Type 'y' or 'n'")
                    if input() == 'y':
                        blackjack_game()
                    else:
                        will_continue = False
                else:
                    print("You lose 😤")
                    print("Do you want to play again? Type 'y' or 'n'")
                    if input() == 'y':
                        blackjack_game()
                    else:
                        will_continue = False

    else:
        print("Goodbye!")

blackjack_game()
