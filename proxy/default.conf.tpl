server {
    listen ${LISTEN_PORT};

    server_name www.api.digitaleasy.cl api.digitaleasy.cl

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass ${APP_HOST}:${APP_PORT};
        include /etc/nginx/uwsgi_params;
        client_max_body_size 10M;
    }

}