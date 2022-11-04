import playsound
import time
import datetime

print(f'chainsaw #1 played at {datetime.datetime.now().isoformat()}')
playsound.playsound('./chainsaw_test.mp3', block=True)

time.sleep(60)
print(f'chainsaw #2 played at {datetime.datetime.now().isoformat()}')
playsound.playsound('./chainsaw_test.mp3', block=True)

time.sleep(60)
print(f'handsaw #1 played at {datetime.datetime.now().isoformat()}')
playsound.playsound('./handsaw_test.mp3', block=True)

time.sleep(60)
print(f'handsaw #2 played at {datetime.datetime.now().isoformat()}')
playsound.playsound('./handsaw_test.mp3', block=True)

time.sleep(60)
print(f'gunshot #1 played at {datetime.datetime.now().isoformat()}')
playsound.playsound('./gunshot_test.mp3', block=True)
playsound.playsound('./gunshot_test.mp3', block=True)
playsound.playsound('./gunshot_test.mp3', block=True)
playsound.playsound('./gunshot_test.mp3', block=True)
playsound.playsound('./gunshot_test.mp3', block=True)

time.sleep(60)
print(f'gunshot #2 played at {datetime.datetime.now().isoformat()}')
playsound.playsound('./gunshot_test.mp3', block=True)
playsound.playsound('./gunshot_test.mp3', block=True)
playsound.playsound('./gunshot_test.mp3', block=True)
playsound.playsound('./gunshot_test.mp3', block=True)
playsound.playsound('./gunshot_test.mp3', block=True)

time.sleep(60)
print(f'laugh #1 played at {datetime.datetime.now().isoformat()}')
playsound.playsound('./laugh_test.mp3', block=True)

time.sleep(60)
print(f'laugh #2 played at {datetime.datetime.now().isoformat()}')
playsound.playsound('./laugh_test.mp3', block=True)
