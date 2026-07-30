CREATE OR REPLACE VIEW analytics.tag_statistics AS

SELECT
    t.tag_name,
    COUNT(*) AS question_count,
    SUM(f.view_count) AS total_views,
    SUM(f.answer_count) AS total_answers,
    AVG(f.score) AS average_score

FROM warehouse.dim_tag t

JOIN warehouse.bridge_question_tag b
ON t.tag_id = b.tag_id

JOIN warehouse.fact_question_metrics f
ON b.question_id = f.question_id

GROUP BY t.tag_name

ORDER BY total_views DESC;