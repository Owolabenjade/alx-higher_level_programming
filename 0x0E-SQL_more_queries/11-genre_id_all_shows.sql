-- This script lists all shows from the 'hbtn_0d_tvshows' database
-- Each record displays 'tv_shows.title' and 'tv_show_genres.genre_id'
-- Shows without a genre will display NULL for 'genre_id'
-- Results are sorted in ascending order by 'tv_shows.title' and 'tv_show_genres.genre_id'

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

