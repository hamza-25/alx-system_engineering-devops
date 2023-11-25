# Puppet to make changes to our configuration file
include stdlib

file_line { 'no pass':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  replace => true,
}

file_line { 'identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  replace => true,
}
