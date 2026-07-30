CREATE OR REPLACE VIEW analytics.top_tags AS

SELECT
    t.tag_name,
    COUNT(*) AS question_count,
    AVG(f.score) AS average_score,
    AVG(f.view_count) AS average_views

FROM warehouse.dim_tag t

JOIN warehouse.bridge_question_tag b
ON t.tag_id = b.tag_id

JOIN warehouse.fact_question_metrics f
ON b.question_id = f.question_id

GROUP BY t.tag_name

ORDER BY question_count DESC;