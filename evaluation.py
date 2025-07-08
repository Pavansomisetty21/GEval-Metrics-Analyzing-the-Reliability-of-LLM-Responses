from litellm import completion
import os
from opik.evaluation.metrics import GEval
from opik import track

# Set API key (make sure this is valid)

#here enter your keys
os.environ['GROQ_API_KEY'] = 
os.environ['OPENAI_API_KEY']=
# System prompt must be defined first
SYSTEM_PROMPT = "Generate a concise summarization of the article you are provided with by the user."

# Prepare user message
content = "What is an LLM?"

# Call the model
response = completion(
    model="groq/llama3-8b-8192",
    
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": content}
    ]
)

# Extract model output
output = response.choices[0].message.content
print("Model Output:\n", output)

# Setup GEval
TASK_INTRODUCTION = "You are an expert judge tasked with evaluating the faithfulness of an AI-generated answer to the given context."
EVALUATION_CRITERIA = "In the provided text, the OUTPUT must not introduce new information beyond what's provided in the CONTEXT."

g_eval_general = GEval(
    task_introduction=TASK_INTRODUCTION,
    evaluation_criteria=EVALUATION_CRITERIA,
    name="g_eval_general"
)


# Score the result (use f-string to correctly insert variables)
result = g_eval_general.score(
    output=f"OUTPUT: {output}\nCONTEXT: {content}"
)

# Print the score/result
print("\nGEval Score Result:\n", result)
