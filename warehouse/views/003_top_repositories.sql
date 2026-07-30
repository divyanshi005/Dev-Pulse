CREATE OR REPLACE VIEW analytics.top_repositories AS

SELECT

    r.full_name AS repository_name,

    o.owner_name,

    l.language_name,

    f.stars,

    f.forks,

    f.watchers,

    f.open_issues

FROM warehouse.dim_repository r

JOIN warehouse.dim_owner o
ON r.owner_id = o.owner_id

LEFT JOIN warehouse.dim_language l
ON r.language_id = l.language_id

JOIN warehouse.fact_repository_metrics f
ON r.repository_id = f.repository_id

ORDER BY f.stars DESC;