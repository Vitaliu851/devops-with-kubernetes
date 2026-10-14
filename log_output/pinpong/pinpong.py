from fastapi import FastAPI, Response
app = FastAPI()

counter =0 
@app.get("/pinpong")
async def pinpong():
    global counter
    current = counter 
    counter +=1
    return Response(content=f"pong {current}\n", media_type="text/plain")
