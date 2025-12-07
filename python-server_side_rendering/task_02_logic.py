#!/usr/bin/python3
"""
Flask application that dynamically renders items from a JSON file
using Jinja templates with loops and conditionals.
"""

from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/items')
def items():
    """Render items list dynamically from items.json."""
    try:
        with open('items.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except Exception as e:
        print(f"Error reading items.json: {e}")
        items_list = []

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
