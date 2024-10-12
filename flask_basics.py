from flask import Flask, request
from flask_migrate import Migrate 
from mod_basics import db

# to create a flask instance
app = Flask(__name__)  ## pass default module name as arguement


# config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'

#  create a migration
migrate = Migrate(app, db)


@app.route('/', methods = ['GET','POST']) #this is a wrapper#
def index():
    # route logic
    return {"message": "Hello World !"}, 401

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)  ## to rerun automatically

@app.get('/about')
def about():
    return """
    <h1>About Page<h1>
    <p>Learning Flask<p>
    """

@app.post('/about')
def create_about():
    return { "message": "About Page Created"}, 201


class User:
    # pass
    no_of_eyes = 2

    def __init__(self,name):
        self.id = None
        self.name = name

    def create_table(cls):
        sql_query = """
            CREATE TABLE IF NOT EXISTS Users (
            id integer primary key autoincrement,
            name ,
            gender varchar(6),)
        """

    def create_user(self):
        sql_query = """
            INSERT INTO Users

        """

    @classmethod
    def find_user(cls):
        sql_query = """
            SELECT FROM User where id = ?      
        """    

        row = cursor.execute(sql_query, (id,)).fetchone()
        print(row)

        if row == None:
            return None
        



John = User('John')
print(John.name)
print(John.no_of_eyes)
print(User.no_of_eyes)





@app.get("/users")
def get_users():
    return []

@app.post('/users')
def create_user():
    return {"message": "User Created successfully"}, 201

@app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def get_user(id):
    if request.method == "GET":

        # user = User.query.filter_by(id = id).first()

        # if user == None:
        #     return {"message": "User not found"}, 404
        
        return {
            "id": id,
            "name": "John Doe"
        }
    
    elif request.method == "PATCH":
        return {f"message": "User {id} updated successfully"}