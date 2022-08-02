server {
    listen ${LISTEN_PORT};

    server_name www.api.digitaleasy.cl api.digitaleasy.cl;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass ${APP_HOST}:${APP_PORT};
        include /etc/nginx/uwsgi_params;
        client_max_body_size 10M;
    }

}

server {

    listen 80;

    root /vol/static/digitaleasyapp-front/build;

    index index.html;

    server_name app.digitaleasy.cl www.app.digitaleasy.cl;

    location / {
        try_files $uri /index.html;
    }

}
