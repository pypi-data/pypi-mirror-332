# -*- encoding: utf-8 -*-
""" Fast and furious FernetFile interface.
It uses the multithreaded ZSTD compressor.

"""
__author__ = 'bibi21000 aka Sébastien GALLET'
__email__ = 'bibi21000@gmail.com'

import pyzstd
from pyzstd import CParameter, DParameter # noqa F401

from cofferfile import _open_cls
from cofferfile.zstd import clean_level_or_option
from . import CHUNK_SIZE, READ, WRITE, APPEND, EXCLUSIVE # noqa F401
from . import FernetFile as _FernetFile


class FernetFile(pyzstd.ZstdFile):

    def __init__(self, name, mode='r', fileobj=None,
            chunk_size=CHUNK_SIZE, level_or_option=None, zstd_dict=None,
            fernet_key=None, **kwargs):
        """Constructor for the FernetFile class.

        At least one of fileobj and filename must be given a
        non-trivial value.

        The new class instance is based on fileobj, which can be a regular
        file, an io.BytesIO object, or any other object which simulates a file.
        It defaults to None, in which case filename is opened to provide
        a file object.

        When fileobj is not None, the filename argument is only used to be
        included in the gzip file header, which may include the original
        filename of the uncompressed file.  It defaults to the filename of
        fileobj, if discernible; otherwise, it defaults to the empty string,
        and in this case the original filename is not included in the header.

        The mode argument can be any of 'r', 'rb', 'a', 'ab', 'w', 'wb', 'x', or
        'xb' depending on whether the file will be read or written.  The default
        is the mode of fileobj if discernible; otherwise, the default is 'rb'.
        A mode of 'r' is equivalent to one of 'rb', and similarly for 'w' and
        'wb', 'a' and 'ab', and 'x' and 'xb'.

        The fernet_key argument is the Fernet key used to crypt/decrypt data.

        Encryption is done by chunks to reduce memory footprint. The default
        chunk_size is 64KB.

        level_or_option is a dict for ztsd compressions.
        2 parameters are importants for performances and cpu usage when writing:

          - compressionLevel
          - nbWorkers

        Look at `pyzstd documentation <https://pyzstd.readthedocs.io/en/stable/#advanced-parameters>`_
        """
        kwargs.pop('cryptor', None)
        self.fernet_file = _FernetFile(name, mode, fileobj=fileobj,
            fernet_key=fernet_key, chunk_size=chunk_size)
        try:
            super().__init__(self.fernet_file, zstd_dict=zstd_dict,
                level_or_option=clean_level_or_option(level_or_option, mode), mode=mode, **kwargs)
        except Exception:
            self.fernet_file.close()
            raise

    def __repr__(self):
        s = repr(self.fernet_file)
        return '<ZstdFernetFile ' + s[1:-1] + ' ' + hex(id(self)) + '>'


    def close(self):
        try:
            super().close()
        finally:
            if self.fernet_file is not None:
                self.fernet_file.close()


def open(filename, mode="rb", fernet_key=None,
        encoding=None, errors=None, newline=None,
        chunk_size=CHUNK_SIZE,
        level_or_option=None, zstd_dict=None,
        **cryptor_args):
    """Open a ZstdFernet file in binary or text mode.

    The filename argument can be an actual filename (a str or bytes object), or
    an existing file object to read from or write to.

    The mode argument can be "r", "rb", "w", "wb", "x", "xb", "a" or "ab" for
    binary mode.

    """
    return _open_cls(filename, mode=mode, chunk_size=chunk_size,
        encoding=encoding, errors=errors, newline=newline,
        coffer_cls = FernetFile,
        level_or_option=level_or_option, zstd_dict=zstd_dict,
        cryptor='fernet', fernet_key=fernet_key, **cryptor_args)
