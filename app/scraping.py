import requests

def fetch_books(query):
    books = []
    # # Google Books API (existing)
    # google_books_url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
    # response = requests.get(google_books_url)
    # if response.status_code == 200:
    #     data = response.json()
    #     for item in data.get("items", []):
    #         book = {
    #             "title": item["volumeInfo"].get("title"),
    #             "authors": ", ".join(item["volumeInfo"].get("authors", [])),
    #             "description": item["volumeInfo"].get("description", "No description available."),
    #             "thumbnail": item["volumeInfo"].get("imageLinks", {}).get("thumbnail"),
    #             "link": item["volumeInfo"].get("infoLink"),
    #         }
    #         books.append(book)
    
 # Project Gutenberg API
    gutenberg_url = f"https://gutendex.com/books/?search={query}"
    response = requests.get(gutenberg_url)
    if response.status_code == 200:
        data = response.json()
        for item in data.get("results", []):
            # Extract image URL from formats
            thumbnail = item["formats"].get("image/jpeg", "")
            book = {
                "title": item["title"],
                "authors": ", ".join(author["name"] for author in item["authors"]),
                "description": "Public domain book.",
                "thumbnail": thumbnail,
                "link": f"https://www.gutenberg.org/ebooks/{item['id']}",
            }
            books.append(book)

    return books