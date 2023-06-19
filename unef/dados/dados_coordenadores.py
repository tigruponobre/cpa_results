import pandas as pd
def detalhe_perguntas(dtframe):
    p1_insuficiente = retornap1_insuficiente(dtframe)
    p1_regular = retornap1_regular(dtframe)
    p1_bom = retornap1_bom(dtframe)
    p1_otimo = retornap1_otimo(dtframe)
    p1_excelente = retornap1_excelente(dtframe)
    p2_insuficiente = retornap2_insuficiente(dtframe)
    p2_regular = retornap2_regular(dtframe)
    p2_bom = retornap2_bom(dtframe)
    p2_otimo = retornap2_otimo(dtframe)
    p2_excelente = retornap2_excelente(dtframe)
    p3_insuficiente = retornap3_insuficiente(dtframe)
    p3_regular = retornap3_regular(dtframe)
    p3_bom = retornap3_bom(dtframe)
    p3_otimo = retornap3_otimo(dtframe)
    p3_excelente = retornap3_excelente(dtframe)
    p4_insuficiente = retornap4_insuficiente(dtframe)
    p4_regular = retornap4_regular(dtframe)
    p4_bom = retornap4_bom(dtframe)
    p4_otimo = retornap4_otimo(dtframe)
    p4_excelente = retornap4_excelente(dtframe)
    p5_insuficiente = retornap5_insuficiente(dtframe)
    p5_regular = retornap5_regular(dtframe)
    p5_bom = retornap5_bom(dtframe)
    p5_otimo = retornap5_otimo(dtframe)
    p5_excelente = retornap5_excelente(dtframe)
    newframe = [
    {'Pergunta': '1',
     'Avaliação': '5 - Excelente',
     'Respostas': p1_excelente},
     {'Pergunta': '1',
     'Avaliação': '4 - Ótimo',
     'Respostas': p1_otimo},
     {'Pergunta': '1',
     'Avaliação': '3 - Bom',
     'Respostas': p1_bom},
     {'Pergunta': '1',
     'Avaliação': '2 - Regular',
     'Respostas': p1_regular},
     {'Pergunta': '1',
     'Avaliação': '1 - Insuficiente',
     'Respostas': p1_insuficiente},
     {'Pergunta': '2',
     'Avaliação': '5 - Excelente',
     'Respostas': p2_excelente},
     {'Pergunta': '2',
     'Avaliação': '4 - Ótimo',
     'Respostas': p2_otimo},
     {'Pergunta': '2',
     'Avaliação': '3 - Bom',
     'Respostas': p2_bom},
     {'Pergunta': '2',
     'Avaliação': '2 - Regular',
     'Respostas': p2_regular},
     {'Pergunta': '2',
     'Avaliação': '1 - Insuficiente',
     'Respostas': p2_insuficiente},
     {'Pergunta': '3',
     'Avaliação': '5 - Excelente',
     'Respostas': p3_excelente},
     {'Pergunta': '3',
     'Avaliação': '4 - Ótimo',
     'Respostas': p3_otimo},
     {'Pergunta': '3',
     'Avaliação': '3 - Bom',
     'Respostas': p3_bom},
     {'Pergunta': '3',
     'Avaliação': '2 - Regular',
     'Respostas': p3_regular},
     {'Pergunta': '3',
     'Avaliação': '1 - Insuficiente',
     'Respostas': p3_insuficiente},
     {'Pergunta': '4',
     'Avaliação': '5 - Excelente',
     'Respostas': p4_excelente},
     {'Pergunta': '4',
     'Avaliação': '4 - Ótimo',
     'Respostas': p4_otimo},
     {'Pergunta': '4',
     'Avaliação': '3 - Bom',
     'Respostas': p4_bom},
     {'Pergunta': '4',
     'Avaliação': '2 - Regular',
     'Respostas': p4_regular},
     {'Pergunta': '4',
     'Avaliação': '1 - Insuficiente',
     'Respostas': p4_insuficiente},
     {'Pergunta': '5',
     'Avaliação': '5 - Excelente',
     'Respostas': p5_excelente},
     {'Pergunta': '5',
     'Avaliação': '4 - Ótimo',
     'Respostas': p5_otimo},
     {'Pergunta': '5',
     'Avaliação': '3 - Bom',
     'Respostas': p5_bom},
     {'Pergunta': '5',
     'Avaliação': '2 - Regular',
     'Respostas': p5_regular},
     {'Pergunta': '5',
     'Avaliação': '1 - Insuficiente',
     'Respostas': p5_insuficiente},
    ]
    df = pd.DataFrame(newframe)
    # df_semzeros = df[df['Respostas'] > "0.00"]
    return df

# CÁLCULO PERGUNTA 1
def retorna_total_p1(frame):
    p1 = pd.DataFrame(frame)
    total_p1 = int(p1["INSUFICIENTE"].sum() + p1["REGULAR"].sum() + p1["BOM"].sum() + p1["ÓTIMO"].sum() + p1["EXCELENTE"].sum())
    return total_p1

def retornap1_excelente(frame):
    data = pd.DataFrame(frame)
    p1 = data.query("idpergunta == 1")
    total_p1 = retorna_total_p1(p1)
    total_excelente = int(p1["EXCELENTE"].sum())
    percent = ((total_excelente * 100) / total_p1)
    return percent
 
def retornap1_otimo(frame):
    data = pd.DataFrame(frame)
    p1 = data.query("idpergunta == 1")
    total_p1 = retorna_total_p1(p1)
    total_otimo = int(p1["ÓTIMO"].sum())
    percent = ((total_otimo * 100) / total_p1)
    return percent

def retornap1_bom(frame):
    data = pd.DataFrame(frame)
    p1 = data.query("idpergunta == 1")
    total_p1 = retorna_total_p1(p1)
    total_bom = int(p1["BOM"].sum())
    percent = ((total_bom * 100) / total_p1)
    return percent

def retornap1_regular(frame):
    data = pd.DataFrame(frame)
    p1 = data.query("idpergunta == 1")
    total_p1 = retorna_total_p1(p1)
    total_regular = int(p1["REGULAR"].sum())
    percent = ((total_regular * 100) / total_p1)
    return percent

def retornap1_insuficiente(frame):
    data = pd.DataFrame(frame)
    p1 = data.query("idpergunta == 1")
    total_p1 = retorna_total_p1(p1)
    total_insuficiente = int(p1["INSUFICIENTE"].sum())
    percent = ((total_insuficiente * 100) / total_p1)
    return percent

# CÁLCULO PERGUNTA 2
def retorna_total_p2(frame):
    p2 = pd.DataFrame(frame)
    total_p2 = int(p2["INSUFICIENTE"].sum() + p2["REGULAR"].sum() + p2["BOM"].sum() + p2["ÓTIMO"].sum() + p2["EXCELENTE"].sum())
    return total_p2

def retornap2_excelente(frame):
    data = pd.DataFrame(frame)
    p2 = data.query("idpergunta == 2")
    total_p2 = retorna_total_p2(p2)
    total_excelente = int(p2["EXCELENTE"].sum())
    percent = ((total_excelente * 100) / total_p2)
    return percent
 
def retornap2_otimo(frame):
    data = pd.DataFrame(frame)
    p2 = data.query("idpergunta == 2")
    total_p2 = retorna_total_p2(p2)
    total_otimo = int(p2["ÓTIMO"].sum())
    percent = ((total_otimo * 100) / total_p2)
    return percent

def retornap2_bom(frame):
    data = pd.DataFrame(frame)
    p2 = data.query("idpergunta == 2")
    total_p2 = retorna_total_p2(p2)
    total_bom = int(p2["BOM"].sum())
    percent = ((total_bom * 100) / total_p2)
    return percent

def retornap2_regular(frame):
    data = pd.DataFrame(frame)
    p2 = data.query("idpergunta == 2")
    total_p2 = retorna_total_p2(p2)
    total_regular = int(p2["REGULAR"].sum())
    percent = ((total_regular * 100) / total_p2)
    return percent

def retornap2_insuficiente(frame):
    data = pd.DataFrame(frame)
    p2 = data.query("idpergunta == 2")
    total_p2 = retorna_total_p2(p2)
    total_insuficiente = int(p2["INSUFICIENTE"].sum())
    percent = ((total_insuficiente * 100) / total_p2)
    return percent

#CÁLCULO PERGUNTA 3
def retorna_total_p3(frame):
    p3 = pd.DataFrame(frame)
    total_p3 = int(p3["INSUFICIENTE"].sum() + p3["REGULAR"].sum() + p3["BOM"].sum() + p3["ÓTIMO"].sum() + p3["EXCELENTE"].sum())
    return total_p3

def retornap3_excelente(frame):
    data = pd.DataFrame(frame)
    p3 = data.query("idpergunta == 3")
    total_p3 = retorna_total_p3(p3)
    total_excelente = int(p3["EXCELENTE"].sum())
    percent = ((total_excelente * 100) / total_p3)
    return percent
 
def retornap3_otimo(frame):
    data = pd.DataFrame(frame)
    p3 = data.query("idpergunta == 3")
    total_p3 = retorna_total_p3(p3)
    total_otimo = int(p3["ÓTIMO"].sum())
    percent = ((total_otimo * 100) / total_p3)
    return percent

def retornap3_bom(frame):
    data = pd.DataFrame(frame)
    p3 = data.query("idpergunta == 3")
    total_p3 = retorna_total_p3(p3)
    total_bom = int(p3["BOM"].sum())
    percent = ((total_bom * 100) / total_p3)
    return percent

def retornap3_regular(frame):
    data = pd.DataFrame(frame)
    p3 = data.query("idpergunta == 3")
    total_p3 = retorna_total_p3(p3)
    total_regular = int(p3["REGULAR"].sum())
    percent = ((total_regular * 100) / total_p3)
    return percent

def retornap3_insuficiente(frame):
    data = pd.DataFrame(frame)
    p3 = data.query("idpergunta == 3")
    total_p3 = retorna_total_p3(p3)
    total_insuficiente = int(p3["INSUFICIENTE"].sum())
    percent = ((total_insuficiente * 100) / total_p3)
    return percent

#CÁLCULO PERGUNTA 4
def retorna_total_p4(frame):
    p4 = pd.DataFrame(frame)
    total_p4 = int(p4["INSUFICIENTE"].sum() + p4["REGULAR"].sum() + p4["BOM"].sum() + p4["ÓTIMO"].sum() + p4["EXCELENTE"].sum())
    return total_p4

def retornap4_excelente(frame):
    data = pd.DataFrame(frame)
    p4 = data.query("idpergunta == 4")
    total_p4 = retorna_total_p4(p4)
    total_excelente = int(p4["EXCELENTE"].sum())
    percent = ((total_excelente * 100) / total_p4)
    return percent
 
def retornap4_otimo(frame):
    data = pd.DataFrame(frame)
    p4 = data.query("idpergunta == 4")
    total_p4 = retorna_total_p4(p4)
    total_otimo = int(p4["ÓTIMO"].sum())
    percent = ((total_otimo * 100) / total_p4)
    return percent

def retornap4_bom(frame):
    data = pd.DataFrame(frame)
    p4 = data.query("idpergunta == 4")
    total_p4 = retorna_total_p4(p4)
    total_bom = int(p4["BOM"].sum())
    percent = ((total_bom * 100) / total_p4)
    return percent

def retornap4_regular(frame):
    data = pd.DataFrame(frame)
    p4 = data.query("idpergunta == 4")
    total_p4 = retorna_total_p4(p4)
    total_regular = int(p4["REGULAR"].sum())
    percent = ((total_regular * 100) / total_p4)
    return percent

def retornap4_insuficiente(frame):
    data = pd.DataFrame(frame)
    p4 = data.query("idpergunta == 4")
    total_p4 = retorna_total_p4(p4)
    total_insuficiente = int(p4["INSUFICIENTE"].sum())
    percent = ((total_insuficiente * 100) / total_p4)
    return percent

#CÁLCULO PERGUNTA 5
def retorna_total_p5(frame):
    p5 = pd.DataFrame(frame)
    total_p5 = int(p5["INSUFICIENTE"].sum() + p5["REGULAR"].sum() + p5["BOM"].sum() + p5["ÓTIMO"].sum() + p5["EXCELENTE"].sum())
    return total_p5

def retornap5_excelente(frame):
    data = pd.DataFrame(frame)
    p5 = data.query("idpergunta == 5")
    total_p5 = retorna_total_p5(p5)
    total_excelente = int(p5["EXCELENTE"].sum())
    percent = ((total_excelente * 100) / total_p5)
    return percent
 
def retornap5_otimo(frame):
    data = pd.DataFrame(frame)
    p5 = data.query("idpergunta == 5")
    total_p5 = retorna_total_p5(p5)
    total_otimo = int(p5["ÓTIMO"].sum())
    percent = ((total_otimo * 100) / total_p5)
    return percent

def retornap5_bom(frame):
    data = pd.DataFrame(frame)
    p5 = data.query("idpergunta == 5")
    total_p5 = retorna_total_p5(p5)
    total_bom = int(p5["BOM"].sum())
    percent = ((total_bom * 100) / total_p5)
    return percent

def retornap5_regular(frame):
    data = pd.DataFrame(frame)
    p5 = data.query("idpergunta == 5")
    total_p5 = retorna_total_p5(p5)
    total_regular = int(p5["REGULAR"].sum())
    percent = ((total_regular * 100) / total_p5)
    return percent

def retornap5_insuficiente(frame):
    data = pd.DataFrame(frame)
    p5 = data.query("idpergunta == 5")
    total_p5 = retorna_total_p5(p5)
    total_insuficiente = int(p5["INSUFICIENTE"].sum())
    percent = ((total_insuficiente * 100) / total_p5)
    return percent