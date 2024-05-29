from gtts import gTTS

def text_to_mp3(input_text_file, output_mp3_file, language='en'):
    # Read the text from the input file
    with open(input_text_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Create a gTTS object
    tts = gTTS(text=text, lang=language)
    
    # Save the audio file as MP3
    tts.save(output_mp3_file)

# Example usage
input_text_file = 'story5.txt'  # Path to the input text file
output_mp3_file = 'output.mp3'   # Path to the output MP3 file
text_to_mp3(input_text_file, output_mp3_file)
