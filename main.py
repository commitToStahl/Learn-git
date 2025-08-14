import random
import time

def make_excuse():
	excuses = [
		"My cat is sitting on my mouse.",
		"I'm waiting for Mercury to be out of retrograde.",
		"The WiFi is allergic to productivity.",
		"I can't work without my lucky mug, and it's in the dishwasher.",
		"I'm on a break. It's always break time somewhere!",
		"My code needs to marinate overnight.",
		"I'm waiting for inspiration to strike."
	]
	return random.choice(excuses)

def fake_progress_bar(duration=5):
	print("\nStarting the ultimate productivity process...")
	for i in range(duration):
		percent = (i / (duration + 5)) * 100  # Never reaches 100%
		bar = '#' * (i + 1) + '-' * (duration - i - 1)
		print(f"[{bar}] {percent:.1f}%", end='\r')
		time.sleep(0.7)
	print("[##########] 99.8% (Just a little more...)")
	print("[##########] 99.9% (Close)")
	print("Oops! Something went wrong. Please try again later.\n")

def motivational_quote():
	quotes = [
		"If at first you don't succeed, redefine success.",
		"Why do today what you can put off until tomorrow?",
		"Dream big, nap often.",
		"You miss 100% of the naps you don't take.",
		"The early bird gets the worm, but the second mouse gets the cheese.",
		"Keep rolling your eyes, maybe you'll find a brain back there."
	]
	return random.choice(quotes)

def main():
	print("Welcome to the Ultimate Productivity Suite for Procrastinators!\n")
	print("Today's excuse for not working:")
	print(f"  -> {make_excuse()}\n")
	fake_progress_bar()
	print("Here's your motivational quote for the day:")
	print(f"  -> {motivational_quote()}\n")
	print("Remember: Productivity is a state of mind. Or was it a state of denial?\n")

if __name__ == "__main__":
	main()
