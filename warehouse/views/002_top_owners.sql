CREATE OR REPLACE VIEW analytics.top_owners AS

SELECT
    o.owner_name,

    COUNT(DISTINCT r.repository_id) AS repository_count,

    SUM(f.stars) AS total_stars,

    ROUND(AVG(f.stars),0) AS average_stars,

    MAX(f.stars) AS highest_starred_repository

FROM warehouse.dim_owner o

JOIN warehouse.dim_repository r
ON o.owner_id = r.owner_id

JOIN warehouse.fact_repository_metrics f
ON r.repository_id = f.repository_id

GROUP BY o.owner_name

ORDER BY total_stars DESC;