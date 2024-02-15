-- A script that lists all shows, and all genres linked to that show, from the
--     database hbtn_0d_tvshows.
--     If a show doesn’t have a genre, display NULL in the genre column
--     Each record should display: tv_shows.title - tv_genres.name
--     Result must be sorted in ascending order bythe showtitle and genre name
--     You can use only one SELECT statement
--     The database name will be passed as an argument of the mysql command
SELECT tv_shows.title, IFNULL(tv_genres.name, 'NULL') AS genre
FROM tv_shows
LEFT JOIN tv_show_genres on tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_genres.genre_id = tv_genres.id
ORDER by tv_shows.title ASC, genre ASC;
