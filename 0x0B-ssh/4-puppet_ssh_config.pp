# Sets up client SSH configuration file so it can connect to a server without typing a password.
# 	Client configuration must be configured to use the private key ~/.ssh/holberton
# 	Client configuration must be configured to refuse to authenticate using a password

file_line { 'Turn off pwd auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}

file_line { 'Configure identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/holberton',
}
