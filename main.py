

from link_shortner import LinkShortner
'''
urls=[
    "https://walla.co.il",
    "https://ynet.co.il",
    "https://yad2.co.il"
]

id=LinkShortner.shorten(urls[2])
'''

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
app=FastAPI()
@app.get("/api/{id}")
def health_check(id: str):
    #return {"status": id} 
    url = LinkShortner.get_url_by_id(id)
    return RedirectResponse(url)

@app.post("/api/shorten")
def creat_url(params: dict):
    url=params["url"]
    id=LinkShortner.shorten(url)
    return {"id":id}