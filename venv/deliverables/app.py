from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a list of products
products = [
 
     
      {"name": 'Blue shirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'White shirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Cream White shirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Cream-yellow shirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Blue-checked shirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red-Checked shirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Pink-Checked shirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Green-Checked shirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Blue shirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Black Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Grey Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Green Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Red Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Blue Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Navi-Blue Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Khaki Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Maroon Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Black Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Black Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Grey Short', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Green Short', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Black Short', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Ash-Grey Short', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Blue Short', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Short', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Maroon Short', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Khaki Short', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Grey Short', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Blue Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Black Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Navi-Blue Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Sky-Blue Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Maroon Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Purple Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'White Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Yellow Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Red Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Green Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Blue Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Blue Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Purple-Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Green-Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Blue-Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Red-Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Brown-Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Grey Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Blue Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Black Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Red Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Maroon Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Ash-Grey Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Sky-Blue Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Brown Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Grey Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Grey Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Red Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Blue Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Black Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Checked Pink Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Checked Red Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Green Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Purple Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Maroon Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'White Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Checked Blue Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Skirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Skirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Skirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Skirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Skirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Skirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Skirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Skirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Skirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Tie', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Tie', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''}, 
      {"name": 'Blue shirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'White shirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Cream-white shirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Cream-yellow shirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Blue-checked shirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red-Checked shirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Pink-Checked shirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Green-Checked shirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Blue shirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Black Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Grey Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Green Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Red Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Blue Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Navi-Blue Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Khaki Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Maroon Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Black Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Black Trousers',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Grey Short', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Green Short', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Black Short', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Ash-Grey Short', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Blue Short', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Short', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Maroon Short', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Khaki Short', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Grey Short', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Blue Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Black Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Navi-Blue Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Sky-Blue Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Maroon Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Purple Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'White Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Yellow Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Red Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Green Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Blue Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Blue Tracksuit',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Purple-Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Green-Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Blue-Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Red-Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Brown-Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Fleece Jacket',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Grey Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Blue Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Black Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Red Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Maroon Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Ash-Grey Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Sky-Blue Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Brown Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Grey Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Grey Sweater',
      "price": {"start": 12.30, "end": 16.30},
      "ImageUrl": ''},
  
      {"name": 'Red Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Blue Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Black Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Checked Pink Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Checked Red Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Green Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Purple Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Maroon Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'White Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Checked Blue Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Dress', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Skirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Skirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Skirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Skirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Skirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Skirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Skirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Skirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Skirt', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Tie', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Tie', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Tie', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Tie', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Tie', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Tie', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Tie', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Tie', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Tie', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Tie', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Tie', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Tie', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Tie', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Tie', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Tie', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},
  
      {"name": 'Red Tie', "price": {"start": 12.30, "end": 16.30}, "ImageUrl": ''},

    # Add more products as needed
]

@app.route('/')
def index():
    return 'Welcome to the Product Search API!'

@app.route('/search')
def search_products():
    # Get the search query from the request URL
    query = request.args.get('q')
    
    if not query:
        return jsonify({"error": "No search query provided"}), 400
    
    # Filter products based on the search query
    search_results = [product for product in products if query.lower() in product['name'].lower()]
    
    return jsonify(search_results)

if __name__ == '__main__':
    app.run(debug=True)
