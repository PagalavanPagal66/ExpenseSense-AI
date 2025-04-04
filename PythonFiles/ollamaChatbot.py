import requests
import json
import dbToText as db
import streamlit as st
import main

# Set up the base URL for the local Ollama API
url = "http://localhost:11434/api/chat"
apiurl = "http://127.0.0.1:8000/"


def format_budget_data(budget_data):
    """
    Converts a list of budget records into a human-readable summary.

    Args:
        budget_data (dict): A dictionary with a "data" key containing a list of budget-related entries.

    Returns:
        str: A formatted summary of the budget data.
    """
    records = budget_data.get("data", [])

    if not records:
        return "No budget data available."

    summary = "Here is the summary of my financial budget records:\n"

    category_totals = {}

    for category, amount in records:
        amount = float(amount)  # Ensure amount is a float

        # Update category-wise totals
        category_totals[category] = category_totals.get(category, 0) + amount

        summary += f"- ₹{amount} recorded under '{category}' category.\n"

    summary += "\nTotal amount by category:\n"
    for category, total in category_totals.items():
        summary += f"- {category}: ₹{total}\n"

    return summary


def format_expense_data(expense_data):
    """
    Converts a list of expense records into a human-readable summary.

    Args:
        expense_data (dict): A dictionary with a "data" key containing a list of expenses.

    Returns:
        str: A formatted summary of expenses.
    """
    records = expense_data.get("data", [])

    if not records:
        return "No expense data available."

    summary = "Here is the summary of my expenses:\n"

    category_totals = {}

    for item, amount, category in records:
        amount = float(amount)  # Ensure amount is a float

        # Update category-wise totals
        category_totals[category] = category_totals.get(category, 0) + amount

        summary += f"- Spent ₹{amount} on {item} under '{category}' category.\n"

    summary += "\nTotal expenditure by category:\n"
    for category, total in category_totals.items():
        summary += f"- {category}: ₹{total}\n"

    print(summary)
    return summary

def get_ollama_response(question):
    url1 = apiurl+"return"
    url2 = apiurl+"returnB"
    expenseResponse = requests.get(url1)
    budgetResponse = requests.get(url2)
    # Check if the request was successful
    if expenseResponse.status_code == 200:
        expenseJson = expenseResponse.json()  # Convert JSON response to Python dictionary
        print("Expense Data:", expenseJson)
    else:
        print("Expense Error:", expenseResponse.status_code, expenseResponse.text)
    if budgetResponse.status_code == 200:
        budgetJson = budgetResponse.json()  # Convert JSON response to Python dictionary
        print("Budget Data:", budgetJson)
    else:
        print("Budget Error:", budgetResponse.status_code, budgetResponse.text)
    print(question)
    print(expenseJson)
    print(budgetJson)
    # Define the payload (your input prompt)
    payload = {
        "model": "llama3.2:latest",
        "messages": [
            {"role": "user",
             "content":
             format_expense_data(expenseJson) + format_budget_data(budgetJson) + " : This is the database string , from which you have to analyse and answer. "
             + " Be precision with the numericals and say only 1 line of answer. no other answers are allowed. If there is nothing, return 0. "
             + question + ".This is the question from the user , which you need to answer by analysing the table and in user understandable format, don't reveal any technical things, just say answer in numbers. Dont' say too much, just say accurate answers in numbers."
            }
        ]
    }
    # Send the HTTP POST request with streaming enabled
    response = requests.post(url, json=payload, stream=False)
    ret = ""
    # Check the response status
    if response.status_code == 200:
        print("Streaming response from Ollama:")
        for line in response.iter_lines(decode_unicode=True):
            if line:  # Ignore empty lines
                try:
                    # Parse each line as a JSON object
                    json_data = json.loads(line)
                    # Extract and print the assistant's message content
                    if "message" in json_data and "content" in json_data["message"]:
                        print(json_data["message"]["content"], end="")
                        ret += json_data["message"]["content"]
                except json.JSONDecodeError:
                    print(f"\nFailed to parse line: {line}")
        print()  # Ensure the final output ends with a newline
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

    return ret



st.set_page_config(page_title="Q&A Demo")

st.header("Ollama LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")
check_blockchain = st.button("Check block chain")

if submit and input:
    response = get_ollama_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    st.write(response)

if check_blockchain:
    if main.my_chain.verify_chain():
        st.success("Block chain is verified successfully, no errors found")
    else:
        st.error("Block chain fails, as there is some transaction issues found")