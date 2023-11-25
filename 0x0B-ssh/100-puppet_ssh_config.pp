# Let’s practice using Puppet to make changes to our configuration file
file_line {'no pass':
ensure => 'present',
path   => '/etc/ssh/ssh_config',
line   => 'PasswordAuthentication no'
}

file_line {'set identity':
ensure => 'present',
path   => '/etc/ssh/ssh_config',
linr   => 'IdentityFile ~/.ssh/school'
}
