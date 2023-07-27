# Social Bagpiper

![](social_bagpiper/media/logo.png)

## Run

```sh
docker compose up -d --build
docker compose exec web python manage.py migrate --noinput
docker compose exec web python manage.py collectstatic --no-input --clear
```



Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.
