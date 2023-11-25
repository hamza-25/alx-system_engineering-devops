# Puppet to make changes to our configuration file
include stdlib

file_line { 'No password':
ensure  => present,
path    => '/etc/ssh/ssh_config',
line    => 'PasswordAuthentication no',
replace => True,
}

file_line { 'Identity file':
ensure  => present,
path    => '/etc/ssh/ssh_config',
line    => 'IdentityFile ~/.ssh/school',
replace => True,
}
