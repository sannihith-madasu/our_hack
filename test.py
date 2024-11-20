from flask import Flask, request, jsonify, render_template_string
import openai
import re

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "ksjd6xfgdflkf3jsdkh34f"

# Function to check if the input is related to travel expenses
def is_travel_related(user_input):
    travel_keywords = ["flight", "hotel", "budget", "cost", "expense", "travel", "trip", "accommodation", "transportation", "fuel", "visa"]
    return any(keyword.lower() in user_input.lower() for keyword in travel_keywords)

@app.route('/chat/<user_input>', methods=['GET'])
def chat(user_input):
    # Check if the input is related to travel expenses
    if not is_travel_related(user_input):
        return jsonify({'reply': "I'm only able to help with travel expense-related queries."}), 400

    try:
        # Make the request to the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[
                {"role": "system", "content": "You are a helpful assistant that only answers questions related to travel expenses."},
                {"role": "user", "content": user_input}
            ]
        )
        
        # Extract the assistant's reply
        assistant_reply = response['choices'][0]['message']['content']
        
        # Return the assistant's reply
        return render_template_string("<h1>Your reply: {{ assistant_reply }}</h1>", assistant_reply=assistant_reply)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
