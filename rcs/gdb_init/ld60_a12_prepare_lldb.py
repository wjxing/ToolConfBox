#!/usr/bin/env python

import lldb
import os

code_base  = os.environ['HOME'] + '/Workspace/Code/android/12/android-12-dev-ld60'
out_prefix = 'out/target/product/tv_e1_dtmb'
out_symbol = code_base + '/' + out_prefix + '/symbols'
out_symbol = os.environ['HOME'] + '/Workspace/Log/LD60/Jira/LDP-8916/sym' + '/symbols'
out_sp_arr = [
        '/system/bin', '/system/bin/hw', '/system/lib64', '/system/lib64/hw', '/system/lib', '/system/lib/hw',
        '/vendor/bin', '/vendor/bin/hw', '/vendor/lib64', '/vendor/lib64/hw', '/vendor/lib', '/vendor/lib/hw',
        '/apex/com.android.runtime/bin', '/apex/com.android.runtime/lib64', '/apex/com.android.runtime/lib',
        '/system/lib64/ssl/engines', '/system/lib/ssl/engines',
        '/system/lib64/drm', '/system/lib/drm',
        '/system/lib64/egl', '/system/lib/egl',
        '/system/lib64/soundfx', '/system/lib/soundfx',
        '/vendor/lib64/egl', '/vendor/lib/egl',
        ]
out_sp     = ' '.join(list(out_symbol + i for i in out_sp_arr))

def __lldb_init_module(debugger, internal_dict):
    res = lldb.SBCommandReturnObject()
    ci = debugger.GetCommandInterpreter()

    ci.HandleCommand("platform select remote-android", res)
    ci.HandleCommand("target modules search-paths add / " + out_symbol, res)
    #ci.HandleCommand("settings append target.exec-search-paths " + out_sp, res)
    ci.HandleCommand("settings set target.inherit-env false", res)

