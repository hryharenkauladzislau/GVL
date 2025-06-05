import lxml.etree as ET

def parse_library(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        total_price = 0
        count = 0
        genre_filter = "Fantasy"

        print("Список книг:")
        for book in root.findall("book"):
            title = book.find("title").text
            author = book.find("author").text
            year = book.find("year").text
            genre = book.find("genre").text
            price = float(book.find("price").text)

            print(f"{title} — {author}, {year}, {genre}, ${price:.2f}")

            total_price += price
            count += 1

        avg_price = total_price / count
        print(f"\nСредняя цена книг: ${avg_price:.2f}")

        print(f"\nКниги жанра '{genre_filter}':")
        for book in root.findall("book"):
            if book.find("genre").text == genre_filter:
                print(book.find("title").text)

    except FileNotFoundError:
        print("Файл не найден.")
    except ET.XMLSyntaxError:
        print("Ошибка синтаксиса XML.")
    except Exception as e:
        print("Произошла ошибка:", e)

parse_library("library.xml")
