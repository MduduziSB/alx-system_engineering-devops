# 0-strace_is_your_friend.pp

exec { 'replace phpp with php':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
