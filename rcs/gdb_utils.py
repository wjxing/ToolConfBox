import gdb

class PluginAdd(gdb.Command):

    def __init__(self):
        super (PluginAdd, self).__init__ ('PluginAdd', gdb.COMMAND_DATA)

    def invoke(self, arg, from_tty):
        argv = gdb.string_to_argv(arg)
        if len(argv) != 1:
            raise gdb.GdbError('PluginAdd takes exactly 1 argument.')

        toolbox = '~/Workspace/ToolBox'
        if argv[0] == "gef":
            gdb.execute("source {}/source/debug/gdb/gef/gef.py".format(toolbox))
        elif argv[0] == "db":
            gdb.execute("source {}/source/debug/gdb/gdb-dashboard/.gdbinit".format(toolbox))

class Offsets(gdb.Command):

    def __init__(self):
        super (Offsets, self).__init__ ('offsets-of', gdb.COMMAND_DATA)

    def invoke(self, arg, from_tty):
        argv = gdb.string_to_argv(arg)
        if len(argv) != 1:
            raise gdb.GdbError('offsets-of takes exactly 1 argument.')

        stype = gdb.lookup_type('struct %s' % argv[0])

        print(argv[0] + '{')
        for field in stype.fields():
            print('    [0x%x] %s' % (field.bitpos//8, field.name))
        print('}')

PluginAdd()
Offsets()
