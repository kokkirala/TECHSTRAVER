import sympy as sp
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

operations = {
    'add': '+',
    'plus': '+',
    'subtract': '-',
    'minus': '-',
    'multiply': '*',
    'times': '*',
    'divide': '/',
    'over': '/'
}

def process_input(query):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(query)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
   
    operation = None
    numbers = []
    
    for word in filtered_words:
        if word.lower() in operations:
            operation = operations[word.lower()]
        else:
            try:
                
                number = sp.sympify(word)
                numbers.append(number)
            except sp.SympifyError:
                pass
    
    if len(numbers) == 2 and operation:
        return numbers[0], numbers[1], operation
    else:
        return None, None, None

# Function to compute the result
def compute_result(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return None

# Main function
def prompt_based_calculator():
    print("Welcome to the Prompt-Based Calculator!")
    print("You can ask me to perform basic arithmetic operations like addition, subtraction, multiplication, and division.")
    print("For example, you can say 'Add 3 and 5' or 'What is 7 minus 2?'")
    
    while True:
        query = input("\nEnter your mathematical query (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            print("Goodbye!")
            break
        
        num1, num2, operation = process_input(query)
        
        if num1 is not None and num2 is not None and operation is not None:
            result = compute_result(num1, num2, operation)
            print(f"The result of {num1} {operation} {num2} is: {result}")
        else:
            print("Sorry, I didn't understand your query. Please try again.")


prompt_based_calculator()
