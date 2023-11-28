# installing nginx using puppet
package {'nginx':
ensure  => present,
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
	error_page 404 /custome_404.html;
	location = /404.html{
		internal;
	}
}"

file {'/var/www/html/index.html':
ensure  => present,
content => 'Hello World!'
}

file {'/var/www/html/custome_404.html':
ensure  => present,
content => "Ceci n'est pas une page"
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
