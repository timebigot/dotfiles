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
alias e 'exit'
alias v 'mvim -v'
alias vi 'mvim -v'
alias vim 'mvim -v'
alias ..='cd ..'

alias p 'cd ~/Projects'
alias dot 'cd ~/Projects/dotfiles'
alias vimrc 'vim ~/.vimrc'
alias config.fish 'vim ~/.config/fish/config.fish'
alias noritr='cd ~/Projects/noritr'

alias py 'python3'
alias python 'python3'
alias manage 'py manage.py'
alias makemigrations 'py manage.py makemigrations'
alias migrate 'py manage.py migrate'
alias server 'py manage.py runserver 0.0.0.0:5000'

function myip
    wget http://ipinfo.io/ip -qO -
end

function tmx
    tmuxp load $argv.yaml
end
