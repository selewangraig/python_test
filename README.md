# Django Product API

## Overview

This Django project provides an API for managing products and their variants. It allows for the bulk insertion of products along with their variants using a POST request. This README file serves as a guide for setting up the project, understanding its structure, and utilizing its features.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Bulk Insertion of Products and Variants](#bulk-insertion-of-products-and-variants)
  - [Retrieving Products](#retrieving-products)
- [Dependencies](#dependencies)

## Installation

1. **Clone the Repository:**

   git clone <repository-url>
   cd product_api_project

2. **Install Dependencies:**

   pip install -r requirements.txt

3. **Apply Database Migrations:**

   python manage.py migrate

4. **Run the Development Server:**

   python manage.py runserver

   The server will start at http://127.0.0.1:8000/.

## Usage

### Bulk Insertion of Products and Variants

To insert products along with their variants, send a POST request to the `/products/bulk-create/` endpoint with JSON data containing the product and variant information.

Example JSON request:

![json { "name": "Yoghurt", "image": "yoghurt.jpg", "variants": [ { "sku": "YOGVAN123", "name": "Vanilla Yoghurt", "price": "20.00", "details": "A bottle of vanilla yoghurt" }, { "sku": "YOGCHOC456", "name": "Chocolate Yoghurt", "price": "18.00", "details": "A bottle of chocolate yoghurt" } ] }](image.png)

Example response body:
![{
"id": 5,
"name": "Yoghurt",
"image": "yoghurt.jpg",
"variants": [
{
"sku": "YOGVAN123",
"name": "Vanilla Yoghurt",
"price": "20.00",
"details": "A bottle of vanilla yoghurt"
},
{
"sku": "YOGCHOC456",
"name": "Chocolate Yoghurt",
"price": "18.00",
"details": "A bottle of chocolate yoghurt"
}
]
}](image-1.png)

### Retrieving Products

You can retrieve a list of products by sending a GET request to the `/products/` endpoint.

## Dependencies

- Django
- Django Rest Framework
