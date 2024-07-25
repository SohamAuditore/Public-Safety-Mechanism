import pyaudio
import wave
import random
import sound
#print(clk)
 
def record():
    clk = random.randint(8,500)
    frames = []
    print('Recording....')
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    try:
        while True:
            data = stream.read(1024)
            frames.append(data)
    except KeyboardInterrupt:
        pass

    stream.stop_stream()
    stream.close()
    audio.terminate()

    sound_file = wave.open(f"myrecording{clk}.wav","wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()
    print('Recording Stopped')
    return f"myrecording{clk}.wav"
