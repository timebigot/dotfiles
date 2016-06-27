# profile

if status --is-login
    set PATH $PATH /usr/bin /sbin
end

# vim is life
set -Ux EDITOR

# alias

alias l 'ls -la'
alias g 'git'
alias c 'clear'
alias v 'vim'

alias install 'sudo pacman -S'
alias uninstall 'sudo pacman -R'
alias py 'python'
alias work 'cd ~/Projects'
alias dot 'cd ~/Projects/dotfiles'
alias vimrc 'vim ~/.vimrc'
alias logout 'openbox --exit'
alias manage 'python manage.py'
alias makemigrations 'python manage.py makemigrations'
alias migrate 'python manage.py migrate'
alias server 'python manage.py runserver 0.0.0.0:8000'

function myip
    wget http://ipinfo.io/ip -qO -
end

function tmx
    tmuxp load $argv.yaml
end
