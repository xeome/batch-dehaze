import os
import subprocess

INPUT_PREFIX = "frame_"
OUTPUT_PREFIX = "dehazed_"

# How many processes in parallel in one cycle
JOB_COUNT = 12

INPUT_EXT = ".jpg"
OUTPUT_EXT = ".png"

INPUT_PATH = "./frames/"
OUTPUT_PATH = "./dehazed_frames/"

_, _, files = next(os.walk(INPUT_PATH))
FILE_COUNT = len(files)

cycles = FILE_COUNT // JOB_COUNT
remainder = FILE_COUNT % JOB_COUNT

for cycle in range(0, cycles + 1):
    if cycle != cycles:
        for i in range(0, JOB_COUNT):
            index = str(cycle * JOB_COUNT + i).rjust(6, "0")
            input = INPUT_PATH + INPUT_PREFIX + index
            output = OUTPUT_PATH + OUTPUT_PREFIX + index
            command = f"gmic -input {input}{INPUT_EXT} +jeje_dehaze 0.45,0.6,0.2,1,0,0,0,0,0 k[1] -output {output}{OUTPUT_EXT}"
            subprocess.Popen(["bash", "-c", command])
    else:
        for i in range(0, remainder):
            index = str(cycle * JOB_COUNT + i).rjust(6, "0")
            input = INPUT_PATH + INPUT_PREFIX + index
            output = OUTPUT_PATH + OUTPUT_PREFIX + index
            command = f"gmic -input {input}{INPUT_EXT} +jeje_dehaze 0.45,0.6,0.2,1,0,0,0,0,0 k[1] -output {output}{OUTPUT_EXT}"
            subprocess.Popen(["bash", "-c", command])
