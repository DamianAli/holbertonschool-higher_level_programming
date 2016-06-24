\! echo "\nNumber of season by TVShow ordered by name (A-Z)?"
SELECT name, count(Season.id) AS nb_seasons FROM TVShow JOIN Season ON TVShow.id=Season.tvshow_id GROUP BY name;

\! echo "\nList of Network by TVShow ordered by name (A-Z)?"
SELECT TVShow.name AS 'TVShow name', Network.name AS 'Network name' FROM TVShow JOIN Network ON TVShow.network_id=Network.id ORDER BY TVShow.name;

\! echo "\nList of TVShows ordered by name (A-Z) in the Network 'Fox (US)'?"
SELECT TVShow.name FROM TVShow JOIN Network ON TVShow.network_id=Network.id WHERE Network.name ='FOX (US)';

\! echo "\nNumber of episodes by TVShows ordered by name (A-Z)?"
SELECT TVShow.name, count(Episode.number) AS 'nb_episodes' FROM TVShow JOIN Season ON TVShow.id=Season.tvshow_id JOIN Episode ON Season.id=Episode.season_id GROUP BY TVShow.name ORDER BY TVShow.name;
