import lldb

def my_first_command(debugger, command, result, internal_dict):    
    print("Hello world!")

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f helloworld.my_first_command first_cmd')
