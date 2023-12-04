# automate the task of creating a custom HTTP header response
exec {'update':
provider => shell,
command  => 'sudo apt -y update',
before   => Exec['install_nginx'],
}

exec {'install_nginx':
provider => shell,
command  => 'sudo apt -y install nginx',
before   => Exec['add_header'],
}

exec { 'add_header':
  provider    => shell,
  environment => ["MYNAME=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\default;/include \/etc\/nginx\/sites-enabled\/\default;\n\tadd_header X-Served-By \"$MYNAME\";/" /etc/nginx/nginx.conf',
  before      => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
