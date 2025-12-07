#!/usr/bin/python3
"""
Flask application that reads product data from JSON or CSV and displays it dynamically.
"""

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json_file(filename):
    """Read JSON file and return list of product dictionaries."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []


def read_csv_file(filename):
    """Read CSV file and return list of product dictionaries."""
    products = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert id and price to proper types
                try:
                    row['id'] = int(row.get('id', 0))
                    row['price'] = float(row.get('price', 0))
                except ValueError:
                    row['id'] = 0
                    row['price'] = 0.0
                products.append(row)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return products


@app.route('/products')
def products():
    """
    Display products from JSON or CSV file based on 'source' query parameter.
    Optional 'id' parameter filters for a single product.
    """
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', type=int)

    # Read data based on source
    if source == 'json':
        data = read_json_file('products.json')
    elif source == 'csv':
        data = read_csv_file('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source", products=[])

    # Filter by id if provided
    if product_id is not None:
        filtered = [p for p in data if p.get('id') == product_id]
        if not filtered:
            return render_template('product_display.html', error="Product not found", products=[])
        data = filtered

    return render_template('product_display.html', products=data, error=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
