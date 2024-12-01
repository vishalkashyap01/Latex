import os

def text_to_latex():
    """
    Converts a plain text file to a LaTeX file by formatting text into LaTeX syntax.
    """
    try:
        # Define directories for input and output
        input_dir = "Upload"
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





### VERSION - 0.3.1

# def text_to_latex():
#     """
#     Converts a plain text file to a LaTeX document.
#     """
#     try:
#         # Get input file name from the user
#         test = input("Enter the name of the input text file (e.g., 'input.txt'): ").strip()
#         if not test:
#             print("Input file name cannot be empty. Please try again.")
#             return
        
#         # Get output file name from the user
#         Output = input("Enter the name of the output LaTeX file (e.g., 'output.tex'): ").strip()
#         if not Output:
#             print("Output file name cannot be empty. Please try again.")
#             return
        
#         with open(test, 'r') as infile, open(Output, 'w') as outfile:
#             # Write the LaTeX document preamble
#             outfile.write(r"""\documentclass{article}
# \usepackage[utf8]{inputenc}
# \title{Generated LaTeX Document}
# \author{Automated Converter}
# \date{\today}

# \begin{document}

# \maketitle

# """)
#             # Process each line of the input file
#             in_itemize = False  # Track if inside an itemize block
#             for line in infile:
#                 line = line.strip()
#                 if not line:  # Handle blank lines as paragraph breaks
#                     if in_itemize:  # Close the itemize environment
#                         outfile.write(r"\end{itemize}" + "\n")
#                         in_itemize = False
#                     outfile.write("\n\n")
#                 elif line.startswith("# "):  # Convert "# " to section
#                     if in_itemize:  # Close the itemize environment
#                         outfile.write(r"\end{itemize}" + "\n")
#                         in_itemize = False
#                     outfile.write(r"\section{" + line[2:] + "}\n")
#                 elif line.startswith("## "):  # Convert "## " to subsection
#                     if in_itemize:  # Close the itemize environment
#                         outfile.write(r"\end{itemize}" + "\n")
#                         in_itemize = False
#                     outfile.write(r"\subsection{" + line[3:] + "}\n")
#                 elif line.startswith("- "):  # Convert "- " to list item
#                     if not in_itemize:
#                         outfile.write(r"\begin{itemize}" + "\n")
#                         in_itemize = True
#                     outfile.write(r"\item " + line[2:] + "\n")
#                 else:  # Regular text
#                     if in_itemize:  # Close the itemize environment
#                         outfile.write(r"\end{itemize}" + "\n")
#                         in_itemize = False
#                     outfile.write(line + "\n")
            
#             # Close any open list environment
#             if in_itemize:
#                 outfile.write(r"\end{itemize}" + "\n")

#             # Write the LaTeX document end
#             outfile.write(r"""
# \end{document}
# """)

#         print(f"Conversion complete! LaTeX file saved as: {Output}")

#     except FileNotFoundError:
#         print(f"Error: The file '{test}' does not exist. Please check the file name and try again.")
#     except Exception as e:
#         print(f"An error occurred: {e}")


# # Run the function
# text_to_latex()





### VERSION - 0.2.0

# def text_to_latex(test, Output):
#     """
#     Converts a plain text file to a LaTeX document.
    
#     :param input_file: Path to the input text file
#     :param output_file: Path to the output LaTeX file
#     """
#     try:
#         with open(test, 'r') as infile, open(Output, 'w') as Output:
#             # Write the LaTeX document preamble
#             Output.write(r"""\documentclass{article}
# \usepackage[utf8]{inputenc}
# \title{Generated LaTeX Document}
# \author{Automated Converter}
# \date{\today}

# \begin{document}

# \maketitle

# """)
#             # Process each line of the input file
#             for line in infile:
#                 line = line.strip()
#                 if not line:  # Handle blank lines as paragraph breaks
#                     Output.write("\n\n")
#                 elif line.startswith("# "):  # Convert "# " to section
#                     Output.write(r"\section{" + line[2:] + "}\n")
#                 elif line.startswith("## "):  # Convert "## " to subsection
#                     Output.write(r"\subsection{" + line[3:] + "}\n")
#                 elif line.startswith("- "):  # Convert "- " to list item
#                     if not Output.tell() or not Output.getvalue().endswith(r"\begin{itemize}\n"):
#                         Output.write(r"\begin{itemize}" + "\n")
#                     Output.write(r"\item " + line[2:] + "\n")
#                 else:  # Regular text
#                     Output.write(line + "\n")
            
#             # Close any open list environment
#             if Output.tell() and r"\begin{itemize}" in Output.getvalue():
#                 Output.write(r"\end{itemize}" + "\n")

#             # Write the LaTeX document end
#             Output.write(r"""
# \end{document}
# """)

#         print(f"Conversion complete! LaTeX file saved as: {Output}")

#     except Exception as e:
#         print(f"An error occurred: {e}")


# # usage
# test = input("enter the text  file here name >>> ")  # Replace with your input text file
# Output = input("enter the latex file name here <<< ")  # Replace with your desired output LaTeX file

# text_to_latex(test, Output)