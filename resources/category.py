from flask_restful import Resource, reqparse
from flask import request
from models import Category,db



class CategoryResource(Resource):
    # create instance of reqparser
    # this is a class attribute
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True, help='Category name is required')


    # /Categories
    # /Categoris/<id>
    def get(self, id= None):
        # means retrieve all categories
        if id == None:
            results = []

            print(request.args)

            categories = Category.query.all()
            for category in categories:
                results.append(category.to_dict())

            return results    
        
        # retrieve a single category
        category = Category.query.filter_by(id = id).first()
        if category is None:
            return {"message": "Category not found"}, 404
        
        return category.to_dict()
        

    def post(self):
        data = self.parser.parse_args()
        category = Category(**data)

        db.session.add(category)
        db.session.commit()

        return {"message":"Category created successfully",
                "category": category.to_dict()}, 201
    

    def patch(self, id):
        data = self.parser.parse_args()

        #retrieve the record
        category = Category.query.filter_by(id=id).first()

        #validate if exists
        if category is None:
            return {"message":"Category not found"}, 404
        
        category.name = data['name']
        db.session.commit()

        return {
            "message":"Category updated successfully",
            "category": category.to_dict()
        }
    

    def delete(self, id):
        #retrieve the record
        category = Category.query.filter_by(id=id).first()

        #validate if exists
        if category is None:
            return {"message":"Category not found"}, 404
        
        db.session.delete(category)
        db.session.commit()

        return {
            "message": " Category deleted successfully."
        }
