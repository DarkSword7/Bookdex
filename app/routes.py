from flask import Blueprint, render_template, request
from .scraping import fetch_books
import requests
import re

# Create a Blueprint for the routes
main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route('/read')
def read_book():
    book_link = request.args.get('link')
    if not book_link:
        return "No book link provided.", 400
    
    # Extract the book ID from the provided link
    try:
        book_id = book_link.split('/')[-1]
        # Construct the URL for the raw book content
        book_url = f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"
    except Exception as e:
        return f"Error processing the link: {str(e)}", 400

    return render_template("read.html", book_url=book_url)