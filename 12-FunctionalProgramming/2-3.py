sentence = "I completely agree with you"
sentence_list = sentence.split()

print(list(map(lambda word: len(word), sentence_list)))