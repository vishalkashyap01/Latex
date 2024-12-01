### VERSION - 1.0.3 ###
import re
import os

def latex_to_text():
    """
    Converts a LaTeX file to a plain text file by removing LaTeX commands.
    """
    try:
        # Define directories for input and output
        input_dir = "Download"
        output_dir = "Download"

        # Get file names from the user
        input_filename = input("Enter the LaTeX file name (e.g., output_report.tex): ").strip()
        output_filename = input("Enter the output text file name (e.g., back_to_text.txt): ").strip()

        # Construct full paths
        input_file = os.path.join(input_dir, input_filename)
        output_file = os.path.join(output_dir, output_filename)

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Read and process the LaTeX file
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                # Remove LaTeX commands using regex
                line = re.sub(r"\\[a-zA-Z]+(\[[^\]]*\])?(\{[^\}]*\})?", "", line)  # Commands like \section{}, \textbf{}
                line = re.sub(r"\{[^\}]*\}", "", line)  # Remove braces
                line = re.sub(r"%.*", "", line)  # Remove comments
                line = line.strip()  # Remove leading and trailing spaces
                
                if line:  # Write non-empty lines
                    outfile.write(line + "\n")

        print(f"Converted LaTeX file to plain text: {output_filename} (located in '{output_dir}' directory)")
    except FileNotFoundError:
        print("Error: The specified LaTeX file was not found in the 'Download' directory. Please check the file name and try again.")
    except PermissionError:
        print("Error: Permission denied. Please check if the output file is open or you have write permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
latex_to_text()




### VERSION - 0.0.3 ###
# import re

# def latex_to_text(input_report, back_to_text):
#     """
#     Converts a LaTeX file to a plain text file by removing LaTeX commands.
    
#     :param input_file: Path to the LaTeX file
#     :param output_file: Path to the output text file
#     """
#     try:
#         with open(output_report, 'r') as infile, open(back_to_text, 'w') as outfile:
#             for line in infile:
#                 # Remove LaTeX commands using regex
#                 line = re.sub(r"\\[a-zA-Z]+(\[[^\]]*\])?(\{[^\}]*\})?", "", line)  # Commands like \section{}, \textbf{}
#                 line = re.sub(r"\{[^\}]*\}", "", line)  # Remove braces
#                 line = re.sub(r"%.*", "", line)  # Remove comments
#                 line = line.strip()  # Remove leading and trailing spaces
                
#                 if line:  # Write non-empty lines
#                     outfile.write(line + "\n")

#         print(f"Converted LaTeX to text: {back_to_text}")
#     except Exception as e:
#         print(f"Error: {e}")

# # usage
# output_report = "output_report.tex"  # Replace with your LaTeX file path
# back_to_text = "back_to_text.txt"  # Replace with your desired text file path

# latex_to_text(output_report, back_to_text)
