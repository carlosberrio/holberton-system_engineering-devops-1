# Puppet Manifest that: install Nginx Web Server
# Creates index.html with sample text as body
# Redirects to -> https://www.youtube.com/watch?v=QH2-TGUlwu4
# Redirection must be a “301 Moved Permanently”
# Adds custom HTTP header with the hostname of the server Nginx running on

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

file_line { 'HTTP header':
  ensure => present,
  path   => '/etc/nginx/nginx.conf',
  after  => 'http {',
  line   => 'X-Served-By \$HOSTNAME;'
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx install'],
}
