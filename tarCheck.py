import tarfile
import hashlib

def sha256(flo):
    hash_sha256 = hashlib.sha256()
    for chunk in iter(lambda: flo.read(4096), b''):
        hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

with tarfile.open('/home/chilly/Codes/spllog/tarballs/clang-19.1.6.src.tar.xz') as mytar:
    for member in mytar.getmembers():
        with mytar.extractfile(member) as _file:
            print('{} {}'.format(sha256(_file), member.name))
