from requests import get

def get_authors(search:str=None):
    authors =[]
    query = get('https://wolnelektury.pl/api/authors/')
    for author_id, author in enumerate(query.json(), start=1):
        if search is None or search in author['name']:
            #todo: convert author to object

            authors.append({
                'author_id': author_id,
                'name': author.get('name'),
                'api_books_url': author.get('href') + 'books'
            })
    return authors

authors = get_authors('Adam')
for author in authors:
    # todo create method to display author as string
    print(f'{author.get("author_id")}. {author.get("name")}')

# print(authors)
search_author_id = int(input('Którego autora książki chcesz zobaczyć? '))
found_author = next(filter(lambda auth: auth.get('author_id') == search_author_id, authors))

for book in get(found_author.get('api_books_url')).json():
    print(f'- {book.get("title")}')