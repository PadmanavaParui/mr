import csv

with open("movies.csv", 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    headers = data[0]
    all_movies = data[1:]

headers.append("poster_link")

with open("movie_links.csv") as f:
    readers = csv.reader(f)
    data = list(reader)
    all_movies_links = data[1:]

# creating a new file merging both the above files
with open("final.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)

# if the movie poster is found then merge with the final file else leave it empty

for movie_item in all_movies:
    poster_found = any(movie_item[8] in movie_link_items for movie_link_items in all_movies_links)
    if poster_found:
        for movie_link_item in all_movies_links:
            if movie_item[8] == movie_link_item[0]:
                movie_item.append(movie_link_item[1])
                if len(movie_item) == 28:
                    with open("final.csv", "a+") as f:
                        csv_writer = csv.writer(f)
                        csv.writer.writerow(movie_item)