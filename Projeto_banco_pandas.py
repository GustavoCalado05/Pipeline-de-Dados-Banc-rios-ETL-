import pandas as pd

dados = [
    {"id": 1, "Nome": "Gustavo", "Saldo": 1500.00, "Score": 20},  
    {"id": 2, "Nome": "Maria", "Saldo": 250.50, "Score": 90},     
    {"id": 3, "Nome": "João", "Saldo": 5200.00, "Score": 40},
    {"id": 4, "Nome": "Pedro", "Saldo": 52000.00, "Score": -20}      
]

df = pd.DataFrame(dados)

print("🔎 Estado Atual: Dados brutos organizados em tabela.")
print(df)

def cerebro_do_marketing(Saldo_do_cliente):
    if Saldo_do_cliente <= 500:
        return "Crédito Pré-Aprovado"
    elif Saldo_do_cliente > 5000:
        return "Consultoria de Investimentos VIP"
    else:
        return "Seguro de Vida Familiar"
    
def Probabilidade_Pagamento(Score_do_cliente):
    if Score_do_cliente <= -1:
        return "Probabildade de pagamento extremamente baixa"
    elif Score_do_cliente <= 60:
        return "Probabildade de pagamento moderada"
    else:
        return "Probabildade de pagamento extremamente alta"

df['Status_Marketing'] = df['Saldo'].apply(cerebro_do_marketing)
print(df[['Nome', 'Status_Marketing']])

df['Probabilidade'] = df['Score'].apply(Probabilidade_Pagamento)
print(df[['Nome', 'Probabilidade']])

clientes_vip = df[df['Score']>= 50]
print(clientes_vip[['Nome', 'Probabilidade']])


df.to_csv("resultado_final.csv", index=False)
