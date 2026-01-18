# 💰 Pipeline de Dados Bancários (ETL)

> Projeto prático de Engenharia de Dados desenvolvido para simular o processamento de campanhas de marketing e análise de crédito bancário.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Library-Pandas-green)
![Status](https://img.shields.io/badge/Status-Concluído-success)

## 📋 Sobre o Projeto

Este projeto consiste em um script Python que executa um processo completo de **ETL (Extract, Transform, Load)**. O objetivo é pegar dados brutos de clientes, aplicar regras de negócio para segmentação de marketing e análise de risco (Score), e exportar os resultados para tomada de decisão.

O projeto foi desenvolvido como parte de estudos práticos sobre Ciência de Dados e Python.

## ⚙️ Funcionalidades (O Pipeline)

O código segue as três etapas fundamentais da Engenharia de Dados:

### 1. 🔄 Extract (Extração)
- Simulação de uma base de dados JSON (Dados Mockados).
- Leitura e estruturação dos dados utilizando **Pandas DataFrame**.

### 2. 🧠 Transform (Transformação)
- **Engenharia de Atributos:** Criação de novas colunas baseadas em lógica condicional.
- **Segmentação de Marketing:**
  - Saldo < 500: Oferta de Crédito.
  - Saldo > 5000: Oferta de Investimentos.
- **Análise de Risco (Credit Score):**
  - Classificação da probabilidade de pagamento (Baixa, Moderada, Alta) baseada no Score do cliente.

### 3. 💾 Load (Carregamento) & Visualização
- Exportação dos dados tratados para um arquivo `resultado_final.csv`.
- Geração de gráficos de barras (`matplotlib`) para análise visual dos Scores dos clientes.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal.
- **Pandas**: Manipulação e análise de tabelas de dados.
- **Matplotlib**: Geração de gráficos para visualização de dados.
- **VS Code**: IDE utilizada para o desenvolvimento.

## 🚀 Como Executar

### Pré-requisitos
Você precisa ter o Python instalado. Em seguida, instale as bibliotecas necessárias via terminal:

```bash
pip install pandas matplotlib

### Resultado
id,Nome,Saldo,Score,Status_Marketing,Probabilidade
1,Gustavo,1500.0,20,Seguro de Vida Familiar,Probabildade de pagamento moderada
2,Maria,250.5,90,Crédito Pré-Aprovado,Probabildade de pagamento extremamente alta
3,João,5200.0,40,Consultoria de Investimentos VIP,Probabildade de pagamento moderada
4,Pedro,52000.0,-20,Consultoria de Investimentos VIP,Probabildade de pagamento extremamente baixa


