# Практика П08 — Docker Compose и мониторинг

Два многоконтейнерных стека Docker Compose:
1. `flask_redis/` — веб-приложение Flask + Redis со счётчиком посещений и нативным endpoint `/metrics`.
2. `monitoring/` — Prometheus + Grafana (дашборд 13659 + панель `Visits per second`) + Blackbox Exporter.

- `report/Отчет_П08.docx` — отчёт со скриншотами
