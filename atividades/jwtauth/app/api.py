from fastapi import FastAPI, Body
from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.auth_handler import sign_jwt

app = FastAPI()

posts = [
    {
        "id": 1,
        "title": "Giovanna",
        "content": "Love"
    }
]

users = []

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False
    

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Hello, World!"}

@app.get("/posts/{id}", tags=["posts"])
async def get_single_post(id: int) -> dict:
    if id > len(posts):
        return {
            "error": "Não tem nenhum post com esse id."
        }

    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }
        
@app.post("/posts", tags=["posts"])
async def add_post(post: PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.model_dump())
    return {
        "data": "post added."
    }

@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user)
    return sign_jwt(user.email)

@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return sign_jwt(user.email)
    return {
        "error": "ta errado os detalhes do login"
    }