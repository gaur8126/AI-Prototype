from flask import Flask, render_template, request, jsonify
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

from langchain_groq import ChatGroq

from langchain_openai import ChatOpenAI, OpenAI

load_dotenv()

# llm = ChatOpenAI(
#     model="openai/gpt-4o",
#     api_key=os.getenv("GITHUB_TOKEN"),
#     base_url="https://models.github.ai/inference",
#     temperature=1,
#     max_tokens=4096,
# )


# Initialize Groq LLM
llm = ChatGroq(
model_name="llama-3.3-70b-versatile",
groq_api_key = os.getenv("GROQ_API_KEY"),
temperature=0.9
)

# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )

prompt_template = PromptTemplate(
    input_variables=["problem"],
    template="""
You are an AI business consultant.

A company reports the following business problem:

{problem}

Analyze the problem and provide the output in this format.

Problem Summary:
Write a short explanation of the problem.

AI Opportunities:
List 2-3 ways Artificial Intelligence can help solve the problem.

Expected Business Impact:
Explain the benefits such as efficiency, cost reduction, better decisions,
or revenue growth.

Keep the answer concise and structured.
"""
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate-usecase", methods=["POST"])
def generate_usecase():

    data = request.json
    problem = data["problem"]

    prompt = prompt_template.format(problem=problem)

    response = llm.invoke(prompt)

    return jsonify({
        "result": response.content
    })


if __name__ == "__main__":
    app.run(debug=True)
