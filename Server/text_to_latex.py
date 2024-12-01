import os

def text_to_latex():
    """
    Converts a plain text file to a LaTeX file by formatting text into LaTeX syntax.
    """
    try:
        # Define directories for input and output
        input_dir = "Download"
        output_dir = "Download"

        # Get file names from the user
        input_filename = input("Enter the plain text file name (e.g., input.txt): ").strip()
        output_filename = input("Enter the output LaTeX file name (e.g., formatted_output.tex): ").strip()

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
\title{Generated LaTeX Document}
\author{Automated Converter}
\date{\today}

\begin{document}

\maketitle

""")
            for line in infile:
                line = line.strip()  # Remove leading and trailing spaces
                if not line:  # Blank lines are treated as paragraph breaks
                    outfile.write("\n\n")
                elif line.startswith("# "):  # Convert "# " to section
                    outfile.write(r"\section{" + line[2:] + "}\n")
                elif line.startswith("## "):  # Convert "## " to subsection
                    outfile.write(r"\subsection{" + line[3:] + "}\n")
                elif line.startswith("- "):  # Convert "- " to list items
                    outfile.write(r"\begin{itemize}" + "\n")
                    outfile.write(r"\item " + line[2:] + "\n")
                    outfile.write(r"\end{itemize}" + "\n")
                else:  # Regular text
                    outfile.write(line + "\n")

            # Write the LaTeX document end
            outfile.write(r"""
\end{document}
""")

        print(f"Converted text file to LaTeX: {output_filename} (located in '{output_dir}' directory)")
    except FileNotFoundError:
        print("Error: The specified text file was not found in the 'Download' directory. Please check the file name and try again.")
    except PermissionError:
        print("Error: Permission denied. Please check if the output file is open or you have write permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
text_to_latex()
