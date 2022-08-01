server {

    server_name www.api.digitaleasy.cl api.digitaleasy.cl;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass ${APP_HOST}:${APP_PORT};
        include /etc/nginx/uwsgi_params;
        client_max_body_size 10M;
    }
    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/api.digitaleasy.cl-0001/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/api.digitaleasy.cl-0001/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}
server {
    if ($host = www.api.digitaleasy.cl) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    if ($host = api.digitaleasy.cl) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    listen 80;

    server_name www.api.digitaleasy.cl api.digitaleasy.cl;
    return 404; # managed by Certbot




}
