from flask import render_template
from flask import Flask,request
import mechanize
br = mechanize.Browser()
app = Flask(__name__)
@app.route('/')
def home():
  return render_template('index.html')
@app.route('/links/', methods=('GET', 'POST'))
def link():
  url = request.args.get("url",'')
  try:
   br.open(url)
  except:
    return "There was a error processing the url is the url correct."
  links = []
  extension = request.args.get("extension","")
  for l in br.links():
    if l.url.endswith(extension):
      links.append(l.url)
  return render_template('links.html',links=links) 
  #return "Hello World"
if __name__ == "__main__":
  app.run()
