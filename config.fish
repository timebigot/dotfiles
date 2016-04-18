# profile

if status --is-login
    set PATH $PATH /usr/bin /sbin
end

# alias

alias l 'ls -la'
alias g 'git'
alias c 'clear'
alias v 'vim'
alias install 'sudo pacman -S'
alias uninstall 'sudo pacman -R'
alias py 'python'
alias dot 'cd ~/Projects/dotfiles'
alias vimrc 'vim ~/.vimrc'
alias logout 'openbox --exit'

function myip
    wget http://ipinfo.io/ip -qO -
end
