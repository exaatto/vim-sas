import sys
import re

class SASError:
  def __init__(self, filename, line):
    self.filename = filename
    self.line = line
    self.col = 0
    self.msg = ''

  def __repr__(self):
    return "{0}:{1}:{2}: {3}".format(
        self.filename,
        self.line,
        self.col,
        self.msg
        )


NR_PREFIX_SPACES = 10
line_p = re.compile(r'^(?P<LINE>\d+).*$')
pointer_p = re.compile(r'^ +_+$')
code_p = re.compile(r'^ +.+$')
msg_p = re.compile(r'^(?P<MSG>ERROR .+)$')
empty_p = re.compile(r'^$')
if __name__ == '__main__':
  filename = sys.argv[1]
  logfilename = filename.replace('.sas', '.log')
  with open(logfilename) as f:
    e = None
    flag = 'NONE'
    for l in f:
      print(l, end='')
      if empty_p.match(l):
        continue
      if flag == 'NONE':
        m = line_p.match(l)
        if m:
          e = SASError(filename, m.group('LINE'))
          flag = 'LINE'
        else:
          flag = 'NONE'
      elif flag == 'LINE':
        m = pointer_p.match(l)
        if m:
          e.col = l.find('_') - NR_PREFIX_SPACES
          flag = 'POINTER'
        else:
          m = line_p.match(l)
          if m:
            e = SASError(filename, m.group('LINE'))
            flag = 'LINE'
          else:
            flag = 'NONE'
      elif flag == 'POINTER':
        m = code_p.match(l)
        if m:
          flag = 'CODE'
        else:
          flag = 'NONE'
      elif flag == 'CODE':
        m = msg_p.match(l)
        if m:
          e.msg = m.group('MSG')
          print(str(e))
        e = None
        flag = 'NONE'
