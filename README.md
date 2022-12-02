# SMTP TEST 📮

I created this repository so that everyone could test sending email templates (And did not distract the  developers)


## USAGE
1. `git clone`
2. Create .env `cp .env.example .env`
3. Complete your .env file
4. `docker-compose up -d --build`
5. Go to http://localhost:8080/docs in your browser

## ADD NEW TEMPLATES
* Add your template to `./template` folder.
* Use figure brackets `{{example}}` in template to pass variables
* In request to server in `email_schema` pass your template variables

## EXAMPLE
How to send email with saved template
```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/saved' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "subject": "Test",
  "email_schema": {
    "email": "user@example.com",
    "body": {
      "message": "This is test template"
    }
  },
  "template": "test_template.html"
}'
```
* Make sure you pass any object in schema `body` 