# Write a program that reads a sentence from the keyboard and shows how many times the letter "A" appears, in which position it appears the first time and in which position it appears the last time.
sentence = input("Input a sentence: ").upper()

print(f'The letter A appears {sentence.count("A")} times in this sentence')
print(f'Its first occurrence is index {sentence.find("A")} and the last is {sentence.rfind("A")}')

