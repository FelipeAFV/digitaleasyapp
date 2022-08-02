server {

    listen 80;

    root /vol/static/digitaleasyapp-front/build;

    index index.html;

    server_name app.digitaleasy.cl www.app.digitaleasy.cl;

    location / {
        try_files $uri /index.html;
    }

}