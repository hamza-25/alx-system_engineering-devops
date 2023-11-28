# installing nginx using puppet
# Update package lists
exec {'update_apt':
  command => 'sudo apt-get -y update',
  path    => '/usr/bin',
}

# Install Nginx
package {'nginx':
  ensure => present,
  before => File['/var/www/html/index.nginx-debian.html'],
}

# Create Hello World HTML file
file {'/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => 'Hello World!',
  notify  => Exec['nginx_restart'],
}

# Configure Nginx to include redirection rule
file {'/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('module_name/default.erb'), # Use an ERB template for better structure
  notify  => Exec['nginx_restart'],
}

# Restart Nginx
exec {'nginx_restart':
  command => 'sudo service nginx restart',
  refreshonly => true,
}


exec {'nginx_restart':
command     => 'sudo service nginx restart',
refreshonly => true,
}
