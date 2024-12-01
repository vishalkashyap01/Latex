### VERSION - 1.3.1
from textblob import TextBlob

def correct_text(incorrect_text):
    # Create a TextBlob object
    blob = TextBlob(incorrect_text)
    
    # Correct the text using TextBlob's built-in correction
    corrected_text = blob.correct()
    
    return str(corrected_text)

# Example Usage
incorrect_text = input("enter the text here : ")
corrected_text = correct_text(incorrect_text)
print("Corrected Text:", corrected_text)



### VERSION 0.3.1 ###
# import os
# import re
# from spellchecker import SpellChecker

# def clean_text_file(input_file, output_file):
#     # Initialize spell checker
#     spell = SpellChecker()

#     try:
#         # Check if the input file exists in the current folder
#         if not os.path.exists(input_file):
#             print(f"Error: {input_file} does not exist in the current folder.")
#             return

#         # Read the content of the file
#         with open(input_file, 'r', encoding='utf-8') as file:
#             content = file.read()

#         # Remove extra spaces and normalize spacing
#         content = re.sub(r'\s+', ' ', content.strip())

#         # Correct spelling mistakes
#         words = content.split()
#         corrected_words = [spell.correction(word) if word not in spell else word for word in words]
#         corrected_text = ' '.join(corrected_words)

#         # Save the corrected content to a new file
#         with open(output_file, 'w', encoding='utf-8') as file:
#             file.write(corrected_text)

#         print(f"Text has been corrected and saved to {output_file}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# input_file = 'input.txt'  # Replace with your input file name
# output_file = 'output.txt'  # Replace with your output file name
# clean_text_file(input_file, output_file)




### VERSION - 0.2.1 ###
# import re
# from spellchecker import SpellChecker

# def clean_text_file(incorrect, correct):
#     # Initialize spell checker
#     spell = SpellChecker()

#     try:
#         # Read the content of the file
#         with open(input_file, 'r', encoding='utf-8') as file:
#             content = file.read()

#         # Remove extra spaces and normalize spacing
#         content = re.sub(r'\s+', ' ', content.strip())

#         # Correct spelling mistakes
#         words = content.split()
#         corrected_words = [spell.correction(word) if word not in spell else word for word in words]
#         corrected_text = ' '.join(corrected_words)

#         # Save the corrected content to a new file
#         with open(output_file, 'w', encoding='utf-8') as file:
#             file.write(corrected_text)

#         print(f"Text has been corrected and saved to {correct}")
#     except FileNotFoundError:
#         print(f"Error: {incorrect} does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# input_file = 'incorrect.txt'  # Replace with your input file path
# output_file = 'correct.txt'  # Replace with your output file path
# clean_text_file(input_file, output_file)






# from spellchecker import SpellChecker

# def spell_checker():
#     """
#     Reads a text file, checks for spelling errors, and corrects them.
#     """
#     try:
#         # Get file name from the user
#         file_name = input("Enter the name of the text file (e.g., document.txt): ").strip()

#         # Read file content
#         with open(file_name, 'r') as file:
#             content = file.readlines()

#         spell = SpellChecker()  # Initialize spell checker
#         corrected_content = []

#         # Process each line
#         for line in content:
#             words = line.split()  # Split line into words
#             corrected_line = []

#             for word in words:
#                 # Check if the word is misspelled
#                 corrected_word = spell.correction(word)
#                 if word != corrected_word:  # Only correct if it's actually misspelled
#                     print(f"Correcting: {word} -> {corrected_word}")
#                 corrected_line.append(corrected_word)

#             # Reconstruct the line
#             corrected_content.append(" ".join(corrected_line))

#         # Write corrected content back to the file
#         with open(file_name, 'w') as file:
#             file.write("\n".join(corrected_content))

#         print(f"Spelling corrections have been made to '{file_name}'.")
#     except FileNotFoundError:
#         print("Error: The specified file was not found. Please check the file name and try again.")
#     except PermissionError:
#         print("Error: Permission denied. Please check if the file is open or you have write permissions.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# # Run the function
# spell_checker()
