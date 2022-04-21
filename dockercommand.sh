docker run \
  -it \
  --name data-copier  \
  --rm \
  --network data-copier-nw \
  -v `pwd`/data/retail_db_json:/data/retail_db_json \
  -e BASE_DIR=/data/retail_db_json \
  -e DB_PASS=Changme \
  -e DB_USER=retail_user \
  -e DB_HOST=retail_pg \
  -e DB_PORT=5432 \
  -e DB_NAME=retail_db \
 data-copier_dc-app python /app/app.py "departments categories products orders order_items customers"

