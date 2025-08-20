# airflow-spark-etl
cat > README.md << 'EOF'
# Airflow + Spark ETL (Local)

This project runs a Spark ETL script from an Airflow DAG using Docker Compose.

- Airflow UI: http://localhost:8080 (user/pass created during init)
- Spark job code lives in: ./spark_jobs/etl_pipeline.py
- DAGs live in: ./dags/
EOF