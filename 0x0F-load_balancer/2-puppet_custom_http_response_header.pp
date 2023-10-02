# Puppet manifest for configuring custom HTTP header response

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Define a custom fact to retrieve the hostname
# This fact will be used to set the value of the X-Served-By header
# Save this file as "custom_hostname_fact.rb" in the "/etc/puppetlabs/facter/facts.d" directory

file { '/etc/puppetlabs/facter/facts.d/custom_hostname_fact.rb':
  ensure  => file,
  content => '#!/bin/bash
              echo "custom_hostname=$(hostname)"
            ',
}

# Create an Nginx configuration file with the custom HTTP header
file { '/etc/nginx/sites-available/custom_header.conf':
  ensure  => file,
  content => "server {
                listen 80;
                server_name localhost;

                location / {
                  proxy_pass http://backend;
                  add_header X-Served-By $custom_hostname;
                }
              }",
}

# Create a symbolic link to enable the site
file { '/etc/nginx/sites-enabled/custom_header.conf':
  ensure => link,
  target => '/etc/nginx/sites-available/custom_header.conf',
}

# Remove the default Nginx site configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure    => 'running',
  enable    => 'true',
  subscribe => File['/etc/nginx/sites-enabled/custom_header.conf'],
}


