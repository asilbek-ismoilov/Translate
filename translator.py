from deep_translator import GoogleTranslator as G

def tarjimon(text):
    tarjima = G(source="uz", target="en").translate(text)
    return tarjima

# print(tarjimon("Salom"))