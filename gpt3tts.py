from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import openai
import gtts

prompt = ''

openai.api_key = "API KEY HERE"

while prompt != "exit":
    prompt = input("Enter question or 'exit' to quit: ")
    print(prompt)
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=f"The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, "
               f"and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help "
               f"you today?\nHuman:{prompt}\nAI:",
        temperature=0.9,
        max_tokens=32,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    generated_text = response["choices"][0]["text"]
    print(f"output: {generated_text}")

    tts = gtts.gTTS(text=generated_text, lang='en')

    with tempfile.NamedTemporaryFile(suffix='.mp3') as f:
        tts.save(f.name)
        sound = AudioSegment.from_file(f.name, format="mp3")
        play(sound)
