from pydantic import BaseModel, EmailStr, root_validator
from typing import Dict, Any, Optional


class EmailSchema(BaseModel):
    email: EmailStr
    body: Dict[str, Any] = {"message": "This is test template"}

    @root_validator
    def check_body(cls, v):
        body = v.get('body')
        if len(body) == 0:
            raise ValueError('Body must be filled, otherwise the message will be empty')
        return v


class RequestEmail(BaseModel):
    subject: str = 'Test'
    email_schema: EmailSchema
    template: str = 'test_template.html'
