import markovify

def generate_lyrics(corpus_path):
    with open(corpus_path, 'r', encoding='utf-8') as f:
        data = f.read().splitlines()

    text_model = markovify.Text(data)
    generated_lyrics = text_model.make_sentence()

    print("Letras generadas:")
    print(generated_lyrics)

corpus_file = 'canciones.txt'
generate_lyrics(corpus_file)
