# Piracy Auditor

The Piracy Auditor aims to detect plagiarism in text and document files. Additionally, it provides functionality to compare two texts and two files for similarities. Follow the steps below to set up and run the project.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/tanwigeetika1618/Piracy_Auditor.git
$ cd Piracy_Auditor
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Usage
# Text Plagiarism Detection
The web application allows you to detect plagiarism in text files. To use this feature:
Click on the "Text" option on the navigation menu.
Enter text content you want to check for plagiarism.
The system will analyze the text and show you the results, indicating if any instances of plagiarism are detected.

# File Plagiarism Detection
The Piracy Auditor can also detect plagiarism in doc or text files. To use this feature:
Click on the "file" option on the navigation menu.
Upload a document file (e.g., txt, DOCX) that you want to check for plagiarism.
The system will process the document and display the results, showing if any cases of plagiarism are found.

# Text Comparison
The Piracy Auditor also offers text comparison functionality to compare two texts for similarities:
Click on the "compare" option on the navigation menu.
Enter the two texts you want to compare in the provided text input fields.
Click the "Compare" button, and the system will analyze the texts and display the similarities, if any.

# File Comparison
Additionally, you can compare two document files for similarities:
Click on the "compare" option on the navigation menu.
Upload two document files you wish to compare.
The system will process the files and show any similarities found between them.
