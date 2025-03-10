# Sentiment and Query Intent Analysis Library

## Overview
This library provides tools for **sentiment analysis** and **query intent detection** using a fine-tuned **BERT-based model** to improve the emotional intelligence of your chatbot. The library enables sentiment classification at both **sentence** and **document** levels, as well as intent categorization most suited for educational chatbot conversations.

## Features
✅ **Sentence-Level Sentiment Analysis** - Classifies individual sentences as **Positive, Neutral, or Negative**.<br>
✅ **Document-Level Sentiment Analysis** - Aggregates multiple sentences and determines the **overall sentiment**.<br>
✅ **Query Intent Detection** - Identifies the **intent behind a query**, such as course information, class schedule, greetings.<br>
✅ **Chat Summary Generation** - Provides a summary table and insights into chat sentiment and intent distribution.<br>
✅ **Conversation Conversion & Analysis** - Converts chat logs initially in a json format into a csv format structured data with **sentiment, intent, and response time analysis** to be used to generate a dynamic dashboard on a website link: https://chatbot-dashboard-analysis.streamlit.app/ 
Keys needed in the chat log: _id ,Person ,stime_text ,stime_timestamp ,last_interact_text ,last_interact_timestamp ,llm_deployment_name ,llm_model_name ,vectorstore_index ,overall_cost ,overall_tokens ,role ,content ,recorded_on_text ,recorded_on_timestamp ,token_cost,tokens ,user_sentiment ,query_intent ,conversation_id ,previous_query_intent ,overall_chat ,chat_sentiment ,chatbot_response_time ,overall_conversation_time


---

## Installation
Ensure you have the necessary dependencies installed:
```bash
pip install torch transformers pandas tabulate
```

---

## Usage
### 1️⃣ **Sentence-Level Sentiment Analysis**
Determine sentiment (**Positive, Neutral, Negative**) for a given sentence. This can return the sentiment of the user.
```python
from chatbot_analysis import sentiment_sentence

sentence = "I love this course!"
sentiment = sentiment_sentence(sentence)
print(sentiment)  # Output: Positive
```

### 2️⃣ **Document-Level Sentiment Analysis**
Analyze sentiment for a **collection of sentences** or a document. This gives back the sentiment at class level. The input should be in a dictionary format where the keys are the sentence number and values are the content
```python
from chatbot_analysis import sentiment_document

document = {"sentence1": "The class was great!", "sentence2": "I learned a lot."}
doc_sentiment = sentiment_document(document)
print(doc_sentiment)  # Output: Positive
```

### 3️⃣ **Query Intent Detection**
Classify the **intent behind a query** ("Course Overview and Information", "Course Assessment" , "Checking Announcement", "Request for Permission", "Learning Course Content",
 "Class Schedule", "Greetings", "Ending", "Casual Chat" , "No Query")
```python
from chatbot_analysis import query_intent

query = "Can I get more details on the assessment criteria?"
intent = query_intent(query)
print(intent)  # Output: Course Assessment
```

### 4️⃣ **Generate Chat Sentiment & Intent Summary**
Summarize sentiment and intent **for multiple sentences**. Use chat_summary if you want query intent to be included.
```python
from chatbot_analysis import chat_summary
from chatbot_analysis import sentiment_summary

document = {
    "sentence1": "I love this class!",
    "sentence2": "When is the next assignment due?"
}
summary = chat_summary(document)
summary = sentiment_summary(document)
print(summary)
```

### 5️⃣ **Analyze and Convert Chat Logs**
Convert chatbot logs into structured data with **sentiment, intent, and response time analysis**.
```python
from chatbot_analysis import conversion

chatlog = [
    {
        "_id": {
            "$oid": "664a1234567890abcdef1234"
        },
        "Person": "9f8e7d6c5b4a3a2b1c0d9e8f7g6h5i4j",
        "stime": {
            "text": "2025-03-02 14:20:10",
            "timestamp": 1741009210.123456
        },
        "messages": [
            {
                "role": "user",
                "content": "What are the benefits of machine learning?",
                "recorded_on": {
                    "text": "2025-03-02 14:21:15",
                    "timestamp": 1741009275.987654
                }
            },
            {
                "role": "ai",
                "content": "Machine learning enables systems to learn patterns and make decisions without explicit programming. It improves automation, enhances decision-making, and drives predictive analytics in various industries such as healthcare, finance, and retail.",
                "recorded_on": {
                    "text": "2025-03-02 14:21:22",
                    "timestamp": 1741009282.543210
                },
                "token_cost": {
                    "cost": "0.00256780",
                    "tokens": 1850
                }
            },
            {
                "role": "user",
                "content": "Can you provide real-world applications?",
                "recorded_on": {
                    "text": "2025-03-02 14:21:50",
                    "timestamp": 1741009310.765432
                }
            },
            {
                "role": "ai",
                "content": "Certainly! Machine learning is used in fraud detection for banking, personalized recommendations in e-commerce, medical diagnosis in healthcare, and predictive maintenance in manufacturing, helping businesses optimize operations and enhance user experiences.",
                "recorded_on": {
                    "text": "2025-03-02 14:21:58",
                    "timestamp": 1741009318.321098
                },
                "token_cost": {
                    "cost": "0.00287650",
                    "tokens": 2050
                }
            }
        ],
        "user_query": "What are the benefits of machine learning?",
        "ai_response": "Machine learning enables systems to learn patterns and make decisions without explicit programming. It improves automation, enhances decision-making, and drives predictive analytics in various industries such as healthcare, finance, and retail.",
        "user_timestamp": 1741009275.987654,
        "user_time_text": "2025-03-02 14:21:15",
        "ai_timestamp": 1741009282.543210,
        "ai_time_text": "2025-03-02 14:21:22",
        "last_interact": {
            "text": "2025-03-02 14:21:58",
            "timestamp": 1741009318.321098
        },
        "llm_deployment_name": "ai-chatbot-ml-gpt4",
        "llm_model_name": "gpt-4-turbo",
        "vectorstore_index": "vector-ml-usecases-2025",
        "overall_cost": {
            "overall_cost": 0.00544430,
            "overall_tokens": 3900
        },
        "cost": "0.00256780",
        "tokens": 1850
    }
]


df = conversion(chatlog, num_of_chats=1)
print(df.head())
```

---

## Query Intent Categories
The `query_intent` function categorizes queries into the following:
| **Category** | **Description** |
|-------------|----------------|
| Course Overview and Information | General course-related inquiries |
| Course Assessment | Questions about exams, assignments |
| Checking Announcement | Checking for latest updates |
| Request for Permission | Asking for special permissions not available in the bector database|
| Learning Course Content | Questions about materials or topics |
| Class Schedule | Checking class timings |
| Greetings | Saying "hello" or "goodbye" |
| Ending | Ending a conversation |
| Casual Chat | Non-academic casual discussions |
| No Query | No identifiable query present |

---

## Sentiment Classification Categories
The library classifies sentiment into:
- **Positive** 😊
- **Neutral** 😐
- **Negative** 😡

---


## Author
Developed by Chalamalasetti Sree Vaishnavi

