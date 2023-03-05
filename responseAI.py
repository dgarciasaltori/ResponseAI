import openai
from halo import Halo

openai.api_key = "API-KEY"

print("##################################################################################")
print("#                       Code by: Diego Garcia Saltori                            #")
print("#                       UTF-8                                                    #")
print("#                       Lang: PT-BR                                              #")
print("#                       Version: 1.0                                             #")
print("##################################################################################")
print("#                     Estudo sobre Inteligencia Artifical                        #")
print("#                     Integrando a aplicação a API da OpenAI                     #")
print("##################################################################################")


def get_answer(question):
    prompt = (f"Q: {question}\nA:")
    with Halo(text='Gerando resposta', spinner='dots'):
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

while True:
    question = input("Faça sua pergunta (ou digite 'sair' para sair): ")
    if question.lower() == "sair":
        print("Até a próxima!")
        break
    context_question = question + " e mais alguma informação relevante"
    answer = get_answer(context_question)
    print("\033[94m" + answer + "\033[0m")