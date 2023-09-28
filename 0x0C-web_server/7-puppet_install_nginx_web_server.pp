# installs and configures an Nginx server using Puppet instead of Bash

# updates the package list on the system
exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

# ensures that the 'nginx' package is installed on the system
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

# sets the content of the file to 'Hello World!'.
file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

# modifies the Nginx configuration
exec {'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

# It ensures that the 'nginx' service is running
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
