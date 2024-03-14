-- This script lists all Comedy shows in the 'hbtn_0d_tvshows' database
-- Displays 'tv_shows.title' for shows where the genre is Comedy
-- Results are sorted in ascending order by the show title

SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;

