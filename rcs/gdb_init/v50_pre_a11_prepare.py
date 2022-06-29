#!/usr/bin/env python

import gdb
import os

code_base  = os.environ['HOME'] + '/Workspace/Code/android/11/android-11-dev-v50-pre'
out_prefix = 'out/target/product/marconi'
out_symbol = code_base + '/' + out_prefix + '/symbols'
out_sp_arr = ['/system/bin', '/system/lib64', '/system/lib']
out_sp     = ";".join(list(out_symbol + i for i in out_sp_arr))

gdb.execute('')
gdb.execute('set osabi GNU/Linux')
gdb.execute('set auto-solib-add off')
gdb.execute('set print thread-events off')
gdb.execute('set print pretty on')
gdb.execute('dir ' + code_base)
#gdb.execute('set solib-search-path ' + out_sp)
#gdb.execute('set sysroot ' + out_symbol)
#gdb.execute('file bin')
#gdb.execute('sharelibrary libc.so')
#gdb.execute('sharelibrary bin')

