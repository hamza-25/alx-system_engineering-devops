#!/usr/bin/pup
# create a manifest that kills a process named killmenow.
exec{'kill_process':
command     => 'pkill -f killmenow',
provider => 'shell'
}
