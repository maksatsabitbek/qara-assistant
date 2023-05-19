from flask import Flask, render_template, request
from markupsafe import Markup
import openai
import markdown
import markdown.extensions.fenced_code
import markdown.extensions.codehilite

openai.api_key = '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'
app = Flask(__name__)
# messages = []
@app.route('/')
def home():

    return render_template('index.html')

@app.route('/get_response', methods=['POST'])

def get_bot_response():
    user_input = request.form['user_input']
    # print(user_input)
    # messages.append({'role': 'user', 'content': user_input})
    # print(messages[1])
    completion = openai.Completion.create(
        model = "text-davinci-003",
        prompt = f"act as message-fraud detector named GRANDHELPER. GRANDHELPER reads an input message, analyzes if it can deal any potential harm or harass the user. You as GRANDHELPER can take final decisions if message is fraud or not. Return Trust or Not trust and percentage in square brackets. GRANDHELPER adds the main issue with the messages to the brackets in one word as well. GRANDHELPER alerts the user about potential fraud. \"Unknown\".\n\nQ: {user_input}\nA:",
        temperature = 1,
        max_tokens = 10,
        top_p = 1,
        frequency_penalty = 0.0,
        presence_penalty = 0.5,
        stop = ["\n"]
    )
    ai_response = completion.choices[0].text
    # print(ai_response)
    messages.append({'role': 'assistant', 'content': ai_response})
    print(messages)
    return  Markup(markdown.markdown(ai_response, extensions=['fenced_code', 'codehilite']))
@app.route('/reset')
def reset():
    global messages
    messages = []
    return "Conversation history has been reset."
if __name__ == '__main__':
    app.run(port=5006)
