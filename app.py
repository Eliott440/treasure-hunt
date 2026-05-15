from flask import Flask, render_template, request, redirect, url_for

app= Flask(__name__)

levels = {
    1 :{
        "comment" : "",
        "question": "48.71228084157847, 2.170049928081917, , page ",
        "answer": "9642"
    },
    2 :{
        "comment" : "",
        "question": "“I am white and watch Paris from above. Artists gather at my feet. My name speaks of love and faith. Looks where the hearts are locked for ever”",
        "answer": "1308"
    },
    3 :{
        "comment" : "Congratulation ! The cadenas is yours now, do what you want with it",
        "question": "48.858278, 2.348444, a tree well explained",
        "answer": "3894"
    },
    4 :{
        "comment" : "",
        "question": "48.85565848022269, 2.3514410712081717, come on ! Don't miss the bus !",
        "answer": "5662"
    },
    5 :{
        "comment" : "You are really close !!!",
        "question": "48.72544605282604, 2.2625433859515467, 1115, 2-6-9",
        "answer": "195"
    },
}

hints = {
    1: {
        "text": "GPS adress",
        "image": None
    },
    2: {
        "text": "Look carefully at this picture.",
        "image": "image/hint1.jpg"
    },
    3: {
        "text": "Look carefully at this picture",
        "image": "image/hint2.jpg"
    },
    4: {
        "text": "Is the bus on time ?",
        "image": None
    },
    5: {
        "text": "Lock to travel, pi is a great number",
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


    return render_template('game.html', level = level, question=levels[level]["question"], error=error, hint=hints[level], comment=levels[level]["comment"])

if __name__ == "__main__":
    app.run(debug=True)