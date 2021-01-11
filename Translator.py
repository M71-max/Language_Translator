from translate import Translator

#translate from and to
print("Translates Spanish to English\n\n")
translator = Translator(from_lang = 'Spanish', to_lang = 'english')
message = input('Enter a message to translate : ')
print("\n\nThe Spanish is : ", translator.translate(message))
