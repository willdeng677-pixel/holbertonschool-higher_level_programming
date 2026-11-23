#!/usr/bin/python3

import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(filepath="products.json"):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def read_csv(filepath="products.csv"):
    products = []
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products


def read_sql(db_path="products.db"):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.route("/products")
def products():
    source = request.args.get("source")
    raw_id = request.args.get("id")
    product_id = request.args.get("id", type=int)

    try:
        if source == "json":
            data = read_json()
        elif source == "csv":
            data = read_csv()
        elif source == "sql":
            data = read_sql()
        else:
            return render_template("product_display.html", error="Wrong source")
    except (sqlite3.Error, FileNotFoundError, json.JSONDecodeError) as err:
        return render_template("product_display.html", error=f"Database error: {err}")

    if raw_id is not None:
        if product_id is None:
            return render_template("product_display.html", error="Product not found")
        data = [item for item in data if item["id"] == product_id]
        if not data:
            return render_template("product_display.html", error="Product not found")

    return render_template("product_display.html", products=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
