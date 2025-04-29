from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Question Answering API",
    description="Simple API that returns placeholder answers",
    version="1.0.0"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    answer: str


@app.post("/get_answer", response_model=AnswerResponse)
async def get_answer(request: QuestionRequest):
    """
    Endpoint that accepts a question and returns a placeholder answer
    
    - **question**: The question text to be answered
    - **metadata**: Optional additional context (not processed in this example)
    """

    try:
        answer = "no answer"  # Placeholder response
        response_data = {"answer": answer}

        return response_data
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail=f"Error processing question: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
