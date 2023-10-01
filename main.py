from fastapi import FastAPI, Response ,HTTPException, status
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()
class Post(BaseModel):
        title:str
        content:str
        published: bool =True
       
my_posts = [{"title":"title of post 1","content": "content of post 1", "id": 1},
            {"title":"fovourte foods", "content": "i like pizza","id":2}]

def find_post(id):
        for p in my_posts:
             if p["id"] == id:
                   return p

@app.get("/")
def root():
    return {"message": "Hello World today"}

@app.get("/posts")
def get_posts():
    return{"data":my_posts}

@app.post("/posts")
def create_posts(post: Post):
                post_dict =post.dict()
                post_dict['id']=randrange(0,1000000)
                my_posts.append(post_dict)
                return{"data":post_dict}

@app.get("/posts/{id}")
def get_post(id:int, response: Response):
        post = find_post(id)
        if not post:
               raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                                    detail=f"post with id:{id} was bot found")
               
        return{"post_details": post}