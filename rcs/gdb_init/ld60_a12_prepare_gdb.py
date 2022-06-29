#!/usr/bin/env python

import gdb
import os

code_base  = os.environ['HOME'] + '/Workspace/Code/android/12/android-12-dev-ld60'
out_prefix = 'out/target/product/tv_e1_dtmb'
out_symbol = code_base + '/' + out_prefix + '/symbols'
out_symbol = os.environ['HOME'] + '/Workspace/Log/LD60/Jira/LDP-8916/sym' + '/symbols'
out_sp_arr = [
        '/system/bin', '/system/bin/hw', '/system/lib64', '/system/lib64/hw', '/system/lib', '/system/lib/hw',
        '/vendor/bin', '/vendor/bin/hw', '/vendor/lib64', '/vendor/lib64/hw', '/vendor/lib', '/vendor/lib/hw',
        '/apex/com.android.runtime/bin', '/apex/com.android.runtime/lib64', '/apex/com.android.runtime/lib'
        '/system/lib64/ssl/engines', '/system/lib/ssl/engines',
        '/system/lib64/drm', '/system/lib/drm',
        '/system/lib64/egl', '/system/lib/egl',
        '/system/lib64/soundfx', '/system/lib/soundfx',
        '/vendor/lib64/egl', '/vendor/lib/egl',
        ]
out_sp     = ":".join(list(out_symbol + i for i in out_sp_arr))

gdb.execute('set osabi GNU/Linux')
gdb.execute('set architecture arm')
gdb.execute('set auto-solib-add on')
gdb.execute('set print thread-events on')
#gdb.execute('set set scheduler-locking on')
gdb.execute('set print pretty on')
gdb.execute('dir ' + code_base)
gdb.execute('set solib-search-path ' + out_sp)
gdb.execute('set sysroot ' + out_symbol)
#gdb.execute('file bin')
#gdb.execute('sharelibrary libc.so')
#gdb.execute('sharelibrary bin')

