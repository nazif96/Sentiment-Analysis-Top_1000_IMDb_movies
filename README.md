# 💬 Projet de Classification de Sentiments

Ce projet a pour objectif de classifier des textes selon leur **sentiment** (positif, négatif ou neutre), en combinant des approches d’analyse de données, de machine learning, et de deep learning. Il se déroule en trois étapes principales :

---

## 🧭 Étapes du projet

### 1. 🔍 Analyse exploratoire des données (EDA)
- Nettoyage des textes (ponctuation, stop words, etc.)
- Visualisation des distributions de sentiments
- Analyse de fréquence des mots et nuages de mots (wordclouds)

### 2. 🤖 Modélisation Machine Learning
- Vectorisation des textes (TF-IDF, CountVectorizer)
- Entraînement de modèles classiques : Naive Bayes, SVM, régression logistique
- Évaluation des performances (accuracy, f1-score, matrice de confusion)

### 3. 🧠 Deep Learning + Interface Streamlit
- Entraînement d’un modèle LSTM avec Keras/TensorFlow
- Prétraitement des textes avec Tokenizer et padding
- Déploiement d’une interface **Streamlit** pour tester le modèle en temps réel

---

## 📁 Structure du projet

```.Sentiment-Analysis-Top_1000_IMDb_movies


├── data/                           # Jeux de données
│   └── Top_1000_IMDb_movies.csv                    
├── Notebooks/ 
|   ├── EDA.ipynb                   # Analyse exploratoire des données
|   ├── ML.ipynb                    # Machine Learning Notebook                       
│   └── DP.ipynb                    # Deep learning Notebook
|                  
├── sentiments_model.h5             # Modèles sauvegardés lstm_model.h5
│  
├── app.py                          # Interface Streamlit
|                        
├── label_encoder                   # 
|
├── tokenizer                       #
|
├── requirements.txt           # Dépendances Python
└── README.md                  # Présentation du projet

```
---

## 📦 Prérequis

1. **EDA et Machine Learning** 

Installez les packages nécessaires pour l’analyse et la modélisation machine learning :

```bash
pip install pandas numpy matplotlib seaborn scikit-learn nltk wordcloud

``` 

2. **pour le deep learning**  

- créez un autre environnement
- Selectionner pyhthon 3.10 
- pip    `pip install --upgrade pip`  

```bash 
pip install -r requirements.txt

```

## 🚀 Lancer l'application Streamlit
Assurez-vous d’avoir installé toutes les dépendances (incluant TensorFlow et Streamlit), puis lancez :

```bash
streamlit run app.py

```


## 🧪 Exemple d’utilisation

Ouvrir l’interface Streamlit

Entrer un texte comme :

"I am very satisfied with this service, everything was perfect !"

Cliquer sur Analyser

Le modèle prédit : ✅ Sentiment positif


## 🛠️ Fonctionnalités à venir
Intégration de modèles basés sur Transformers (ex. BERT)

Export des résultats en CSV

Personnalisation de l’interface Streamlit


## 🤝 Contribution

Les contributions sont les bienvenues !

N’hésitez pas à ouvrir une issue ou soumettre une pull request.

## 👨‍💻 Auteurs 

**AFOLABI Nazifou**

- **Datascientist | Machine Learning & Modeling** 
- Passionné par les sciences de données et l'intelligence artificielle.
- **Email** : [afolabinazif96@gmail.com](mailto.afolabinazif96@gmail.com)
- **LinkedIn** : [Nazifou AFOLABI](https://www.linkedin.com/in/nazifou-afolabi-10544729b/)