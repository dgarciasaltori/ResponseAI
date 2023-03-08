from flask import Flask, request
import openai

app = Flask(__name__)

openai.api_key = "API-KEY"

def get_answer(question):
    prompt = (f"Q: {question}\nA:")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    answer = response.choices[0].text.strip()
    return answer

@app.route('/pergunta', methods=['POST'])
def pergunta():
    question = request.args.get('q')
    context_question = question + " e mais alguma informação relevante"
    answer = get_answer(context_question)
    return answer

if __name__ == '__main__':
    app.run()
