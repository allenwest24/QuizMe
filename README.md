# Review Question Generator

This Python program uses the OpenAI API to generate review questions based on a given text. The program takes a file path and a number as input, reads the contents of the file into a string, and generates review questions based on the text. The program also allows the user to specify whether the number of questions is for the entire document or per page.

## Motivation:
I was studying for a couple certs but didn't want to buy the practice tests so I made this tool to paste the textbook into my program and have it feed me review questions. This tool is clutch for identifying items that should go into your SANS matrix.

## Requirements:

-    Python 3
-    openai

## Usage:

To use the program, you will need to set your OpenAI API key. Replace YOUR_API_KEY in the following line with your API key:
```
openai.api_key = "YOUR_API_KEY"
```

To run the program, pass the file path, number of review questions, and per_page flag as command line arguments:
```
python main.py FILE_PATH NUM_QUESTIONS [per_page]
-    FILE_PATH: The path to the file to generate review questions for.
-    NUM_QUESTIONS: The number of review questions to generate.
-    [per_page]: (optional) If specified, generates the specified number of review questions for each page in the file. If not specified, generates the specified number of review questions for the entire file.
```

## Examples:

Generate 5 review questions for the entire file:
```
python main.py file.txt 5
```

Generate 2 review questions for each page in the file:
```
python main.py file.txt 2 per_page
```

## Sample Output:
```
1. What is the purpose of dynamic analysis?
2. What is the difference between static and dynamic analysis?
3. What is the VBA debugging tool?
4. How do you use the VBA debugging tool?
```
