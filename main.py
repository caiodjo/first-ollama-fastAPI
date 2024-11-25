from fastapi import FastAPI
import ollama

app = FastAPI()

@app.get("/")
def read_root():
  try:
    response = ollama.chat(model="tinyllama", messages=[
      {
        "role":"user",
        "content":"whats 2+2"
      }
    ])
    llm_res = response.get('message', {}).get('content', '')
    return{"Reposta da llm": llm_res}
  except Exception as e:
    raise Exception()