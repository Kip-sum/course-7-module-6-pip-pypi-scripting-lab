from datetime import datetime
import requests


def fetch_data():
    """
    Fetch data from a public API.
    """
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    if response.status_code == 200:
        return response.json()

    return {}


def write_log(post):
    """
    Write log information to a text file.
    """
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        file.write("=== Automation Tool Log ===\n")
        file.write(f"Date: {datetime.now()}\n\n")

        file.write("Fetched Post Information\n")
        file.write("------------------------\n")
        file.write(f"Title: {post.get('title', 'No title found')}\n")
        file.write(f"Body: {post.get('body', 'No body found')}\n")

    print(f"Log written to {filename}")


if __name__ == "__main__":
    post = fetch_data()

    print(
        "Fetched Post Title:",
        post.get("title", "No title found")
    )

    write_log(post)