SELECT service_name, COUNT(service_name) FROM deployments
WHERE JULIANDAY(CURRENT_DATE) - JULIANDAY(finished_at) <= 7 AND
status = 'failed' GROUP BY service_name;
