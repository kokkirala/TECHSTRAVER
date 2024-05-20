from googletrans import Translator # type: ignore

def translate_text(text, target_language):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_language)
        return translation.text
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    print("Welcome to the Basic Language Translation Tool!")
    print("You can ask me to translate text between different languages.")
    
    while True:
        text = input("\nEnter the text to be translated (or type 'exit' to quit): ")
        if text.lower() == 'exit':
            print("Goodbye!")
            break
        
        target_language = input("Enter the target language (e.g., 'fr' for French, 'es' for Spanish): ")
        
        translation = translate_text(text, target_language)
        print(f"Translation: {translation}")

if __name__ == "__main__":
    main()
