from app.commands import Command

class SplitWord(Command):
    def execute(self, *args):
        try:
            words = ' '.join(args)
            letters = [letter for word in words.split() for letter in word]
            print(f"The letters of the words {words} are: {letters}")
        except Exception as e:
            print(f"Error: {e}")
            
class RemoveSpace(Command):
    def execute(self, *args):
        try:
            # Join the input arguments to form a sentence
            sentence = ' '.join(args)
            # Remove spaces from the sentence
            sentence_without_spaces = sentence.replace(' ', '')
            # Print the modified sentence
            print(f"The sentence after removing spaces is: {sentence_without_spaces}")
        except Exception as e:
            print(f"Error: {e}")

class NextLine(Command):
    def execute(self, *args):
        try:
            sentence = ' '.join(args)
            sentence_with_next_line = sentence.replace(' ', '\n')
            print(f"The sentence with next line char is :\n {sentence_with_next_line}")
        except Exception as e:
            print(f"Error: {e}")