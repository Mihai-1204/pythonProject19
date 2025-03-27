from flask import Flask, render_template, request, jsonify
from utils.gas import Gas
from utils.diesel import Diesel
from utils.distance import Distance
from roady import Roady
from utils.init_config import config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('roady.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        departure_city = request.form['departure_city']
        destination_city = request.form['destination_city']
        number_of_persons = int(request.form['number_of_persons'])
        consumption = float(request.form['consumption'])
        fuel_type = request.form['fuel_type']
        with_return = bool(request.form.get('with_return'))
        dist = Distance(departure_city, destination_city, config)
        dist_km = dist.km

        if fuel_type == "Gas":
            fuel_price = Gas(config)
        else:
            fuel_price = Diesel(config)

        roady = Roady(dist, fuel_price)
        price = roady.calculate_price(number_of_persons, consumption, with_return)

        return jsonify({"price": round(price, 2)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9267)