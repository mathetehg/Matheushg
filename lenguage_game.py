import sounddevice as sd
import numpy as np
import random
import scipy.io.wavfile as wav
import speech_recognition as sr
from deep_translator import MyMemoryTranslator

# dicionario de dificuldades com palavras em pt-br e suas traduções em ingls
words_by_level = {
    "fácil": {"gato": "cat", "cachorro": "dog", "maçã": "apple"},
    "médio": {"casa": "house", "escola": "school", "janela": "window"},
    "difícil": {
        "tecnologia": "technology",
        "universidade": "university",
        "imaginação": "imagination",
    },
}


print("=" * 45)
print("🎮 BEM-VINDO AO JOGO DE PRONÚNCIA EM INGLÊS! 🎙️")
print("=" * 45)
print("Regras: Traduza a palavra mostrada para o ingles.")
print("⚠️ Atenção: O jogo termina após 3 erros! ❗")

print("Escolha o nível de dificuldade:")
print("🟩 Fácil 🟩")
print("🟨 Médio 🟨")
print("🟥 Difícil 🟥")

escolha = input("Digite o número do nível (1, 2 ou 3): ")

if escolha == "1":
     nivel = "fácil"
elif  escolha == "2":
     nivel = "médio"
elif escolha == "3":
     nivel = "difícil"
else:
     print("❌ Opção inválida! O nível fácil será selecionado por padrão. 📘")
     nivel = "fácil"

ponto = 0 #isso é os ponto
erro = 0 #isso é os erros  
recognizer = sr.Recognizer() #isso eu n entendi, mas de acordo com a IA eu presciso disso pra mudar o nome

duration = 5  #5 segundos de gravação
sample_rate = 44100

if escolha == "3":
    duration = 3

while erro < 3:
     palavra_pt, traducao_en = random.choice(
          list(words_by_level[nivel].items())
     )

     print("=" * 45)
     print(f"🎯 Traduza para o inglês a palavra: {palavra_pt.upper()}")
     print(f"📊 Placar -> Pontos: {ponto} | ❌ Erros: {erro}")
     print("=" * 45)

     input("💬 Aperte enter quando quiser começar a falar! 🎤")


#iiaaaaaaaaaaaaaaaaaaaaaaaaa
     print("Fale agora...")
     recording = sd.rec(
      int(duration * sample_rate),
      samplerate=sample_rate,
      channels=1,
      dtype="int16",
  )
     sd.wait()

     wav.write("output.wav", sample_rate, recording)
     print("Gravação concluída, estou em reconhecimento...")

  # 2. Ler o áudio gravado
     with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)

     try:
        # Mudámos para "en-US" porque o jogador fala em inglês!
        text = recognizer.recognize_google(audio, language="en-US")
        text = text.lower().strip()  # Deixar tudo minúsculo para comparar melhor
        print(f"Você disse: '{text}' | Tradução esperada: '{traducao_en}'")

        # 3. Verificar se acertou
        if text == traducao_en.lower():
            print("🎉 ACERTASTE! Parabéns! +1 ponto 🌟\n")
            ponto += 1
        else:
            print(f"❌ Erraste! A palavra correta era '{traducao_en}'.\n")
            erro += 1

     except sr.UnknownValueError:
        print("🤖 Não consegui entender a fala devido a ruídos ou silêncio.\n")
        erro += 1
     except sr.RequestError as e:
        print(f"🔌 Service error: {e}\n")
        break

# Quando o erro chegar a 3, o ciclo termina e cai aqui:
print("=" * 45)
print("💀 FIM DE JOGO!")
print(f"🏆 Pontuação final: {ponto} ponto(s).")
print("=" * 45)
