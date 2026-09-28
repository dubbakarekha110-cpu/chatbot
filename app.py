
"""import ollama
print("🤖MY AI Q&A Bot")
print("Type 'exit' to stop.\n")

while True:
    question=input("you:")
    if question.lower()=="exit":
        print("Bot: Goodbye!👋")
        break
    else:     
        response=ollama.chat(
            model="llama3.2",
            messages=[
           {
            "role":"user",
            "content":question
           }
    ]
)
print("AI:",response["message"]["content"])

"""






import ollama
print("🤖MY AI Q&A Bot")
print("Type 'exit' to stop.\n")

while True:
    question=input("you:")
    if question.upper()=="EXIT":
        print("Bot: Goodbye!👋")
        break
    else:     
        response=ollama.chat(
            model="llama3.2",
            messages=[
           {
            "role":"user",
            "content":question
           }
    ]
)
print("AI:",response["message"]["content"])
