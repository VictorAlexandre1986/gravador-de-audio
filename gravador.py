import pyaudio
import wave

class Gravador_Audio:
    
    audio = pyaudio.PyAudio()
    
    def gravacao_audio(self,audio):

        #Criando um stream de audio
        stream = audio.open(
            #Vai receber o audio(microfone)
            input=True,
            #bits do audio
            format=pyaudio.paInt32,
            #qts canais(mono/stereo)
            channels=1,
            #Hertz
            rate=44000,
            #qtos pedacos de audio vai estar no bloco(tamanho do bloco)
            frames_per_buffer=1024,
            
        )
        
        frames = []
        try:
            while True:
                bloco = stream.read(1024)
                frames.append(bloco)
        except KeyboardInterrupt:
            pass

        stream.start_stream()
        stream.close()
        audio.terminate()
        
        return frames

    def geracao_arquivo(self, frames, audio):
        with wave.open('gravacao.wav','wb') as arquivo_final:
            arquivo_final.setnchannels(1)
            arquivo_final.setframerate(44000)
            arquivo_final.setsampwidth(audio.get_sample_size(pyaudio.paInt32))
            arquivo_final.writeframes(b"".join(frames))