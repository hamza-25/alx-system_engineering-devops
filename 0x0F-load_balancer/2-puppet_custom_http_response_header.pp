# automate the task of creating a custom HTTP header response
exec {'update':
provider => shell,
command  => 'sudo apt -y update'
}

exec {'install_nginx':
provider => shell,
command  => 'sudo apt -y install nginx'
}

exec { 'add_header':
  provider    => shell,
  environment => ["MYNAME=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\default;/include \/etc\/nginx\/sites-enabled\/\default;\n\tadd_header X-Served-By \"$MYNAME\";/" /etc/nginx/nginx.conf',
  before      => Exec['restart Nginx'],
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
