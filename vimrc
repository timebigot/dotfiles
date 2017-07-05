"plugins

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'scrooloose/syntastic'
Plugin 'kien/ctrlp.vim'
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
set clipboard+=unnamed

"colors
syntax on
set term=screen-256color
let g:solarized_termcolors=256
set background=dark
"colorscheme solarized
let python_highlight_all=1

"remapped ESC
inoremap jk <ESC>

"new tab
nnoremap <C-t> :tabnew<CR>
inoremap <C-t> <Esc>:tabnew<CR>

"remapping
let mapleader="\<Space>"
let g:ctrlp_map = '<c-p>'
let g:ctrlp_cmd = 'CtrlP'

"nohl by hitting return
nnoremap <CR> :noh<CR>
