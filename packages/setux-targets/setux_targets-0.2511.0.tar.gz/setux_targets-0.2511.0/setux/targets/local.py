from shutil import copy, copytree
from pathlib import Path

from .base import BaseTarget
from . import error, info, debug


# pylint: disable=arguments-differ


class Local(BaseTarget):
    def __init__(self, **kw):
        kw['name'] = kw.get('name', 'local')
        super().__init__(**kw)

    def set_local(self):
        self.local = self
        return self.local

    def run(self, *arg, **kw):
        kw.pop('term', None)
        arg, kw = self.parse(*arg, **kw)
        if sudo := kw.pop('sudo', None):
            try:
                login = self.distro.login.name
                if sudo != login:
                    arg = ['sudo', f'--user={sudo}'] + arg
            except Exception: pass
        ret, out, err =  super().run(*arg, **kw)
        return ret, out, err

    def do_send(self, local, remote):
        local =  Path(local)
        assert local.is_file()
        remote = Path(remote) if remote else local
        if remote == local: return True
        ret, out, err = self.run(f'mkdir -p {remote.parent}')
        if ret: return False
        try:
            copy(local, remote)
            return True
        except:
            return False

    def do_send_as(self, sudo, local, remote):
        local =  Path(local)
        assert local.is_file()
        remote = Path(remote)
        ret, out, err = self.run(f'mkdir -p {remote.parent}', sudo=sudo)
        ok = ret == 0
        ret, out, err = self.run(f'cp {local} {remote}', sudo=sudo)
        ok = ok and ret == 0
        ret, out, err = self.run(f'chown {sudo} {remote}', sudo=sudo)
        ok = ok and ret == 0
        return ok

    def do_fetch(self, remote, local, quiet=False):
        ret, out, err = self.run(f'file {remote}')
        try:
            isdir = out[0].split(':')[1].strip() == 'directory'
        except Exception:
            isdir = False
        fetch = copytree if isdir else copy
        try:
            fetch(remote, local)
            return True
        except:
            return False

    def do_fetch_as(self, sudo, remote, local, quiet=False):
        ret, out, err = self.run(f'file {remote}')
        try:
            isdir = out[0].split(':')[1].strip() == 'directory'
        except Exception:
            isdir = False
        args = '-r' if isdir else ''
        tmp = Path('/tmp/setux/') / Path(local)
        login = self.distro.login.name
        ret, out, err = self.run(f'cp {args} {remote} {tmp}', sudo=sudo)
        ok = ret == 0
        ret, out, err = self.run(f'chown {login} {tmp}', sudo=sudo)
        ok = ok and ret == 0
        return ok

    def do_sync(self, src, dst=None):
        if dst == src: return
        assert Path(src).is_dir()
        if not src.endswith('/'): src+='/'
        if dst:
            self.dir(dst, verbose=False)
            info(f'\tsync {src} -> {dst}')
            return self.rsync(f'{src} {dst}')
        else:
            debug(f'\tskipped {src} -> {dst}')
            return True

    def export(self, path):
        error("can't export on local")

    def remote(self, module, export_path=None, **kw):
        error("can't remote on local")

    def __str__(self):
        return f'Local({self.name})'
