E-mail validation to check if the address provided is available to send messages

## Setup

#### install dependencies

```bash
python3 -m venv .venv
```
```bash
source .venv/bin/activate
```
```bassh
pip install -r requirements.txt
```

#### Database

```sql
create database smtp_dns 
```

#### Run server

```bash
source venv/bin/activate
```
```bash
uvicorn main:app --reload
```

## Routes

```
method:
 - GET

query param:
 - email: String

response:
 - Boolean
```

```bash
 http get :8000/smtp/email email==email@email.com
```
`GET` `http://localhost:8000/smtp/email`
```json
{
    "email":"email@email.com"
}
```


```
method:
 - POST

body:
 - emails: Array[Strings]

response:
 - Boolean
```

```bash
 http post :8000/smtp/emails emails:='["one@email.com", "two@email.com"]'
```
`POST` `http://localhost:8000/smtp/emails`
```json
{
    "email":["one@email.com", "two@email.com"]
}
```
