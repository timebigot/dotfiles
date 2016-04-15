"plugins

set rtp+=~/.vim/bundle/Vundle.vim
set rtp+={repository_root}/powerline/bindings/vim

call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'scrooloose/syntastic'
Plugin 'scrooloose/nerdtree'
Plugin 'powerline/powerline'
Plugin 'kien/ctrlp.vim'

call vundle#end()
filetype plugin indent on

"settings

set number
set smarttab
set ignorecase
set noerrorbells
set softtabstop=2
set tabstop=8
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
set expandtab
set shiftwidth=4
set smartindent
set cindent

syntax on

filetype plugin indent on

inoremap jk <ESC>

"remapping
let mapleader="\<Space>"
let g:ctrlp_map = '<c-p>'
let g:ctrlp_cmd = 'CtrlP'
