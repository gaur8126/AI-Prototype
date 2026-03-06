# Chiacon AI Webpage Prototype – AI Use Case Generator

[Live Demo](https://ai-prototype-0vxc.onrender.com/)

## Overview

This project is a simple AI-powered webpage prototype built for the Chiacon AI Webpage Assignment.

The webpage demonstrates how Artificial Intelligence can help businesses identify potential AI opportunities from real business problems.

Users can enter a business challenge, and the system generates:

* A short problem summary
* 2–3 AI opportunities
* Expected business impact

The goal of the project is to showcase a working AI capability in a clean and simple webpage.



## Demo Feature

### AI Use Case Generator

User enters a business problem such as:

> "Retail company struggling with inventory forecasting"

The AI analyzes the problem and returns:

**Problem Summary**

A concise explanation of the issue.

**AI Opportunities**

2–3 practical ways AI can help address the problem.

**Expected Business Impact**

Potential benefits such as efficiency improvement, cost reduction, or better decision-making.


## Tech Stack

Frontend

* HTML
* CSS
* JavaScript

Backend

* Python
* Flask

AI Integration

* LangChain
* Groq API



## Project Structure

```
chiacon-ai-prototype
│
├── app.py
├── requirements.txt
├── .env
│
├── templates
│   └── index.html
│
├── static
│   ├── style.css
│   └── script.js
│
└── README.md
```



## How It Works

<img src="Screenshot 2026-03-06 222731.png"><img>

1. The user enters a business problem in the web interface.
2. The frontend sends the request to the Flask backend.
3. The backend uses LangChain to construct a prompt.
4. The prompt is sent to the GROQ API.
5. Groq generates structured AI insights.
6. The response is returned and displayed on the webpage.

## Running the Project Locally

### 1. Clone the Repository

```
git clone https://github.com/gaur8126/chiacon-ai-prototype.git
cd chiacon-ai-prototype
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Add GROQ API Key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

### 4. Run the Application

```
python app.py
```

Then open:

```
http://127.0.0.1:5000
```


