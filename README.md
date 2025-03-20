### **🌐 LinguaFusion: AI-Powered Interactive Language Learning Platform**  

LinguaFusion is an innovative web-based language-learning platform that combines **machine learning-driven translation** (English to Amharic) with **interactive lessons** (English, Amharic, Spanish, and French). It features a **built-in AI chatbot** for real-time conversation practice, structured learning modules, and progress-tracking quizzes. This project showcases the power of **AI, NLP, and interactive learning** to make language acquisition more engaging and effective.  

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
 **challenges**

Dataset Size: With only 2500 lines, the dataset was relatively small, limiting the model's ability to generalize effectively.

Tokenization Mismatch: Using SentencePieceProcessor caused a mismatch between tokenized and padded English and Amharic vocabularies. Padding resolved part of the issue.

Training from Scratch: Training the model from scratch was difficult, so the Helsinki-NLP/opus-mt-en-mul pre-trained model from Hugging Face was used as a foundation.

Training Errors: Training with custom tokenization led to errors, so the pre-trained Helsinki-NLP/opus-mt-en-mul tokenizer was adopte

Out of Memory (OOM) Issues: Memory limitations occurred during training, which were resolved by reducing the batch size and increasing gradient accumulation steps to optimize resource usage.

Amharic Complexity: Amharic's complex grammar and morphology presented challenges for accurate translations.

Overfitting and Underfitting: One of the main challenges was avoiding overfitting or underfitting the model. Striking the right balance in model complexity and the amount of training data was necessary to improve the generalization capability of the model.

Hyperparameter Tuning: Finding the best hyperparameters for the translation model was challenging and required multiple iterations to optimize the learning rate, batch size, and other parameters.

Sentence Length and Complexity: The model sometimes struggled with translating longer or more complex sentences accurately. Simple sentences worked well, but maintaining accuracy with more involved structures required additional training and adjustments.

***improvments***

Larger and More Diverse Dataset: To improve translation accuracy, incorporating a larger dataset with more varied topics, sentence structures, and vocabulary would be beneficial. This would help the model handle a wider range of text and improve its ability to translate complex or idiomatic sentences.

Advanced Models: Implementing more advanced and state-of-the-art models such as Transformer-based architectures (e.g., Transformer, GPT, BERT) could improve the quality of translations. These models have shown significant improvements in language understanding and translation tasks.

Real-Time Suggestions and Corrections: Adding a feature where the system provides real-time feedback or suggestions during the translation process can make it more interactive and engaging.

use Rule-based training can improve your model by fixing grammar issues, ensuring consistency, resolving ambiguities, and augmenting data. Combining it with neural models can refine translations, especially for complex languages like Amharic. However, it can be challenging to scale and maintain.

**conclusion**

 English-to-Amharic translation model, integrated with a website for easy access, successfully utilizes the Helsinki-NLP/opus-mt-en-mul pre-trained model. It addresses challenges like tokenization mismatches and memory constraints through optimizations such as reducing batch sizes and increasing gradient steps. While the model achieves a BLEU score of 38.05 with 2500 sentences, there is still room for improvement, particularly in handling complex Amharic grammar. The website's integration allows users to easily interact with the model for real-time translations. Future enhancements could focus on improving data quality, expanding the dataset, and integrating rule-based methods to refine accuracy and support additional languages, making the tool an even more powerful resource for language learning and cross-cultural communication.
### **🔹 Run the App:**  
```bash
python app.py
```

---

## 🤝 **Contributing**  
We welcome contributions from developers, AI researchers, and language educators! To contribute:  

1️⃣ **Fork** the repository.  
2️⃣ **Create a new branch** (feature/your-feature-name).  
3️⃣ **Make your changes and commit.**  
4️⃣ **Open a pull request for review.**  

---

## 🙌 **Future Enhancements**  

🚀 **Multi-Language Support:** Expand to additional languages with advanced ML models.  
🎙️ **Speech Recognition:** Enable **voice input** and text-to-speech for pronunciation training.  
🧠 **Smarter Chatbot:** Improve AI responses with **better NLP models** for deeper conversations.  

---

## 📬 **Contact & Support**  
For questions, suggestions, or collaboration opportunities, feel free to reach out:  

📩 **LinkedIn:** [Yanet Niguse](https://www.linkedin.com/in/yanetniguse7)  

---

## ❤️ **Acknowledgements**  
Special thanks to **Fyori** for their support, and to the **open-source community** for providing the tools that made LinguaFusion possible!  
