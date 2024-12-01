# VERSION - 1.1.0
import os

def text_to_latex():
    """
    Converts a plain text file to a LaTeX file with enhanced formatting and structure.
    """
    try:
        # Define directories for input and output
        input_dir = "Download"  # select which folder to input the file
        output_dir = "Upload" # select which folder to see the changes or output of the text file

        # Get file names from the user
        input_filename = input("Enter the plain text file name (e.g., input.txt): ").strip()
        output_filename = input("Enter the output LaTeX file name (e.g., output.tex): ").strip()

        # Construct full paths
        input_file = os.path.join(input_dir, input_filename)
        output_file = os.path.join(output_dir, output_filename)

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Read the input text file and format it into LaTeX
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            # Write the LaTeX document preamble
            outfile.write(r"""\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{hyperref} % For clickable links
\usepackage{setspace} % For custom spacing
\usepackage{geometry} % To adjust margins
\geometry{margin=1in}
\title{Enhanced LaTeX Document}
\author{Automated Converter}
\date{\today}

\begin{document}

\maketitle

\onehalfspacing

""")
            # Variables to track context
            in_itemize = False  # Tracks if we are inside a list
            
            for line in infile:
                line = line.strip()
                if not line:  # Handle blank lines as paragraph breaks
                    if in_itemize:  # Close any open itemize environment
                        outfile.write(r"\end{itemize}" + "\n\n")
                        in_itemize = False
                    outfile.write("\n\n")
                elif line.startswith("# "):  # Convert "# " to section
                    if in_itemize:  # Close any open itemize environment
                        outfile.write(r"\end{itemize}" + "\n\n")
                        in_itemize = False
                    outfile.write(r"\section{" + line[2:].capitalize() + "}\n")
                elif line.startswith("## "):  # Convert "## " to subsection
                    if in_itemize:  # Close any open itemize environment
                        outfile.write(r"\end{itemize}" + "\n\n")
                        in_itemize = False
                    outfile.write(r"\subsection{" + line[3:].capitalize() + "}\n")
                elif line.startswith("- "):  # Convert "- " to list items
                    if not in_itemize:
                        outfile.write(r"\begin{itemize}" + "\n")
                        in_itemize = True
                    outfile.write(r"\item " + line[2:] + "\n")
                elif line.startswith("**"):  # Convert "**bold**" to bold text
                    bold_text = line.strip("*").capitalize()
                    outfile.write(r"\textbf{" + bold_text + "}" + "\n")
                elif line.startswith("_"):  # Convert "_italic_" to italic text
                    italic_text = line.strip("_").capitalize()
                    outfile.write(r"\textit{" + italic_text + "}" + "\n")
                else:  # Regular text
                    if in_itemize:  # Close any open itemize environment
                        outfile.write(r"\end{itemize}" + "\n\n")
                        in_itemize = False
                    outfile.write(line.capitalize() + "\n")

            # Close any open environments
            if in_itemize:
                outfile.write(r"\end{itemize}" + "\n\n")

            # Write the LaTeX document end
            outfile.write(r"""
\end{document}
""")

        print(f"Conversion complete! LaTeX file saved as: {output_filename} (located in '{output_dir}' directory)")
    except FileNotFoundError:
        print("Error: The specified text file was not found in the 'Download' directory. Please check the file name and try again.")
    except PermissionError:
        print("Error: Permission denied. Please check if the output file is open or you have write permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
text_to_latex()


# input --> upload folder
# output <-- download folder
# File creation is supported!!!