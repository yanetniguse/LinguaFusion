### 🌐 **LinguaFusion: AI-Powered Interactive Language Learning Platform**  
🔗 **Live Demo:** [https://lingua-jade.vercel.app/](https://lingua-jade.vercel.app/)  
📊 **ML Model Training (Google Colab):** [View Notebook](https://colab.research.google.com/drive/1iVlxhtUhVCNgru1botaAjpqWTdJ7kvYy?usp=sharing)

**LinguaFusion** is an innovative web-based platform that revolutionizes language learning by combining **AI-powered translation** (English to Amharic) with **interactive multilingual lessons** in English, Amharic, Spanish, and French.  

With features like a built-in **AI chatbot** for real-time conversation, structured lessons, and dynamic quizzes, LinguaFusion empowers users to learn languages in an engaging, effective, and personalized way.

---

## 🚀 **Project Overview**  

### **🎯 Objective:**  
Build a **scalable, user-friendly** language-learning platform with:  

✅ **📚 Structured Lessons:** Vocabulary, grammar, and sentence-building exercises.  
✅ **🤖 AI Chatbot:** Real-time conversation practice with instant feedback.  
✅ **📝 Quizzes & Assessments:** Track progress with interactive tests.  
✅ **🔄 Translation Tool:** Seamless English-to-Amharic translation for better learning.  

---

## ✨ **Key Features**  

✔ **📖 Interactive Lessons** – Learn through engaging modules covering grammar and vocabulary.  
✔ **🗣️ Chatbot Integration** – Practice real-time conversations and receive instant AI feedback.  
✔ **📊 Quizzes & Assessments** – Reinforce learning with tests that offer **real-time scoring**.  
✔ **🔤 Translation Tool** – AI-powered translations enhance language comprehension.  
✔ **📱 Responsive UI** – Optimized for both desktop and mobile use.  
✅ **🧠 ML Model Training** – [Colab Notebook](https://colab.research.google.com/drive/1iVlxhtUhVCNgru1botaAjpqWTdJ7kvYy?usp=sharing) for AI pipeline.

---

## 🔧 **Technologies Used**  

### **💻 Front-end:**  
- **HTML, CSS, JavaScript** – Creating a responsive and dynamic user interface.  

### **🖥️ Back-end:**  
- **Python (Flask)** – Handling server requests and API interactions.  

### **🤖 Machine Learning & NLP:**  
- **Hugging Face Transformers** – Powering the AI translation model.  
- **SentencePiece & MarianMT** – Enabling effective Amharic-English translations.  

### **📂 Data Storage:**  
- **JSON & Databases** – Managing vocabulary and user progress.  

---

## 🏗️ **Development Steps**  

1️⃣ **Requirement Analysis** – Defined functional and non-functional needs based on user insights.  
2️⃣ **System Design** – Created UML diagrams (use case, sequence) for system architecture.  
3️⃣ **Implementation:**  
   - Developed vocabulary modules using **flashcards & interactive content**.  
   - Integrated **AI chatbot** for real-time language practice.  
4️⃣ **Testing & Optimization** – Ensured **functionality, performance, and usability**.  

---

## 🛡️ **Non-Functional Requirements**  

✔ **🖥️ Usability:** Intuitive, user-friendly interface.  
✔ **⚡ Performance:** Fast response times and smooth interactions.  
✔ **🔒 Security:** Data protection and vulnerability defenses.  
✔ **📈 Scalability:** Supports a growing user base and multiple languages.  

---

## 📊 **Project Screenshots**  
![image](https://github.com/user-attachments/assets/c2d6b520-e1aa-439a-9cb8-22b4024ee374)
![image](https://github.com/user-attachments/assets/fe377232-3775-4952-af4c-07d1aecfdaa6)
![image](https://github.com/user-attachments/assets/6abdf5ba-9284-4ef4-8bc6-74878f6a322d)
![image](https://github.com/user-attachments/assets/c162d748-bdb6-4299-9f84-b610dc747304)
![image](https://github.com/user-attachments/assets/95266e75-9afe-40bc-87b9-e4fe76a9b3dd)
![image](https://github.com/user-attachments/assets/d26d14e1-9845-46e2-8cb4-3c6ee9ad8f86)
![image](https://github.com/user-attachments/assets/b1ca2e50-a369-47aa-a2b2-e79ca90a9f4f)


---

## 🛠️ **Installation & Setup**  

### **🔹 Clone the Repository:**  
```bash
git clone https://github.com/yanetniguse/linguafusion.git
cd linguafusion
```

### **🔹 Set Up the Environment:**  
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### **🔹 Run the App:**  
```bash
python app.py
```

---

## 📊 **Challenges & Solutions**

### 🔴 **Key Challenges:**  
🚧 **Limited Dataset** – Only 2,500 sentence pairs initially available.  
🚧 **Tokenization Mismatch** – Misalignment between English-Amharic vocabularies.  
🚧 **Memory Constraints** – Out-of-memory (OOM) issues during model training.  
🚧 **Complex Amharic Grammar** – Struggles with fluency and sentence structure.  
🚧 **Overfitting & Hyperparameter Tuning** – Difficulty in generalizing across contexts.

### ✅ **Solutions & Improvements:**  
✔ **Expanded Dataset** – Curated a larger and more diverse set of sentence pairs.  
✔ **Pre-Trained Models** – Used `Helsinki-NLP/opus-mt-en-mul` as a strong foundation.  
✔ **Optimized Training** – Adjusted batch sizes and used gradient accumulation to avoid OOM.  
✔ **Hybrid AI Approach** – Combined ML with rule-based logic to improve grammar accuracy.

---

## 🚀 **Future Enhancements**

🔹 **🌎 Multi-Language Support** – Include more languages and dialects.  
🔹 **🎙️ Speech Recognition** – Voice input and pronunciation feedback.  
🔹 **🧠 Smarter AI Chatbot** – Real-world conversation handling via enhanced NLP.  
🔹 **📈 Adaptive Learning** – Personalize content based on individual progress and behavior.

---
📬 Contact & Support
For questions, suggestions, or collaboration opportunities, reach out:

📩 **LinkedIn:** [Yanet Niguse](https://www.linkedin.com/in/yanetniguse7)  
🌍 **Portfolio:** [yanet-niguse-tesfay.vercel.app](https://yanet-niguse-tesfay.vercel.app/)

### **❤️ Acknowledgements**  

We sincerely appreciate the contributions and support that made **LinguaFusion** possible.  

🔹 **[Professor Edward Ombui, Ph.D.](https://www.linkedin.com/in/edward-ombui/)** – For his invaluable mentorship in AI and NLP.  
🔹 **[Professor Fredrick Ogore](https://www.linkedin.com/in/fredrick-ogore-61435620/)** – For his guidance in system design and development.  
🔹 **Fyori** – For their collaboration in developing the **translation ML model**, contributing significantly to the AI-driven capabilities of LinguaFusion.  
🔹 **The Open-Source Community** – For providing the tools, resources, and inspiration that fueled this project.  

Your support and expertise have been instrumental in shaping **LinguaFusion** into an impactful and innovative platform. 🚀
