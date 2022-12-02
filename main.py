from fastapi import FastAPI

from schema import RequestEmail
from mail_service import service

app = FastAPI(title='SMTP TEST')


@app.get("/")
async def root():
    return {"message": "SMTP test"}


@app.post("/email")
async def say_hello(
        request: RequestEmail
):
    status = None
    try:
        await service.send_mail(request.subject, request.email_schema, request.template)
        status = True
    except Exception as e:
        print(e)
        status = False
    finally:
        return {"message": status}



