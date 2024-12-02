PDF & Text to LaTeX Converter with Spell Checker
This project is a robust utility for converting PDF files to LaTeX format, plain text to LaTeX, and vice versa. It also includes a spell checker for improved accuracy. The project is built using Python and utilizes libraries like PyPDF2, blob, and others.

Project Structure
Server Folder: Contains the main application logic for the conversions and spell-checking functionality.
Upload Folder: This is the designated directory where input files are uploaded for processing.
Download Folder: Stores the output files generated after processing.
Features
PDF to LaTeX Conversion:
Converts PDF documents into structured LaTeX files for academic or professional use.

Text to LaTeX Conversion:
Transforms plain text files into LaTeX format with basic LaTeX structures.

LaTeX to Text Conversion:
Extracts readable text from LaTeX documents, removing LaTeX commands.

Spell Checker:
Identifies and corrects spelling errors in input files for better accuracy.

Technologies Used
Languages: Python
Libraries:
PyPDF2: For PDF processing
blob: For efficient file handling
Other utilities for LaTeX parsing and spell checking
Version Control: Git
How to Use
Clone the repository:

git clone <repository-url>  
cd <project-folder>  
Install the required dependencies:

pip install -r requirements.txt  
Place your input files in the Upload folder.

Run the server script:

python server/main.py  
Processed files will be available in the Download folder after execution.

Testing
This project has been rigorously tested with various file formats and scenarios to ensure robust performance and reliability.

Contributions
Contributions are welcome! Please fork the repository and create a pull request with your improvements or bug fixes.

License
This project is licensed under the MIT License.