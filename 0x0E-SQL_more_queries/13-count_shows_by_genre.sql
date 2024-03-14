-- This script lists all genres from 'hbtn_0d_tvshows' and displays the number of shows linked to each
-- Displays 'tv_genres.name' as 'genre' and count of linked shows as 'number_of_shows'
-- Excludes genres with no shows linked and sorts results in descending order by 'number_of_shows'

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC, genre ASC;

