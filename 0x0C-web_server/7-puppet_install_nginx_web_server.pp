package {'nginx':
ensure  => present,
version => '1.18.0'
}
$cont="server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;
	location /redirect_me {
		return 301 www.youtube.com;
	}
	error_page 404 /404.html;
	location = /404.html{
		internal;
	}
}"

file {'/var/www/html/index.html':
ensure  => present,
content => 'Hello World!'
}

file {'/etc/nginx/sites-available/default':
ensure  => present,
content => $cont
}

service {'nginx':
ensure => stopped,
}

service {'nginx':
ensure => running,
}
