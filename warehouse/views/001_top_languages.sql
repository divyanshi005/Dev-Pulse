CREATE OR REPLACE VIEW analytics.top_languages AS

SELECT

    l.language_name,

    COUNT(DISTINCT r.repository_id) AS repository_count,

    ROUND(AVG(f.stars), 0) AS average_stars,

    MAX(f.stars) AS highest_starred_repository

FROM warehouse.dim_repository r

JOIN warehouse.dim_language l

ON r.language_id = l.language_id

JOIN warehouse.fact_repository_metrics f

ON r.repository_id = f.repository_id

GROUP BY

    l.language_name

ORDER BY repository_count DESC;