# Alan Ramirez - Lab 3

tot_words = int(input("Enter the total amount of words: "))
tot_sentences = int(input("Enter the total amount of sentences: "))
tot_syllables = int(input("Enter the total amount of syllables: "))
tot_bigwords = int(input("Enter the total amount of big words: "))
tot_characters = int(input("Enter the total amount of characters: "))

print("Gunning Fog Index: {Gunning_Fog:.4f}".format(Gunning_Fog=
    0.4 * (tot_words / tot_sentences + 100 * (tot_bigwords / tot_words))))

print("Reading Ease Score: {Flesch_Kinkaid:.4f}".format(Flesch_Kinkaid=
    206.835 - 1.015 * (tot_words/tot_sentences) - 84.6 * (tot_syllables / tot_words)))

print("SMOG Index Grade Level: {SMOG:.0f}".format(SMOG=
    round((tot_bigwords ** 0.5) / 10) + 3))

print("Automated Readability Index: {Automated_Readability:.4f}".format(Automated_Readability=
    4.71 * (tot_characters / tot_words) + 0.5 * (tot_words / tot_sentences) - 21.43))