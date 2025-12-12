import cv2
import time
import os
import getopt, sys
import audioop as audioop
sys.modules['audioop'] = audioop
from pydub import AudioSegment
from pydub.playback import play
import threading
import math
from pydub.effects import normalize




video = cv2.VideoCapture()
audio = AudioSegment.silent(duration=0)
auval = None

def check_none_audio(audio):
    if audio.duration_seconds <= 0:
        return AudioSegment.from_file("Examples/output.mp3")
    return audio


args = sys.argv[1:]
options = "f:a:h:v:"
long_options = ["File=", "Audio=", "help","Volume="]
try:
    arguments, values = getopt.getopt(args, options, long_options)
    for currentArg, currentVal in arguments:
        if currentArg in ("-f", "--File"):
            video = cv2.VideoCapture(currentVal)
            if not video.isOpened():
                video = cv2.VideoCapture("Examples/BadApple.mp4")

        if currentArg in ("-a", "--Audio"):
            audio = AudioSegment.from_file(currentVal)

        if currentArg in ("-v", "--Volume"):
            try:
                audio = check_none_audio(audio)
                auval = float(currentVal)  # percent
                if auval <= 0:
                    print("Volume must be > 0")
                if auval is not None:
                    # Convert percent to dB change
                    db_change = 20 * math.log10(max(auval, 1) / 100)
                    audio = audio + db_change
                    print(f"Volume set to {auval}% ({db_change:.2f} dB)")

            except ValueError:
                print("Invalid volume value.")

except getopt.error as err:
    print(str(err))


audio = check_none_audio(audio)


if not video.isOpened():
    video = cv2.VideoCapture("Examples/BadApple.mp4")

threading.Thread(target=play, args=(audio,), daemon=True).start()
# Get the FPS of the video (fallback to 30 if unknown)
fps = video.get(cv2.CAP_PROP_FPS)
if fps <= 0:
    fps = 30
frame_delay = 1 / fps

# Hide cursor and clear screen for cleaner animation
os.system("cls" if os.name == "nt" else "clear")
print("\033[?25l", end="")  # hide cursor


start_time = time.time()
frame_count = 0
try:
    while True:
        ret, frame = video.read()
        if not ret:
            break

        frame = cv2.resize(frame, (200, 60), interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        for y in range(gray.shape[0]):
            row = ""
            for x in range(gray.shape[1]):
                row += "★" if gray[y, x] > 128 else " "
            print(row)
        print("\033[H", end="")

       
        frame_count += 1
        expected_time = frame_count * frame_delay
        actual_time = time.time() - start_time
        sleep_time = expected_time - actual_time
        if sleep_time > 0:
            time.sleep(sleep_time)

finally:
    print("\033[?25h", end="")
    video.release()
