from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

from fastapi.middleware.cors import CORSMiddleware

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


app = FastAPI(
    title="Question Answering API",
    description="Simple API that returns placeholder answers",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    replica: str


@app.post("/get_answer", response_model=Message)
async def get_answer(request: Optional[Message]):
    """
    Endpoint that accepts a question and returns a placeholder answer
    
    - **question**: The question text to be answered
    - **metadata**: Optional additional context (not processed in this example)
    """
    try:
        result = Message(replica="no answer")

        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing question: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
