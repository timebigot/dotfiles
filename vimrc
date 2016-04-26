"plugins

set shell=/bin/sh

set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'scrooloose/syntastic'
Plugin 'scrooloose/nerdtree'
Plugin 'kien/ctrlp.vim'
"Plugin 'Valloric/YouCompleteMe'
Plugin 'altercation/vim-colors-solarized'
Plugin 'tpope/vim-surround'

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

let python_highlight_all=1
syntax on

inoremap jk <ESC>

"remapping
let mapleader="\<Space>"
let g:ctrlp_map = '<c-p>'
let g:ctrlp_cmd = 'CtrlP'
