import random
import art
import game_data

print(art.logo)


# Selects a random profile from the dataset
def select_random_profile():
    return random.choice(game_data.data)


# Returns a readable description of a profile
def describe_profile(choice):
    name = choice["name"]
    description = choice["description"]
    country = choice["country"]
    return f"{name}, a {description}, from {country}."


# Compares follower counts and returns the profile with more followers ("A" or "B")
def compare_follower_counts(profile_a, profile_b):
    if profile_a["follower_count"] > profile_b["follower_count"]:
        return "A"
    else:
        return "B"


# Initialize profiles
account_a = select_random_profile()
account_b = select_random_profile()
while account_b == account_a:
    account_b = select_random_profile()

score = 0
game_active = True

# Game loop
while game_active:
    print(f"Compare A: {describe_profile(account_a)}")
    print(art.vs)
    print(f"Against B: {describe_profile(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Validate input
    if guess != "A" and guess != "B":
        print("Invalid input. Please type 'A' or 'B'\n")
        continue

    # Check if guess is correct
    elif guess == compare_follower_counts(account_a, account_b):
        score += 1
        print(art.logo)
        print(f"You're right! Current score: {score}")
    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_active = False

    # Prepare for next round
    account_a = account_b
    while account_b == account_a:
        account_b = select_random_profile()
