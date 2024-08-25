from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

API_KEY = "0b1eda90195b0dbe632ed39c542dd42a"
all_movie_details = []

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///greatest-movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class EditForm(FlaskForm):
    rating = StringField(label='Your Rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')


class AddForm(FlaskForm):
    movie = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=True)
    rating = db.Column(db.Float, unique=False, nullable=True)
    ranking = db.Column(db.Integer, unique=False, nullable=True)
    review = db.Column(db.String(80), unique=False, nullable=True)
    img_url = db.Column(db.String(250), unique=False, nullable=True)

    def __repr__(self):
        return f'<Movie {self.title}>'


db.create_all()


# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=None,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()        # Movie.query.order_by(Movie.rating).all()
    all_movies.reverse()
    for i in range(len(all_movies)):
        all_movies[i].ranking = i + 1
    return render_template("index.html", all_movies=all_movies)


@app.route('/edit', methods=["GET", "POST"])
def edit():
    form = EditForm()
    if form.validate_on_submit():
        movie_id = request.args.get('id')
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = float(form.rating.data)
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        searched_movie = form.movie.data
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=en-US&query={searched_movie}&page=1&include_adult=false"
        response = requests.get(url).json()
        global all_movie_details
        all_movie_details = response["results"]
        return render_template("select.html", all_movie_details=all_movie_details)
    return render_template("add.html", form=form)

@app.route("/select")
def add_selected_movie():
    selected_movie_id = int(request.args.get('movie_id'))
    global all_movie_details
    for movie in all_movie_details:
        if movie["id"] == selected_movie_id:
            title = movie["original_title"]
            year = int(movie["release_date"].split("-")[0])
            description = movie["overview"]
            img_url = "https://image.tmdb.org/t/p/w500/" + movie["poster_path"]
            new_movie = Movie(
                title=title,
                year=year,
                description=description,
                rating=None,
                ranking=None,
                review=None,
                img_url=img_url
            )
            db.session.add(new_movie)
            db.session.commit()
            new_movie_id = Movie.query.filter_by(title=title).first().id
            return redirect(url_for('edit', id=new_movie_id))

if __name__ == '__main__':
    app.run(debug=True)
