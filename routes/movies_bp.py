from flask import Blueprint, request

from constants import STATUS_CODE
from extensions import db
from models.movie import Movie

movies_bp = Blueprint("movies_bp", __name__)


# API/Endpoint


@movies_bp.get("/")
def get_movies():
    movies = Movie.query.all()
    movies_dictionary = [movie.to_dict() for movie in movies]
    return movies_dictionary


# print(movies[0].to_dict())


# READ
@movies_bp.get("/<id>")
def get_movie_by_id(id):
    movie = Movie.query.get(id)

    if not movie:
        return {"message": "Movie not found"}, STATUS_CODE["NOT_FOUND"]

    data = movie.to_dict()
    return data


# DELETE
@movies_bp.delete("/<id>")
def delete_movie_by_id(id):
    movie = Movie.query.get(id)
    if not movie:
        return {"message": "Movie not found"}, STATUS_CODE["NOT_FOUND"]

    try:
        data = movie.to_dict()
        db.session.delete(movie)
        db.session.commit()
        return {
            "message": f"Movie has been deleted successfully",
            "data": data,
        }
    except Exception as e:
        db.session.rollback()  # undo: restore data
        return {"message": str(e)}, STATUS_CODE["SERVER_ERROR"]


##CREATE
@movies_bp.post("/")
def create_movie():
    data = request.get_json()
    new_movie = Movie(
        name=data["name"],
        poster=data["poster"],
        rating=data["rating"],
        summary=data["summary"],
        trailer=data["trailer"],
    )
    try:
        db.session.add(new_movie)
        db.session.commit()
        return {
            "message": "Movie created successfully",
            "data": new_movie.to_dict(),
        }, 201  # created
    except Exception as e:
        db.session.rollback()
        return {"message": str(e)}, STATUS_CODE["SERVER_ERROR"]
    # ids = [int(movie["id"]) for movie in movies]
    # new_movie["id"] = str(max(ids) + 1)
    # movies.append(new_movie)
    # return {"message": "Movie created successfully"}


@movies_bp.put("/<id>")
def update_movie_by_id(id):
    body = request.get_json()

    for movie in movies:
        if movie["id"] == id:
            movie.update(body)
            return {"message": f"{movie['name']} updated successfully"}

    return {"message": "Movie not found"}, 404
