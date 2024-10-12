from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin


# this allows us to define our tables and table columns
metadata = MetaData()

# create flask sqlalcemy extension and link it to sqlalchemy
db =  SQLAlchemy(metadata = metadata)

"""
-> Must have the __tablename__ property
-> Must have at least one column (attribute)
-> Must inherit from db.Model
"""


class Menu(db.Model, SerializerMixin):
    __tablename__ = "menus"
    #columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer, nullable = False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    created_at = db.Column(db.TIMESTAMP)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }
    
    ## defining many to one relationship
    category = db.relationship("Category", back_populates = "menus")
    # serializer rules
    # serialize_only = ('name')

    # serializer rules (negates)
    serialize_rules = ('-category.menus', '-category_id',)



class Category(db.Model, SerializerMixin):
    __tablename__= "category"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)

    #one to many
    menus = db.relationship('', back_populates= 'category')

    serialize_rules = ('-menus',)



class Users(db.Model, SerializerMixin):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    # role = db.Column()
    phone = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)

    # never sedn password back to client
    serialize_rules = ('-password')


