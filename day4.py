import ollama
#Conversion memory
messages=[]

while True:
    user_input=input("You: ")
    
    #Stop Chatbot
    if user_input.lower()=="exit":
        break
    messages.append(
        {
            "role":"user",
            "content":user_input
        }
    )
    
    #send complete conversion history to Ollama
    response=ollama.chat(
        model="llama3.2",
        messages=messages
    )
    
    #Get AI response
    ai_message=response["message"]["content"]
    print("AI:", ai_message)
    messages.append(
        {
            "role":"assistant",
            "content":ai_message
        }
    )
    #Print conversion history using for loop
    print("\n--- Chat History ---")
    for messsage in messages:
        if messsage["role"]=="user":
            print("You", messsage["content"])
        else:
            print("AI", messsage["content"])
    print("------------------------\n")
    
    
 
""" 
    1)CHUNKING
    2)TYPES OF VECTOR DATA BASES
    """