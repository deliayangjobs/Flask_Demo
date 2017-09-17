from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [{
    'name': 'My Wonderful Store',
    'items': [{'name':'my item', 'price': 15.99 }]
}]

@app.route('/')
def home():
  return render_template('index.html')

#post /store data: {name :}
@app.route('/store' , methods=['POST'])
def create_store():
    req_data = request.get_json()
    new_store= {
        'name': req_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

#get /store/<name> data: {name :}
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if name == store['name']:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

#get /store
@app.route('/store')
def get_stores():
  return  jsonify(stores)

#post /store/<name> data: {name :}
@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
    req_data = request.get_json()
    for store in stores:
        if name == store['name']:
            new_item = {'name': req_data['name'],
                        'price': req_data['price']}
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

#get /store/<name>/item data: {name :}
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if name == store['name']:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})

app.run(port=5000)
