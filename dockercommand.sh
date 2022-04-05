docker run \
  -it \
  --name data-copier  \
  --rm \
  --network data-copier-nw \
  -v `pwd`/data/retail_db_json:/data-copier/data/retail_db_json \
  -e BASE_DIR=/data-copier/data/retail_db_json \
  -e DB_PASS=itversity \
  -e DB_USER=retail_user \
  -e DB_HOST=retail_pg \
  -e DB_PORT=5432 \
  -e DB_NAME=retail_db \
 data-copier_dc-app python /data-copier/app/app.py "departments categories products orders order_items customers"

