import asyncio.subprocess
import sys


@asyncio.coroutine
def run_sas(argv):
  SysinFile = argv.pop(1)
  argv += [
      '-batch',
      '-pageno', '1',
      '-linesize', '80',
      '-pagesize', '9999',
      '-nosplash',
      '-sysin',
      SysinFile,
      ]
  create = asyncio.create_subprocess_exec(*argv)
  proc = yield from create
  yield from proc.wait()


if __name__ == '__main__':
  if sys.platform == "win32":
      loop = asyncio.ProactorEventLoop()
      asyncio.set_event_loop(loop)
  else:
      loop = asyncio.get_event_loop()

  argv = sys.argv[1:]
  loop.run_until_complete(run_sas(argv))
