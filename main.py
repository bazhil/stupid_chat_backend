from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(
    title="Question Answering API",
    description="Simple API that returns placeholder answers",
    version="1.0.0"
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
        return {
            "answer": "no answer",  # Placeholder response
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing question: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
