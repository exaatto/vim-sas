vim-sas
====
Use VIM as SAS IDE on MS/Windows

Why vim-sas
----
> Why vim-sas, instead of native SAS IDE?

***Because we can.***

> Why vim-sas, instead of Emacs/ESS?

*Please do not make it a war. I love ESS but just fail to get it work on Windows.*

*No, I can not afford a copy of SAS on *NIX*

*Yes, I still vote for ESS-R.*

> Why vim-sas, instead of [EricGebhart/SAS-Vim](https://github.com/EricGebhart/SAS-Vim)?

*EricGebhart/SAS-Vim is a great inspiration and syntax/indent files are borrowed from it.*

*But EricGebhart/SAS-Vim itself is a little bit ad-hoc, not very VIM-ish and missing features like quickfix.*

How to use vim-sas
--
- Prerequisites: Python3
- Get the codes, e.g. using [pathogen.vim](https://github.com/tpope/vim-pathogen).
```bat
cd ~/.vim/bundle
git clone https://github.com/exaatto/vim-sas.git
```
- Install utility scripts into ```%PATH%```.
```bat
mklink "C:\Windows\saswrapper.py" "%CD%\bin\saswrapper.py"
mklink "C:\Windows\saslogfilt.py" "%CD%\bin\saslogfilt.py"
```
- Configure path to ```sas.exe``` in ```.vimrc```.
```vim
let g:SASExe="\"C:\\Program Files\\SASHome\\SASFoundation\\9.3\\sas.exe\""
```
- My own additional configurations.
```vim
let g:SASOptions="-CONFIG \"C:\\Program Files\\SASHome\\SASFoundation\\9.3\\nls\\en\\sasv9.cfg\" -nosource -nosource2 -nocpuid -noechoauto -nomprint -noovp -noprintmsglist -nosymbolgen -nonotes -nocenter"
augroup filetype
autocmd BufRead *.sas map <F10> :make<CR>
autocmd BufRead *.sas map lst :call SASLstToggle()<CR>
autocmd BufRead *.sas map log :call SASLogToggle()<CR>
augroup END
```

BUGS
--
- There is always a SAS dialog window flashing by so fast that I have no idea.
- Window spliting/resize is still a bit messy.
- I have no plan to parse warning/note messages in SAS log file.

