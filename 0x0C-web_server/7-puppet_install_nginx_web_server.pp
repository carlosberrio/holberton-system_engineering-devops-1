# Puppet Manifest that: install Nginx Web Server
# Creates index.html with sample text as body
# Redirects to -> https://www.youtube.com/watch?v=QH2-TGUlwu4
# Redirection must be a “301 Moved Permanently”

package { 'nginx install':
  ensure => installed,
  name   => 'nginx',
}

file { '/var/www/html/index.html':
  content => 'Holberton School',
  path    => '/var/www/html/index.html'
}

file_line { 'redirection 301':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx install'],
}