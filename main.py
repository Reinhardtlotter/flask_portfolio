# import "packages" from flask
from flask import Flask, render_template,json, request
import requests

# create a Flask instance
from algorithms.image import image_data

app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")

@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")

@app.route('/binary', methods=['GET', 'POST'])
def binary():
    if request.form:
        bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("binary.html", bits=int(bits))
        # starting and empty input default
    return render_template("binary.html", bits=12)


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet.html", name=name)
    # starting and empty input default
    return render_template("greet.html", name="World")

@app.route('/grid')
def grid():
    return render_template("grid.html")

@app.route('/wireframes')
def wireframes():
    return render_template("wireframes.html")

@app.route('/aboutme')
def aboutme():
    return render_template("aboutme.html")

@app.route('/week3')
def week3():
    return render_template("week3.html")

@app.route('/rgb', methods=["GET", "POST"])
def rgb():
    return render_template("rgb.html", images=image_data())

@app.route('/list')
def list():
    return render_template("list.html")

@app.route('/colorcodes')
def colorcodes():
    return render_template("colorcodes.html")


@app.route('/logicgates')
def logicgates():
    return render_template("logicgates.html")

@app.route('/binary2')
def binary2():
    return render_template("binary2.html")

@app.route('/val', methods=['GET', 'POST'])
def val():
    if request.form:
        bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("val.html", bits=int(bits))
        # starting and empty input default
    return render_template("val.html", bits=12)

@app.route('/controllers')
def controllers():
    return render_template("controllers.html")

@app.route('/duelists')
def duelists():
    return render_template("duelists.html")

@app.route('/initiators')
def initiators():
    return render_template("initiators.html")

@app.route('/sentinels')
def sentinels():
    return render_template("sentinels.html")

@app.route('/kdr', methods=['GET', 'POST'])
def kdr():
    kd_ratio = 0
    great_player = False
    urgood = "Let's see if your good"
    if request.form:
        kills = request.form.get("kills")
        deaths = request.form.get("deaths")
        if deaths is not None :
            kd_ratio = int(kills)/int(deaths)
            if kd_ratio >= 1:
                great_player = True
            else:
                great_player = False
            if great_player == True:
                urgood=("You're a great player!!")
            else:
                urgood=("You suck. Be better")
        else:
            print("do nothing")
    return render_template("kdr.html", kdrval = kd_ratio, gpstatus = great_player, goodplayer=urgood)

@app.route('/maps')
def maps():
    return render_template("maps.html")

@app.route('/weapons')
def weapons():
    url = "https://valorant-weapons.p.rapidapi.com/Sidearms"

    headers = {
        'x-rapidapi-host': "valorant-weapons.p.rapidapi.com",
        'x-rapidapi-key': "8369759d57msh8fa2295ad3d60ccp1b48eajsn37d90ec37799"
    }
    response = requests.request("GET", url, headers=headers)
    output = json.loads(response.text)

    print(response.text)
    return render_template("weapons.html",x=output)


    response = requests.request("GET", url, headers=headers)
    output = json.loads(response.text)

    print(response.text)
    return render_template("weapons.html",x=output)


@app.route('/slider')
def slider():
    return render_template("slider.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)