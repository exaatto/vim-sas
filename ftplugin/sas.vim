" Only do this when not done yet for this buffer
if exists("b:did_ftplugin") | finish | endif

" Don't load another plug-in for this buffer
let b:did_ftplugin = 1

function! s:set(var, default)
  if !exists(a:var)
    if type(a:default)
      execute 'let' a:var '=' string(a:default)
    else
      execute 'let' a:var '=' a:default
    endif
  endif
endfunction

call s:set("g:SASExe", "sas.exe")
call s:set("g:SASOptions", "")

let &makeprg="saswrapper.py " . g:SASExe . " \"" . expand("%:p") . "\" " . g:SASOptions
let &shellpipe="& saslogfilt.py " . expand("%:t") . " > "
let &errorformat="%f:%l:%c: %m"

let g:SASLstFile=''
let g:SASLogFile=''
function SASWindowToggle(filename, suffix)
  if (a:filename == '')
    vertical rightbelow 80 split
    if (a:suffix == '.lst')
      let g:SASLstFile = expand("%:p:r") . a:suffix
      exec "edit " . g:SASLstFile
    else
      let g:SASLogFile = expand("%:p:r") . a:suffix
      exec "edit " . g:SASLogFile
    endif
  else
    let wnr = bufwinnr(a:filename)
    exec wnr . " wincmd w"
    close
    exec "bdelete " . a:filename
    if (a:suffix == '.lst')
      let g:SASLstFile = ''
    else
      let g:SASLogFile = ''
    endif
  endif
endfunction

function SASLstToggle()
  call SASWindowToggle(g:SASLstFile, '.lst')
endfunction
function SASLogToggle()
  call SASWindowToggle(g:SASLogFile, '.log')
endfunction

