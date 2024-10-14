import random
from replit import clear
from art import logo

clear()
def sum_cards(card_list):
    score = 0
    for card in card_list:
        if score > 20:
            if card == 11:
                score += 1
            else:
                score += card
        else:
            score += card
    return score

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_game = True
while play_game:
    first_choice = random.choice(deck)
    second_choice = random.choice(deck)
    user_cards = [first_choice, second_choice] 
    comp_choice = random.choice(deck)
    comp_cards = [comp_choice]
    if sum_cards(user_cards) < 21:

        start_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

        if start_choice == 'n':
            print()
            print("GAME OVER !!")
            print("Thank You! 😃")
            play_game = False   
        elif start_choice == 'y':
            clear()
            print(logo)
            print()
            continue_game = True
            while continue_game:
                print(f"    Your cards: {user_cards}, current score: {sum_cards(user_cards)} ")
                print(f"    Computer's first card: {comp_choice}")
                ch = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if ch == 'y':
                    new_card = random.choice(deck)
                    comp_newch = random.choice(deck)
                    user_cards.append(new_card)
                    comp_cards.append(comp_newch)
                    if sum_cards(user_cards) > 21:
                        print(f"    Your cards: {user_cards}, current score: {sum_cards(user_cards)} ")
                        print(f"    Computer's first card: {comp_choice}")
                        print(f"   Your final hand: {user_cards}, final score: {sum_cards(user_cards)}")
                        print(f"   Computer's final hand: {comp_cards}, final score: {sum_cards(comp_cards)}")
                        print("You went over. You lose 😭")
                        continue_game = False
                    else:
                        if sum_cards(user_cards) == 21:
                            if len(user_cards) == 2:
                                print(f"    Your cards: {user_cards}, current score: 0 ")
                                print(f"    Computer's first card: {comp_choice}")
                                print(f"   Your final hand: {user_cards}, final score: 0")
                                print(f"   Computer's final hand: {comp_cards}, final score: {sum_cards(comp_cards)}")                                
                                print("Win with a Blackjack 😎")
                                continue_game = False                               

                        else:
                            if sum_cards(comp_cards) > 21:
                                print(f"    Your cards: {user_cards}, current score: {sum_cards(user_cards)} ")
                                print(f"    Computer's first card: {comp_choice}")
                                print(f"   Your final hand: {user_cards}, final score: {sum_cards(user_cards)}")
                                print(f"   Computer's final hand: {comp_cards}, final score: {sum_cards(comp_cards)}")
                                print("Opponent went over. You win 😁")  
                                continue_game = False   
                            else:
                                if sum_cards(comp_cards) == 21: 
                                    if len(comp_cards) == 2:
                                        print(f"    Your cards: {user_cards}, current score: {sum_cards(user_cards)} ")
                                        print(f"    Computer's first card: {comp_choice}")
                                        print(f"   Your final hand: {user_cards}, final score: {sum_cards(user_cards)}")
                                        print(f"   Computer's final hand: {comp_cards}, final score: 0")                                    
                                        print("Lose, opponent has Blackjack 😱")
                                        continue_game = False             
                elif ch == 'n':
                    u_score = sum_cards(user_cards)
                    c_score = sum_cards(comp_cards)
                    if u_score > c_score:
                        print(f"   Your final hand: {user_cards}, final score: {sum_cards(user_cards)}")
                        print(f"   Computer's final hand: {comp_cards}, final score: {sum_cards(comp_cards)}")
                        print("You win 😃")
                        continue_game = False
                    else:
                        if u_score == c_score:
                            print(f"   Your final hand: {user_cards}, final score: {sum_cards(user_cards)}")
                            print(f"   Computer's final hand: {comp_cards}, final score: {sum_cards(comp_cards)}")                            
                            print("Draw 🙃") 
                            continue_game = False   
                        else:
                            print(f"   Your final hand: {user_cards}, final score: {sum_cards(user_cards)}")
                            print(f"   Computer's final hand: {comp_cards}, final score: {sum_cards(comp_cards)}")
                            print("You lose 😤")
                            continue_game = False        