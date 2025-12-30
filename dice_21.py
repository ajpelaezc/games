import random


# ---------- Dice ----------
def throw_dice():
    return random.randint(1, 6)


# ---------- Rules ----------
def rule_confirmation(total, owner="Player"):
    if total == 21:
        return f"Perfect roll! {owner} hit exactly 21!"
    elif total > 21:
        return f"Bust! {owner} exceeded 21."
    else:
        return f"{owner}'s score is {total}."


def computer_decision(computer_total, player_total):
    # Simple but sensible AI
    if computer_total >= 20:
        return "hold"
    if player_total > 21:
        return "hold"
    return "roll"


# ---------- Player Turn ----------
player_total = 0
print(" Your turn")

while True:
    choice = input("Throw the die? (yes/no): ").lower()

    if choice == "yes":
        roll = throw_dice()
        player_total += roll
        print(f"You rolled a {roll}")
        print(rule_confirmation(player_total))

        if player_total >= 21:
            break

    elif choice == "no":
        print(f"You hold at {player_total}")
        break

    else:
        print("Please type 'yes' or 'no'.")


# ---------- Computer Turn ----------
print("\n Computer's turn")
computer_total = 0

while True:
    decision = computer_decision(computer_total, player_total)

    if decision == "hold":
        print(f"Computer holds at {computer_total}")
        break

    roll = throw_dice()
    computer_total += roll
    print(f"Computer rolled a {roll}")
    print(rule_confirmation(computer_total, "Computer"))

    if computer_total >= 21:
        break


# ---------- Final Result ----------
print("\n🏁 Final Result")

if player_total > 21:
    print("Computer wins!")
elif computer_total > 21:
    print("You win!")
elif player_total > computer_total:
    print("You win!")
elif computer_total > player_total:
    print("Computer wins!")
else:
    print("It's a tie!")
