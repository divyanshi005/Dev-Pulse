CREATE OR REPLACE VIEW analytics.top_questions AS

SELECT
    q.title,
    o.owner_name,
    f.score,
    f.answer_count,
    f.view_count

FROM warehouse.dim_question q

JOIN warehouse.dim_owner o
ON q.owner_id = o.owner_id

JOIN warehouse.fact_question_metrics f
ON q.question_id = f.question_id

ORDER BY f.score DESC;