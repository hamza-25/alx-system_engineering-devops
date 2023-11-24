#!/usr/bin/pup
# create a manifest that kills a process named killmenow.
exec{'kill_process':
command     => 'pkill -f killmenow',
refreshonly => true,
onlyif      => 'pkill -f killmenow'
}
