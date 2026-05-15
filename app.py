from flask import Flask, render_template, request, redirect, url_for

app= Flask(__name__)

levels = {
    1 :{
        "question": "48.71228084157847, 2.170049928081917",
        "answer": "1001"
    },
    2 :{
        "question": "“I am white and watch Paris from above. Artists gather at my feet. My name speaks of love and faith. Looks where the hearts are locked for ever”",
        "answer": "2002"
    },
    3 :{
        "question": "",
        "answer": "3003"
    },
    4 :{
        "question": "48.72544605282604, 2.2625433859515467, 1115",
        "answer": "3003"
    },
}

hints = {
    1: {
        "text": "GPS adress",
        "image": None
    },
    2: {
        "text": "Look carefully at this picture.",
        "image": None
    },
    3: {
        "text": "",
        "image": None
    },
    4: {
        "text": "Lock to travel",
        "image": None
    }
}


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/readme')
def readme():
    return render_template('readme.html')

@app.route("/win")
def win():
    return render_template('win.html')

@app.route('/game/<int:level>', methods=["GET", "POST"])
def game(level):
    error=None
    success = False

    if level not in levels:
        return "Game finished ! "
    
    if request.method =="POST":
        user_code = request.form["code"]
        if user_code == levels[level]["answer"]:
            if level+1 in levels:
                return redirect(url_for("game", level=level+1))
            else:
                return redirect(url_for('win'))
        else:
            error = "Wrong answer... Try again"


    return render_template('game.html', level = level, question=levels[level]["question"], error=error, hint=hints[level])

if __name__ == "__main__":
    app.run(debug=True)