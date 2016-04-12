"plugins

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'scrooloose/syntastic'
Plugin 'scrooloose/nerdtree'

call vundle#end()
filetype plugin indent on

"settings

set number
set smarttab
set ignorecase
set noerrorbells
set softtabstop=2
set tabstop=2
set smarttab
set autoindent
set cursorline
set showmatch
set encoding=utf-8
set backspace=indent,eol,start
set relativenumber
set incsearch
set hlsearch
set visualbell

syntax on

filetype plugin indent on

inoremap jk <ESC>

let mapleader="\<Space>"
