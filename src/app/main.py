from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from . import question_info 


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"],
)


class QuestionInfo(BaseModel):
    id : int
    title : str
    question_content : str
    question_example_one_test : str
    question_example_one_answer : str
    question_example_one_explanation : str
    question_example_two_test : str
    question_example_two_answer : str
    question_example_two_explanation : str
    question_scaffold : str
    question_tag : str

class QuestionMeta(BaseModel):
    number_of_questions: int
    question_meta: dict


@app.get("/getQuestionInfo/{id}")
async def get_question_info(id: int):
    if id not in question_info.questions.keys():
        raise HTTPException(status_code=404, detail="Question not found")
    return QuestionInfo(**question_info.questions[id])


@app.get("/getQuestionMeta")
async def get_question_meta():
    number_of_questions = len(question_info.questions)
    return QuestionMeta(number_of_questions=number_of_questions,
                        question_meta=question_info.questions)

