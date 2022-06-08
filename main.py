import os
import subprocess
import time
import psutil

INPUT_PREFIX = "frame_"
OUTPUT_PREFIX = "dehazed_"

# How many processes in one cycle
JOB_COUNT = 12

INPUT_EXT = ".jpg"
OUTPUT_EXT = ".png"

INPUT_PATH = "./keep/"
OUTPUT_PATH = "./dehazed_frames/"

# +jeje_dehaze 0.45,0.6,0.2,1,0,0,0,0,0 k[1]

FILTER = "fx_freaky_details 0.2,40,1,11,0,50,50"

INPUTFILES = os.listdir(INPUT_PATH)
FILE_COUNT = len(INPUTFILES)

DELAY_MULTIPLIER = 18  # higher is faster, and more ram percentage used

cycles = FILE_COUNT // JOB_COUNT
remainder = FILE_COUNT % JOB_COUNT

for cycle in range(0, cycles + 1):
    mem = psutil.virtual_memory()
    if cycle != cycles:
        for i in range(0, JOB_COUNT):
            mem = psutil.virtual_memory()
            index = cycle * JOB_COUNT + i
            input = INPUTFILES[index]
            output = (INPUTFILES[index].replace(INPUT_PREFIX, OUTPUT_PREFIX)).replace(
                INPUT_EXT, OUTPUT_EXT
            )
            command = f"gmic -input {INPUT_PATH}{input} {FILTER} -output {OUTPUT_PATH}{output}"
            subprocess.Popen(["bash", "-c", command])
            time.sleep(mem.percent / (DELAY_MULTIPLIER * JOB_COUNT))

    else:
        for i in range(0, remainder):
            index = cycle * JOB_COUNT + i
            input = INPUTFILES[index]
            output = (INPUTFILES[index].replace(INPUT_PREFIX, OUTPUT_PREFIX)).replace(
                INPUT_EXT, OUTPUT_EXT
            )
            command = f"gmic -input {INPUT_PATH}{input} {FILTER} -output {OUTPUT_PATH}{output}"
            subprocess.Popen(["bash", "-c", command])
