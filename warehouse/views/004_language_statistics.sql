CREATE OR REPLACE VIEW analytics.language_statistics AS

SELECT
    l.language_name,

    COUNT(*) AS repository_count,

    SUM(f.stars) AS total_stars,
    ROUND(AVG(f.stars), 0) AS average_stars,
    MAX(f.stars) AS max_stars,
    MIN(f.stars) AS min_stars,

    SUM(f.forks) AS total_forks,
    ROUND(AVG(f.forks), 0) AS average_forks,

    SUM(f.watchers) AS total_watchers,
    ROUND(AVG(f.watchers), 0) AS average_watchers,

    SUM(f.open_issues) AS total_open_issues,
    ROUND(AVG(f.open_issues), 0) AS average_open_issues

FROM warehouse.dim_language l

JOIN warehouse.dim_repository r
    ON l.language_id = r.language_id

JOIN warehouse.fact_repository_metrics f
    ON r.repository_id = f.repository_id

GROUP BY
    l.language_name

ORDER BY
    total_stars DESC;