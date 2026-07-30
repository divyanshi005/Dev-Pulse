CREATE OR REPLACE VIEW analytics.owner_statistics AS

SELECT
    o.owner_name,
    COUNT(q.question_id) AS questions_posted,
    SUM(f.score) AS total_score,
    SUM(f.view_count) AS total_views,
    AVG(f.answer_count) AS average_answers

FROM warehouse.dim_owner o

JOIN warehouse.dim_question q
ON o.owner_id = q.owner_id

JOIN warehouse.fact_question_metrics f
ON q.question_id = f.question_id

WHERE o.platform = 'stackexchange'

GROUP BY o.owner_name

ORDER BY total_score DESC;