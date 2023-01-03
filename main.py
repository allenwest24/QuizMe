import openai
import sys

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def generate_review_questions(prompt, model, temperature, num_questions, per_page):
    """
    Generate review questions based on the given prompt.
    
    Parameters:
        prompt (str): The text to generate review questions for.
        model (str): The name of the OpenAI model to use for generation.
        temperature (float): The temperature to use when generating the questions.
        num_questions (int): The number of review questions to generate.
        per_page (bool): If True, generate the specified number of review questions for each page in the prompt.
                         If False, generate the specified number of review questions for the entire prompt.
    
    Returns:
        A list of review questions generated from the prompt.
    """
    review_questions = []
    if per_page:
        # Split the prompt into pages
        pages = prompt.split("\n\n")
        for page in pages:
            # Generate the specified number of review questions for each page
            page_questions = []
            for i in range(num_questions):
                completions = openai.Completion.create(
                    engine=model,
                    prompt=f"Review questions for the following text:\n{page}\n\n",
                    max_tokens=1024,
                    n=1,
                    temperature=temperature,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                page_questions.append(completions.choices[0].text)
            review_questions.extend(page_questions)
    else:
        # Generate the specified number of review questions for the entire document
        for i in range(num_questions):
            completions = openai.Completion.create(
                engine=model,
                prompt=f"Review questions for the following text:\n{prompt}\n\n",
                max_tokens=1024,
                n=1,
                temperature=temperature,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            review_questions.append(completions.choices[0].text)
    return review_questions

# Get the file path from the first argument
file_path = sys.argv[1]

# Get the number of review questions from the second argument
num_questions = int(sys.argv[2])

# Determine if the number of questions is for each page or the entire document
per_page = False
if len(sys.argv) > 3:
    per_page = sys.argv[3] == "per_page"

# Read the contents of the file into a string
with open(file_path, "r") as f:
    prompt = f.read()

# Generate the review questions
review_questions = generate_review_questions(prompt, "text-davinci-002", 0, num_questions, per_page)

# Print the review questions
for question in review_questions:
    print(question)
