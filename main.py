import pandas as pd

#lista de perguntas
questions = [
    ["Qual é o antônimo da palavra 'HAPPY' em inglês?", "SAD", "ANGRY", "EXCITED", "TIRED", 1],
    ["Qual é a forma correta da terceira pessoa do singular do verbo 'TO GO' (ir) no tempo presente?", "GOE", "GOES", "GO", "GOING", 2],
    ["Qual é o significado da palavra 'CAT' em português?", "PEIXE", "PÁSSARO", "CACHORRO", "GATO", 4],
    ["Qual é a tradução correta da expressão 'HOW ARE YOU'? para o português?", "Como você se chama?", " Onde você mora?", "O que você está fazendo?", "Como você está?", 4],
    ["Qual é o pronome pessoal correto para preencher a lacuna na frase: '______ IS A TEACHER'.", "HE", "SHE", "IT", "THEY", 2],
    ["Qual é a forma correta do comparativo da palavra 'GOOD' (bom) em inglês??", "BETTER", "GOODER", "BEST", "GOODEST", 1],
    ["Qual é o tempo verbal correto para preencher a lacuna na frase: 'I _______ DINNER WHEN THE PHONE.' ", "AM EATING", "ATE", "EAT", "WILL EAT", 1],
    ["Quem foi o primeiro presidente dos Estados Unidos?", "George Washington", "Abraham Lincoln", "Thomas Jefferson", "John F. Kennedy", 1],
    ["Qual é o plural correto da palavra 'CHILD' (criança) em inglês?", "CHILDRENS", "CHILDS", "CHILDREN", "CHILDES", 3],
    ["Qual é a palavra em inglês que corresponde ao número 100?", "TEN", "TWENTY", "ONE HUNDRED", "ONE THOUSAND", 3],
    ["Qual é o termo correto para preencher a lacuna na frase: 'I HAVE _______ APPLES IN THE FRIDGE.'", "A FEW", "AN", "ANY", " SOME", 4],
    ["Qual é o termo correto para a seguinte definição: 'A habilidade de se expressar fluentemente em dois idiomas'?", "Multilingualism", "Bilingualism", "Polyglotism", "Code-switching", 2],
    ["Qual é o antônimo da palavra 'BIG' em inglês?", "SMALL", "TALL", "HUGE", "GIANT", 1],
    ["Qual é o significado da palavra 'PREJUDICE' em inglês?", "PREJUÍZO", "PREOCUPAÇÃO", "PRECONCEITO", "PRIVACIDADE", 3],
    ["Qual é a tradução correta da palavra 'BOOK' em português?", "LIVRO", "CADERNO", "CANETA", "BOLSA", 1],
    ["Qual é a forma correta do passado simples do verbo 'TO SWIM' (nadar) em inglês?", "SWIM", "SWAM", "SWIMMING", "SWUM", 2],
    ["Qual é a forma correta do comparativo da palavra 'INTERESTING' (interessante) em inglês?", "Most interesting", "Interestinger", "Interestingest", "More interesting", 4],
    ["Qual é a forma correta do passado simples do verbo 'TO RUN' (correr) em inglês?", "RUN", "RAN", "RUNNING", "RUNNED", 2],
    ["Qual é o passado simples correto do verbo “SING”?", "SINGED", "SUNG", "SINGD", "SANG", 2],
    ["Qual é o significado da palavra “SELDOM”?", "SEMPRE", "ÁS VEZES", "RARAMENTE", "NUCA", 3],
    ["Qual é o tempo verbal correto para a frase “I ___ to the store yesterday”", "WENT", "GO", "GOES", "HAVE GONE", 1]
]
#criar dataframe do pandas
df = pd.DataFrame(questions, columns=["perguntas", 'Opção 1', 'Opção 2', 'Opção 3', 'Opção 4', "Respostas" ])

#Salvar no Excel
df.to_excel("questions.xlsx", index=False)

print("perguntas ensiridas com sucesso")
