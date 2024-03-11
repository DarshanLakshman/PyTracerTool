# PyTracerTool Module

Welcome to the PyTracerTool Module! This module provides a versatile tool, PyTracerTool, for tracing the execution of Python code, capturing variable changes, and logging print statements. PyTracerTool helps you gain insights into the sequence of code execution, variable values, and output generated during runtime.

## Features

* Trace the execution order of Python code.
* Capture variable changes during code execution.
* Log print statements and associate them with line numbers.
* Generate a formatted trace table for analysis.

## Installation

You can install PyTracerTool via pip:

```bash
pip install pytracertool
```

## Website

Please have a look at a website I developed, which takes Python code as an input and allows you to step through the program - https://tracetableproject.pythonanywhere.com/ 

<<<<<<< HEAD
## Python Documentation

Help on built-in module sys:

NAME
    sys

MODULE REFERENCE
    https://docs.python.org/3.10/library/sys.html
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides access to some objects used or maintained by the
    interpreter and to functions that interact strongly with the interpreter.
    
    Dynamic objects:
    
    argv -- command line arguments; argv[0] is the script pathname if known
    path -- module search path; path[0] is the script directory, else ''
    modules -- dictionary of loaded modules
    
    displayhook -- called to show results in an interactive session
    excepthook -- called to handle any uncaught exception other than SystemExit
      To customize printing in an interactive session or to install a custom
      top-level exception handler, assign other functions to replace these.
    
    stdin -- standard input file object; used by input()
    stdout -- standard output file object; used by print()
    stderr -- standard error object; used for error messages
      By assigning other file objects (or objects that behave like files)
      to these, it is possible to redirect all of the interpreter's I/O.
    
    last_type -- type of last uncaught exception
    last_value -- value of last uncaught exception
    last_traceback -- traceback of last uncaught exception
      These three are only available in an interactive session after a
      traceback has been printed.
    
    Static objects:
    
    builtin_module_names -- tuple of module names built into this interpreter
    copyright -- copyright notice pertaining to this interpreter
    exec_prefix -- prefix used to find the machine-specific Python library
    executable -- absolute path of the executable binary of the Python interpreter
    float_info -- a named tuple with information about the float implementation.
    float_repr_style -- string indicating the style of repr() output for floats
    hash_info -- a named tuple with information about the hash algorithm.
    hexversion -- version information encoded as a single integer
    implementation -- Python implementation information.
    int_info -- a named tuple with information about the int implementation.
    maxsize -- the largest supported length of containers.
    maxunicode -- the value of the largest Unicode code point
    platform -- platform identifier
    prefix -- prefix used to find the Python library
    thread_info -- a named tuple with information about the thread implementation.
    version -- the version of this interpreter as a string
    version_info -- version information as a named tuple
    __stdin__ -- the original stdin; don't touch!
    __stdout__ -- the original stdout; don't touch!
    __stderr__ -- the original stderr; don't touch!
    __displayhook__ -- the original displayhook; don't touch!
    __excepthook__ -- the original excepthook; don't touch!
    
    Functions:
    
    displayhook() -- print an object to the screen, and save it in builtins._
    excepthook() -- print an exception and its traceback to sys.stderr
    exc_info() -- return thread-safe information about the current exception
    exit() -- exit the interpreter by raising SystemExit
    getdlopenflags() -- returns flags to be used for dlopen() calls
    getprofile() -- get the global profiling function
    getrefcount() -- return the reference count for an object (plus one :-)
    getrecursionlimit() -- return the max recursion depth for the interpreter
    getsizeof() -- return the size of an object in bytes
    gettrace() -- get the global debug tracing function
    setdlopenflags() -- set the flags to be used for dlopen() calls
    setprofile() -- set the global profiling function
    setrecursionlimit() -- set the max recursion depth for the interpreter
    settrace() -- set the global debug tracing function

FUNCTIONS
    __breakpointhook__ = breakpointhook(...)
        breakpointhook(*args, **kws)
        
        This hook function is called by built-in breakpoint().
    
    __displayhook__ = displayhook(object, /)
        Print an object to sys.stdout and also save it in builtins._
    
    __excepthook__ = excepthook(exctype, value, traceback, /)
        Handle an exception by displaying it with a traceback on sys.stderr.
    
    __unraisablehook__ = unraisablehook(unraisable, /)
        Handle an unraisable exception.
        
        The unraisable argument has the following attributes:
        
        * exc_type: Exception type.
        * exc_value: Exception value, can be None.
        * exc_traceback: Exception traceback, can be None.
        * err_msg: Error message, can be None.
        * object: Object causing the exception, can be None.
    
    addaudithook(hook)
        Adds a new audit hook callback.
    
    audit(...)
        audit(event, *args)
        
        Passes the event to any audit hooks that are attached.
    
    breakpointhook(...)
        breakpointhook(*args, **kws)
        
        This hook function is called by built-in breakpoint().
    
    call_tracing(func, args, /)
        Call func(*args), while tracing is enabled.
        
        The tracing state is saved, and restored afterwards.  This is intended
        to be called from a debugger from a checkpoint, to recursively debug
        some other code.
    
    displayhook(object, /)
        Print an object to sys.stdout and also save it in builtins._
    
    exc_info()
        Return current exception information: (type, value, traceback).
        
        Return information about the most recent exception caught by an except
        clause in the current stack frame or in an older stack frame.
    
    excepthook(exctype, value, traceback, /)
        Handle an exception by displaying it with a traceback on sys.stderr.
    
    exit(status=None, /)
        Exit the interpreter by raising SystemExit(status).
        
        If the status is omitted or None, it defaults to zero (i.e., success).
        If the status is an integer, it will be used as the system exit status.
        If it is another kind of object, it will be printed and the system
        exit status will be one (i.e., failure).
    
    get_asyncgen_hooks()
        Return the installed asynchronous generators hooks.
        
        This returns a namedtuple of the form (firstiter, finalizer).
    
    get_coroutine_origin_tracking_depth()
        Check status of origin tracking for coroutine objects in this thread.
    
    getallocatedblocks()
        Return the number of memory blocks currently allocated.
    
    getdefaultencoding()
        Return the current default encoding used by the Unicode implementation.
    
    getdlopenflags()
        Return the current value of the flags that are used for dlopen calls.
        
        The flag constants are defined in the os module.
    
    getfilesystemencodeerrors()
        Return the error mode used Unicode to OS filename conversion.
    
    getfilesystemencoding()
        Return the encoding used to convert Unicode filenames to OS filenames.
    
    getprofile()
        Return the profiling function set with sys.setprofile.
        
        See the profiler chapter in the library manual.
    
    getrecursionlimit()
        Return the current value of the recursion limit.
        
        The recursion limit is the maximum depth of the Python interpreter
        stack.  This limit prevents infinite recursion from causing an overflow
        of the C stack and crashing Python.
    
    getrefcount(object, /)
        Return the reference count of object.
        
        The count returned is generally one higher than you might expect,
        because it includes the (temporary) reference as an argument to
        getrefcount().
    
    getsizeof(...)
        getsizeof(object [, default]) -> int
        
        Return the size of object in bytes.
    
    getswitchinterval()
        Return the current thread switch interval; see sys.setswitchinterval().
    
    gettrace()
        Return the global debug tracing function set with sys.settrace.
        
        See the debugger chapter in the library manual.
    
    intern(string, /)
        ``Intern'' the given string.
        
        This enters the string in the (global) table of interned strings whose
        purpose is to speed up dictionary lookups. Return the string itself or
        the previously interned string object with the same value.
    
    is_finalizing()
        Return True if Python is exiting.
    
    set_asyncgen_hooks(...)
        set_asyncgen_hooks(* [, firstiter] [, finalizer])
        
        Set a finalizer for async generators objects.
    
    set_coroutine_origin_tracking_depth(depth)
        Enable or disable origin tracking for coroutine objects in this thread.
        
        Coroutine objects will track 'depth' frames of traceback information
        about where they came from, available in their cr_origin attribute.
        
        Set a depth of 0 to disable.
    
    setdlopenflags(flags, /)
        Set the flags used by the interpreter for dlopen calls.
        
        This is used, for example, when the interpreter loads extension
        modules. Among other things, this will enable a lazy resolving of
        symbols when importing a module, if called as sys.setdlopenflags(0).
        To share symbols across extension modules, call as
        sys.setdlopenflags(os.RTLD_GLOBAL).  Symbolic names for the flag
        modules can be found in the os module (RTLD_xxx constants, e.g.
        os.RTLD_LAZY).
    
    setprofile(...)
        setprofile(function)
        
        Set the profiling function.  It will be called on each function call
        and return.  See the profiler chapter in the library manual.
    
    setrecursionlimit(limit, /)
        Set the maximum depth of the Python interpreter stack to n.
        
        This limit prevents infinite recursion from causing an overflow of the C
        stack and crashing Python.  The highest possible limit is platform-
        dependent.
    
    setswitchinterval(interval, /)
        Set the ideal thread switching delay inside the Python interpreter.
        
        The actual frequency of switching threads can be lower if the
        interpreter executes long sequences of uninterruptible code
        (this is implementation-specific and workload-dependent).
        
        The parameter must represent the desired switching delay in seconds
        A typical value is 0.005 (5 milliseconds).
    
    settrace(...)
        settrace(function)
        
        Set the global debug tracing function.  It will be called on each
        function call.  See the debugger chapter in the library manual.
    
    unraisablehook(unraisable, /)
        Handle an unraisable exception.
        
        The unraisable argument has the following attributes:
        
        * exc_type: Exception type.
        * exc_value: Exception value, can be None.
        * exc_traceback: Exception traceback, can be None.
        * err_msg: Error message, can be None.
        * object: Object causing the exception, can be None.

DATA
    __stderr__ = <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf...
    __stdin__ = <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8...
    __stdout__ = <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf...
    abiflags = ''
    api_version = 1013
    argv = ['/Users/darshanl/Documents/pyTracerModule/PyTracerTool/x.py']
    base_exec_prefix = '/Library/Frameworks/Python.framework/Versions/3.10...
    base_prefix = '/Library/Frameworks/Python.framework/Versions/3.10'
    builtin_module_names = ('_abc', '_ast', '_codecs', '_collections', '_f...
    byteorder = 'little'
    copyright = 'Copyright (c) 2001-2021 Python Software Foundati...ematis...
    dont_write_bytecode = False
    exec_prefix = '/Library/Frameworks/Python.framework/Versions/3.10'
    executable = '/usr/local/bin/python3'
    flags = sys.flags(debug=0, inspect=0, interactive=0, opt...mode=False,...
    float_info = sys.float_info(max=1.7976931348623157e+308, max_...epsilo...
    float_repr_style = 'short'
    hash_info = sys.hash_info(width=64, modulus=2305843009213693...iphash2...
    hexversion = 50987248
    implementation = namespace(name='cpython', cache_tag='cpython-310...ia...
    int_info = sys.int_info(bits_per_digit=30, sizeof_digit=4)
    maxsize = 9223372036854775807
    maxunicode = 1114111
    meta_path = [<_distutils_hack.DistutilsMetaFinder object>, <class '_fr...
    modules = {'__main__': <module '__main__' from '/Users/darshanl/Docume...
    orig_argv = ['/Library/Frameworks/Python.framework/Versions/3.10/Resou...
    path = ['/Users/darshanl/Documents/pytracermodule/PyTracerTool', '/Lib...
    path_hooks = [<class 'zipimport.zipimporter'>, <function FileFinder.pa...
    path_importer_cache = {'/Library/Frameworks/Python.framework/Versions/...
    platform = 'darwin'
    platlibdir = 'lib'
    prefix = '/Library/Frameworks/Python.framework/Versions/3.10'
    pycache_prefix = None
    stderr = <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
    stdin = <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>
    stdlib_module_names = frozenset({'__future__', '_abc', '_aix_support',...
    stdout = <_io.TextIOWrapper name='help_output.txt' mode='w' encoding='...
    thread_info = sys.thread_info(name='pthread', lock='mutex+cond', versi...
    version = '3.10.0 (v3.10.0:b494f5935c, Oct  4 2021, 14:59:19) [Clang 1...
    version_info = sys.version_info(major=3, minor=10, micro=0, releaselev...
    warnoptions = []

FILE
    (built-in)




=======
>>>>>>> 85da39925a91bfe393b794bfa7d4152c2b724d17
## License

MIT License
