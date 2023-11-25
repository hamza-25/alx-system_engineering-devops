# Let’s practice using Puppet to make changes to our configuration file
include stdlib


file_line { 'No password':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => 'PasswordAuthentication no'
}

file_line { 'Identity file':
ensure => present,
path   => '/etc/ssh/ssh_config',
linr   => 'IdentityFile ~/.ssh/school'
}
