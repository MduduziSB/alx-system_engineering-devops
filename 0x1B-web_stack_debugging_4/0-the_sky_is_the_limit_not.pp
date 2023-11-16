# update the limit nginx.
exec { 'fix-limits':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

exec { 'nginx_restart':
  command     => '/etc/init.d/nginx restart',
  refreshonly => true,
  subscribe   => File['/etc/nginx/nginx.conf'],
}
