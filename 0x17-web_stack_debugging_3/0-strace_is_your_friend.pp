# 0-strace_is_your_friend.pp

file { '/var/www/html/wp-settings.php':
  ensure  => 'file',
  content => template('your_module/wp-settings.php.erb'),
  replace => true,
}
