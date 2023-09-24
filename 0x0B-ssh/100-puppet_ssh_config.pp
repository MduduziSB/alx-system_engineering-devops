#!/usr/bin/env python3
# using Puppet to make changes to our configuration file

$cont = '\n    IdentityFile ~/.ssh/school\n    PasswordAuthentication no'
exec { 'ssh_config':
  path    => '/usr/bin',
  command => "echo '${cont}' >> /etc/ssh/ssh_config",
}
