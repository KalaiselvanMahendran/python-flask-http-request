from flask import Flask
from flask import render_template
from flask import request
from flask import requests
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/searchGithub', methods=['POST'])
def searchGithub():
    githubUser =  request.form['username'];
    response = requests.get('https://api.github.com/users/' + githubUser)
    html = json.load(response)
    reposUrl = html['repos_url']
    repoList = urllib2.urlopen(reposUrl)
    repoListJson = json.load(repoList)
    return json.dumps(repoListJson);

if __name__ == "__main__":
    app.run()
