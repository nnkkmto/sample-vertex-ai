QUERY = """
WITH min_interactions AS (
    SELECT 
        user_name,
        artist_name
    FROM `listenbrainz.listenbrainz.listen`
    GROUP BY user_name, artist_name
    HAVING count(*) > {min_interactions}
)
, min_user_listens AS (
    SELECT
        user_name
    FROM `listenbrainz.listenbrainz.listen`
    GROUP BY user_name
    HAVING count(*) > {min_user_listens}
)
SELECT DISTINCT
    origin.user_name,
    origin.artist_name
FROM `listenbrainz.listenbrainz.listen` origin
INNER JOIN min_interactions
    ON min_interactions.user_name = origin.user_name
    AND min_interactions.artist_name = origin.artist_name
INNER JOIN min_user_listens
    ON min_user_listens.user_name = origin.user_name
"""