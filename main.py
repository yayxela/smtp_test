from fastapi import FastAPI, UploadFile, File
from pydantic import EmailStr
from schema import RequestEmail
from mail_service import service

app = FastAPI(title='SMTP TEST')


@app.get("/")
async def root():
    return {"message": "SMTP test"}


@app.post("/saved")
async def saved_template(
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


@app.post("/file")
async def file_template(
        subject: str,
        email: EmailStr,
        file: UploadFile = File(..., description='html template file', media_type='text/html')
):
    status = None
    try:
        template = await file.read()
        await service.send_file(subject, email, template.decode('utf-8'))
        status = True
    except Exception as e:
        print(e)
        status = False
    finally:
        return {"message": status}

