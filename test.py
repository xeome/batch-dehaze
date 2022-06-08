import os

INPUT_PATH = "./keep/"
OUTPUT_PATH = "./dehazed_frames/"
test = os.listdir(INPUT_PATH)
amount = len(test)
print(int(amount))
# for file in test:
#     print(str(file))
