from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_question_info_query():
    response = client.get("/getQuestionInfo/1")
    assert response.status_code == 200
    assert response.json().get("id") == 1

def test_get_question_info_bad_query():
    response = client.get("/getQuestionInfo/0")
    assert response.status_code == 404
    assert response.json() == {"detail": "Question not found"}

def test_get_question_meta():
    response = client.get("/getQuestionMeta")
    assert response.status_code == 200
    # check that the number of questions is correct
    assert len(response.json().get("question_meta")) == response.json().get("number_of_questions")