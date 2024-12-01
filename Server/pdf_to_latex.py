from PyPDF2 import PdfReader
import os

def pdf_to_latex():
    """
    Converts the text from a PDF file to a LaTeX document, requiring only file names.
    """
    try:
        # Define directories for input and output
        input_dir = "upload"
        output_dir = "Download"

        # Get file names from the user
        input_filename = input("Enter the PDF file name (e.g., Report.pdf): ").strip()
        output_filename = input("Enter the output LaTeX file name (e.g., vishal.tex): ").strip()

        # Construct full paths
        input_pdf = os.path.join(input_dir, input_filename)
        output_tex = os.path.join(output_dir, output_filename)

        # Load the PDF
        reader = PdfReader(input_pdf)

        with open(output_tex, 'w') as outfile:
            # Write LaTeX preamble
            outfile.write(r"""\documentclass{article}
\usepackage[utf8]{inputenc}
\title{Converted PDF to LaTeX}
\author{Automated Script}
\date{\today}

\begin{document}

\maketitle

""")
            # Extract and write text from each page
            for i, page in enumerate(reader.pages):
                outfile.write(f"% Page {i+1}\n")
                text = page.extract_text().replace("\n", " ")  # Flatten lines
                outfile.write(f"{text}\n\n")

            # End document
            outfile.write(r"\end{document}")

        print(f"LaTeX file created successfully in '{output_dir}' directory as '{output_filename}'!")
    except FileNotFoundError:
        print("Error: The specified PDF file was not found in the 'upload' directory. Please check the file name and try again.")
    except PermissionError:
        print("Error: Permission denied. Please check if the output file is open or you have write permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
pdf_to_latex()



### VERSION - 0.1.2
# from PyPDF2 import PdfReader

# def pdf_to_latex():
#     """
#     Converts the text from a PDF file to a LaTeX document.
#     """
#     try:
#         # Get user inputs for file names
#         input_pdf = input("Enter the path of the PDF file (e.g., upload/Report.pdf): ").strip()
#         output_tex = input("Enter the path of the output LaTeX file (e.g., Download/vishal.tex): ").strip()

#         # Load the PDF
#         reader = PdfReader(input_pdf)

#         with open(output_tex, 'w') as outfile:
#             # Write LaTeX preamble
#             outfile.write(r"""\documentclass{article}
# \usepackage[utf8]{inputenc}
# \title{Converted PDF to LaTeX}
# \author{Automated Script}
# \date{\today}

# \begin{document}

# \maketitle

# """)
#             # Extract and write text from each page
#             for i, page in enumerate(reader.pages):
#                 outfile.write(f"% Page {i+1}\n")
#                 text = page.extract_text().replace("\n", " ")  # Flatten lines
#                 outfile.write(f"{text}\n\n")

#             # End document
#             outfile.write(r"\end{document}")

#         print(f"LaTeX file created successfully at: {output_tex}")
#     except FileNotFoundError:
#         print("Error: The specified PDF file was not found. Please check the file path and try again.")
#     except PermissionError:
#         print("Error: Permission denied. Please check if the output file is open or you have write permissions.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# # Run the function
# pdf_to_latex()





### VERSION - 0.1.1 ###
# from PyPDF2 import PdfReader

# def pdf_to_latex(Pdf, Latex):
#     """
#     Converts the text from a PDF file to a LaTeX document.
    
#     :param input_pdf: Path to the input PDF file
#     :param output_tex: Path to the output LaTeX file
#     """
#     try:
#         reader = PdfReader(Pdf)
#         with open(Latex, 'w') as outfile:
#             # LaTeX preamble
#             outfile.write(r"""\documentclass{article}
# \usepackage[utf8]{inputenc}
# \title{Converted PDF to LaTeX}
# \author{Automated Script}
# \date{\today}

# \begin{document}

# \maketitle

# """)
#             # Extract and write text from each page
#             for i, page in enumerate(reader.pages):
#                 outfile.write(f"% Page {i+1}\n")
#                 text = page.extract_text().replace("\n", " ")  # Extract text and flatten lines
#                 outfile.write(f"{text}\n\n")

#             # End document
#             outfile.write(r"\end{document}")

#         print(f"LaTeX file created: {Latex}!!!")
#     except Exception as e:
#         print(f"Error: {e}")

# # Usage
# input_pdf = "upload/Report.pdf"
# output_tex = "Download/vishal.tex"

# pdf_to_latex(input_pdf, output_tex)
