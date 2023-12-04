# automate the task of creating a custom HTTP header response
$srv = "
map \$hostname \$var1 {
    ~*01\$ web-01;
    default web-02;
}

server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    location / {
        try_files \$uri \$uri/ =404;
        add_header X-Served-By \$var1;
    }
}
"

file { '/etc/nginx/sites-available/default':
    ensure => present,
    content => "$srv",
}
