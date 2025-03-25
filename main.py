from pprint import pprint

from flask import Flask, render_template, request

app = Flask(__name__)


# API/Endpoint
@app.get("/")
def hello_world():
    return "<h1>Super, Cool 😁</h1>"


name = "Jamie"
hobbies = ["Gaming", "Reading", "Soccer", "Ballet", "Gyming", "Yoga"]
users = [
    {
        "name": "Jordan",
        "img": "https://www.beckonmedia.com.au/wp-content/uploads/2018/07/Professional-Portrait-Photography-17.jpg",
    },
    {
        "name": "Ayanda",
        "img": "https://i.pinimg.com/originals/ef/07/32/ef0732e30b721faf2b2986bceb96cfd2.jpg",
    },
    {
        "name": "Kylie",
        "img": "https://img.freepik.com/free-photo/portrait-young-woman-with-natural-make-up_23-2149084942.jpg",
    },
]


@app.get("/about")
def about_page():
    return render_template("about.html", name=name, hobbies=hobbies)


@app.get("/profile")
def profile_page():
    return render_template("profile.html", users=users)


from routes.movies_bp import movies_bp

app.register_blueprint(movies_bp, url_prefix="/movies")

if __name__ == "__main__":
    app.run(debug=True)
