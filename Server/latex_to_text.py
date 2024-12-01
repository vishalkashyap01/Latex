### VERSION - 0.0.3 ###
import re

def latex_to_text(input_report, back_to_text):
    """
    Converts a LaTeX file to a plain text file by removing LaTeX commands.
    
    :param input_file: Path to the LaTeX file
    :param output_file: Path to the output text file
    """
    try:
        with open(output_report, 'r') as infile, open(back_to_text, 'w') as outfile:
            for line in infile:
                # Remove LaTeX commands using regex
                line = re.sub(r"\\[a-zA-Z]+(\[[^\]]*\])?(\{[^\}]*\})?", "", line)  # Commands like \section{}, \textbf{}
                line = re.sub(r"\{[^\}]*\}", "", line)  # Remove braces
                line = re.sub(r"%.*", "", line)  # Remove comments
                line = line.strip()  # Remove leading and trailing spaces
                
                if line:  # Write non-empty lines
                    outfile.write(line + "\n")

        print(f"Converted LaTeX to text: {back_to_text}")
    except Exception as e:
        print(f"Error: {e}")

# usage
output_report = "output_report.tex"  # Replace with your LaTeX file path
back_to_text = "back_to_text.txt"  # Replace with your desired text file path

latex_to_text(output_report, back_to_text)
