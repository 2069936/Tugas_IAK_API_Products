from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Sample products data
products = {
    "1": {
        "name": "Smartphone",
        "brand": "TechBrand",
        "quantity": 100,
        "price": 5000000,
        "category": "Electronics"
    },
    "2": {
        "name": "Laptop",
        "brand": "CompTech",
        "quantity": 50,
        "price": 15000000,
        "category": "Electronics"
    },
    "3": {
        "name": "Headphones",
        "brand": "SoundMax",
        "quantity": 200,
        "price": 300000,
        "category": "Accessories"
    },
    "4": {
        "name": "Smartwatch",
        "brand": "WearTech",
        "quantity": 75,
        "price": 2000000,
        "category": "Wearables"
    },
    "5": {
        "name": "Tablet",
        "brand": "TabCo",
        "quantity": 60,
        "price": 7000000,
        "category": "Electronics"
    }
}

class ProductList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "Success",
            "count": len(products),
            "products": products
        }

class ProductDetail(Resource):
    def get(self, product_id):
        if product_id in products:
            return {
                "error": False,
                "message": "Success",
                "product": products[product_id]
            }
        return {"error": True, "message": "Product not found"}, 404

class AddProduct(Resource):
    def post(self):
        data = request.get_json()
        product_id = str(len(products) + 1)
        new_product = {
            "name": data.get("name"),
            "brand": data.get("brand"),
            "quantity": data.get("quantity"),
            "price": data.get("price"),
            "category": data.get("category")
        }
        products[product_id] = new_product
        return {
            "error": False,
            "message": "Product added successfully",
            "product": new_product
        }, 201

class UpdateProduct(Resource):
    def put(self, product_id):
        if product_id in products:
            data = request.get_json()
            product = products[product_id]
            product["name"] = data.get("name", product["name"])
            product["brand"] = data.get("brand", product["brand"])
            product["quantity"] = data.get("quantity", product["quantity"])
            product["price"] = data.get("price", product["price"])
            product["category"] = data.get("category", product["category"])
            return {
                "error": False,
                "message": "Product updated successfully",
                "product": product
            }
        return {"error": True, "message": "Product not found"}, 404

class DeleteProduct(Resource):
    def delete(self, product_id):
        if product_id in products:
            deleted_product = products.pop(product_id)
            return {
                "error": False,
                "message": "Product deleted successfully",
                "product": deleted_product
            }
        return {"error": True, "message": "Product not found"}, 404

# Add routes for product-related endpoints
api.add_resource(ProductList, '/products')
api.add_resource(ProductDetail, '/products/<string:product_id>')
api.add_resource(AddProduct, '/products/add')
api.add_resource(UpdateProduct, '/products/update/<string:product_id>')
api.add_resource(DeleteProduct, '/products/delete/<string:product_id>')

if __name__ == '__main__':
    app.run(debug=True)
