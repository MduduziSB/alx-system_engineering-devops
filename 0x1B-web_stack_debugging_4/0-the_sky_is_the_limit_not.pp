# update the limit nginx.
exec { 'fix-limits':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

exec { 'restart nginx':
  provider => shell,
  command  => 'service nginx restart'
}
