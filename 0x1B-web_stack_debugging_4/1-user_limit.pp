# user files limit

exec {'rep_1':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile unlimited/" /etc/security/limits.conf',
  before   => Exec['rep_2'],
}

exec {'rep_2':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile unlimited/" /etc/security/limits.conf',
}
