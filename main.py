from gravador import Gravador_Audio,pyaudio

if __name__=='__main__':
    
    gravador = Gravador_Audio()
    
    audio = pyaudio.PyAudio()

    
    frames = gravador.gravacao_audio(audio)
    
    gravador.geracao_arquivo(frames, audio)
    
    