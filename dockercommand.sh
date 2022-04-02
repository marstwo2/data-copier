docker run \
  -it \
  --name data-copier \
  --rm \
  --network data-copier-nw \
  -v /home/jshernandez05/Projects/data-copier/data/retail_db_json:/data-copier/data/retail_db_json \
  -e BASE_DIR=/data-copier/data/retail_db_json \
  -e DB_PASS=itversity \
  -e DB_USER=retail_user \
  -e DB_HOST=a936820710aa \
  -e DB_PORT=5432 \
  -e DB_NAME=retail_db \
  data-copier python /data-copier/app/app.py "departments categories"

