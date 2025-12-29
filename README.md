# 🫀 CardIAca

Sistema web de **predição de risco de doença cardíaca** utilizando **Inteligência Artificial**.

O projeto utiliza um modelo de Machine Learning treinado com o dataset **Heart Disease (UCI)** para estimar a probabilidade de risco com base em dados clínicos informados pelo usuário.

⚠️ **Atenção:** Este sistema **não substitui diagnóstico médico**. O resultado é apenas informativo.

---

## 🚀 Tecnologias Utilizadas

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML5
- CSS3

---

## 🧠 Modelo de IA

- Algoritmo: **Random Forest Classifier**
- Precisão aproximada: **87%**
- Dataset: Heart Disease UCI

O modelo realiza a normalização dos dados e retorna:
- Classificação de risco (alto ou baixo)
- Probabilidade estimada

---

## 📊 Funcionalidades

- Formulário interativo para entrada de dados clínicos
- Predição em tempo real
- Exibição visual do resultado
- Informações sobre fatores de risco
- Dicas de prevenção
- Avisos sobre limitações do modelo

---

## 🖥️ Como Executar o Projeto Localmente

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/juliofilho04/cardIAca.git
cd CardIAca

### 2️⃣ Crie e ative o ambiente virtual

python -m venv venv
venv\Scripts\activate

### 3️⃣ Instale as dependências

pip install -r requirements.txt

### 4️⃣ Execute a aplicação

python app.py

📁 Estrutura do Projeto

├── app.py
├── model.pkl
├── requirements.txt
├── static/
│   ├── images/
│   └── style.css
├── templates/
│   ├── index.html
│   └── informacoes.html
└── README.md

👨‍💻 Autor

Desenvolvido por Julio César
