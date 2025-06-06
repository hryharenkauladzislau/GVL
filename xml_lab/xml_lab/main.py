import xml.etree.ElementTree as ET

def load_xml(filename):
    try:
        tree = ET.parse(filename)
        return tree.getroot()
    except Exception as e:
        print(f"Error loading XML: {e}")
        return None

def list_books(root):
    books = root.findall('book')
    prices = []
    for book in books:
        title = book.find('title').text
        author = book.find('author').text
        year = book.find('year').text
        genre = book.find('genre').text
        price = float(book.find('price').text)
        prices.append(price)
        print(f"{title} by {author}, {year}, {genre}, ${price:.2f}")
    if prices:
        avg = sum(prices) / len(prices)
        print(f"Average price: ${avg:.2f}")

def filter_books(root, genre_filter):
    print(f"Books in genre: {genre_filter}")
    for book in root.findall('book'):
        genre = book.find('genre').text
        if genre.lower() == genre_filter.lower():
            print(book.find('title').text)

if __name__ == "__main__":
    root = load_xml("library.xml")
    if root:
        list_books(root)
        filter_books(root, "Dystopia")
