from werkzeug.exceptions import HTTPException
class InternalServerError(HTTPException):
    pass

class SchemaValidationError(HTTPException):
    pass

class MovieAlreadyExistsError(HTTPException):
    pass

class UpdatingMovieError(HTTPException):
    pass

class DeletingMovieError(HTTPException):
    pass

class MovieNotExistsError(HTTPException):
    pass

class EmailAlreadyExistsError(HTTPException):
    pass

class UnauthorizedError(HTTPException):
    pass

class BadTokenError(HTTPException):
    pass

class EmailDoesnotExistsError(HTTPException):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "HTTPException": {
        "message": "Something went wrong",
        "status": 402
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "MovieAlreadyExistsError": {
         "message": "Movie with given name already exists",
         "status": 400
     },
     "UpdatingMovieError": {
         "message": "Updating movie added by other is forbidden",
         "status": 403
     },
     "DeletingMovieError": {
         "message": "Deleting movie added by other is forbidden",
         "status": 403
},
     "MovieNotExistsError": {
         "message": "Movie with given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     },
 "EmailDoesnotExistsError": {
         "message": "Couldn't find the user with given email address",
         "status": 400
     },
     "BadTokenError": {
         "message": "Invalid token",
         "status": 403
      }
}