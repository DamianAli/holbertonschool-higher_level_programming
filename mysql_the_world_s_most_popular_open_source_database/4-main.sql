\! echo "\nList of all TVShows by all Genres ordered by genre name (A-Z)? (if a genre has 0 TVShow, please display NULL)"
SELECT Genre.name AS 'Genre name', TVShow.name AS 'TVShow name' FROM Genre LEFT JOIN TVShowGenre ON Genre.id=TVShowGenre.genre_id LEFT JOIN TVShow ON TVShowGenre.tvshow_id=TVShow.id ORDER BY Genre.name ASC;

\! echo "\nName of the pilot (first episode of the first season) of each TVShow ordered by TVShow name (A-Z)?"
SELECT TVShow.name AS 'TVShow name', Episode.name AS 'Episode name' FROM TVShow JOIN Season ON TVShow.id=Season.tvshow_id JOIN Episode ON Season.id=Episode.season_id WHERE Season.number = 1 && Episode.number = 1 ORDER BY TVShow.name;

\! echo "\nList of all Genres by all TVShows ordered by TVShow name (A-Z)? (if a genre has 0 TVShow, please display NULL as TVShow name)"
SELECT TVShow.name AS 'TVShow name', Genre.name AS 'Genre name' FROM Genre LEFT JOIN TVShowGenre ON Genre.id=TVShowGenre.genre_id LEFT JOIN TVShow ON TVShowGenre.tvshow_id=TVShow.id ORDER BY TVShow.name;
