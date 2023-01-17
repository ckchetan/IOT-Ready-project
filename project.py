import json
from jinja2 import Environment,FileSystemLoader

with open('project.json') as f:
   data = json.load(f)
fileLoader=FileSystemLoader("templates")
env=Environment(loader=fileLoader)

render=env.get_template("design.html").render(data=data,title="simple page")

fileName="index.html"

with open(f"./site/{fileName}","w")as f:
    f.write(render)