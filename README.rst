PyTracerTool Module
===================

Welcome to the PyTracerTool Module! This module provides a versatile
tool, PyTracerTool, for tracing the execution of Python code, capturing
variable changes, and logging print statements. PyTracerTool helps you
gain insights into the sequence of code execution, variable values, and
output generated during runtime.

Features
--------

-  Trace the execution order of Python code.
-  Capture variable changes during code execution.
-  Log print statements and associate them with line numbers.
-  Generate a formatted trace table for analysis.

Installation
------------

You can install PyTracerTool via pip:

.. code:: bash

   pip install pytracertool

To import this module, you must do ``import PyTracerTool``

Website
-------

Please have a look at a website I developed, which takes Python code as
an input and allows you to step through the program -
https://tracetableproject.pythonanywhere.com/

<<<<<<< HEAD

Python Documentation
--------------------

Help on module pytracertool:

NAME pytracertool - Welcome to the PyTracerTool Module

DESCRIPTION This module provides a versatile tool, PyTracerTool, for
tracing the execution of Python code, capturing variable changes, and
logging print statements. PyTracerTool helps you gain insights into the
sequence of code execution, variable values, and output generated during
runtime.

::

   Version: 1.0.0

   Classes:
       - OutputLogger: A utility class used for capturing and logging output produced by print statements.
       - CodeTracer: The main class that enables tracing and capturing code execution, variable changes, and print outputs.

   Usage:
       To use the PyTracerTool module, instantiate the CodeTracer class with the Python code you want to trace. You can then use
       the provided methods to capture and analyze the execution order, variable values, and print outputs.

   Author:
       Darshan Lakshman

   Disclaimer:
       This module is intended for educational purposes and code analysis. It may not cover all edge cases and situations.

CLASSES builtins.object CodeTracer OutputLogger

::

   class CodeTracer(builtins.object)
    |  CodeTracer(python_code: str)
    |  
    |  CodeTracer provides a versatile tool for tracing code execution, capturing variable changes, and logging print outputs.
    |  
    |  This class enables tracing the execution of Python code, capturing variable changes, and logging print outputs
    |  for later analysis. It offers methods to trace the execution order, capture variable values, and generate a formatted
    |  trace table that displays the sequence of code execution, variable changes, and print outputs.
    |  
    |  Methods:
    |      __init__(python_code): Initialize a new instance of CodeTracer with the provided Python code.
    |      __str__(): Returns the trace table in a string format
    |      format_code_for_tracing(): Format the Python code for tracing by encapsulating it in a main() function.
    |      capture_print_statements(): Capture print outputs during code execution and associate them with line numbers.
    |      trace_lines(): Trace and record the order in which lines are executed.
    |      variables_tracer(): Trace and record the changes in variable values during code execution.
    |      generate_trace_table(): Trace execution order, variable changes, and print outputs to generate a trace table.
    |  
    |  Attributes:
    |      code: The Python code to be traced.
    |      execution_order: A list to store the order in which lines of code are executed.
    |      tracer_info: A list to store information about variable values during execution.
    |      trace_table: A list to store a formatted trace table.
    |      calls_log: A list to log function calls during execution.
    |      output_lines: A dictionary to store captured print statement outputs.
    |      context: A dictionary to store the execution context.
    |  
    |  Methods defined here:
    |  
    |  __init__(self, python_code: str)
    |      Initialize a new instance of CodeTracer.
    |      
    |      :param python_code: The Python code to be traced.
    |      :type python_code: str
    |      
    |      :note:
    |          This constructor initializes an instance of the CodeTracer class with the provided Python code.
    |          The code will be traced to capture execution order, variable values, and print outputs.
    |  
    |  __str__(self) -> str
    |      Generate a formatted trace table for display.
    |      
    |      This method generates a formatted trace table from the captured information
    |      about code execution, variable changes, and print outputs. It uses the tabulate
    |      library to create a grid representation of the trace table and returns it as a string.
    |      
    |      :param self: The instance of the class.
    |      :return: Formatted trace table as a string.
    |      :rtype: str
    |      
    |      :Example:
    |          Suppose you have an instance of the CodeTracer class and have already
    |          generated a trace table using the generate_trace_table method:
    |      
    |          ```python
    |          example_code = '''
    |          x = 1
    |          y = 1
    |          x = x + y
    |          print(x)
    |          tracer = CodeTracer(example_code)
    |          tracer.generate_trace_table()
    |          trace_table_str = str(tracer)
    |          print(trace_table_str)
    |          ```
    |      
    |          The trace_table_str will contain a formatted table as a string, which you can print:
    |      
    |      
    |      :seealso: generate_trace_table
    |  
    |  capture_print_statements(self) -> dict
    |              Capture and associate print statements with line numbers during code execution.
    |      
    |              This method captures the output of print statements generated during the execution
    |              of the provided code. The captured output is associated with the line numbers in the
    |              code where the print statements occurred. It achieves this by temporarily redirecting
    |              the standard output stream to an instance of OutputLogger, which logs the output along
    |              with the corresponding line numbers.
    |      
    |              :param self: The instance of the class.
    |              :return: A dictionary mapping line numbers to captured output text.
    |              :rtype: dict
    |      
    |              :Example:
    |                  Capturing print statements and their associated line numbers:
    |      
    |                  ```python
    |                  example_code = "print('Hello, World!')
    |      print('Line 2 output')"
    |                  tracer = CodeTracer(example_code)
    |                  output_lines = tracer.capture_print_statements()
    |                  print(output_lines)
    |                  ```
    |      
    |                  The output_lines dictionary will contain:
    |                  ```
    |                  {
    |                      '1': 'Hello, World!',
    |                      '2': 'Line 2 output'
    |                  }
    |  
    |  format_code_for_tracing(self) -> str
    |      Formats the Python code, so that it can be traced.
    |      
    |      :param self: The instance of the class.
    |      :return: Formatted code provided by user; code provided by user placed inside a main() def
    |      :rtype: str
    |      
    |      :note:
    |          - This method puts all of the code given into a function called main(), by indenting all the lines by 1 tab
    |          - It also adds a line called _finished = True at the end of the method, because the trace functions only
    |            work until the second to last line.
    |      
    |      :example:
    |      
    |          This is an example of how to use this method:
    |      
    |              code = '''a = 1
    |              b = 1
    |              c = a + b'''
    |      
    |              python_code = CodeTracer(code)
    |              python_code.format_code_for_tracing()
    |      
    |          The result would be:
    |      
    |              def main()
    |                  a = 1
    |                  b = 1
    |                  c = a + b
    |                  _finished = True
    |  
    |  generate_trace_table(self)
    |      Trace the execution order and capture variable values and print outputs.
    |      
    |      This method traces the execution order of lines in the provided code and captures
    |      the values of variables at each step. It creates a table that displays variable values,
    |      print outputs, and the execution order.
    |      
    |      :param self: The instance of the class.
    |      
    |      :note:
    |          This method builds upon the `trace_lines` method to track the execution order
    |          and captures print outputs using `capture_print_statements`. It then prepares
    |          the code for execution by formatting it and appending a call to `main()`.
    |          The `variables_tracer` tracing mechanism is set up using `sys.settrace`, and
    |          the formatted code is executed. After execution is complete, the tracing function
    |          is unset using `sys.settrace(None)`.
    |      
    |      :return: None
    |      
    |      :Example:
    |          # Define an instance of CodeTracer and example code
    |          example_code = '''
    |          x = 10
    |          print("Value of x:", x)
    |          y = x + 5
    |          print("Value of y:", y)
    |          '''
    |          tracer = CodeTracer(example_code)
    |      
    |          # Trace variables and print captured trace table
    |          tracer.trace_variables()
    |          trace_table = tracer.trace_table
    |      
    |          # Print the formatted trace table
    |          print(tracer)
    |      
    |          Running the example will display a table with variable values, outputs, and execution order:
    |      
    |          Trace Table:
    |          +-------+----+----+-------------------+
    |          | Line  | x  | y  | OUTPUT            |
    |          +-------+----+----+-------------------+
    |          | 2     | 10 |    | Value of x: 10    |
    |          | 3     | 10 | 15 | Value of y: 15    |
    |          +-------+----+----+-------------------+
    |      
    |      :seealso: trace_lines, capture_print_statements, format_code_for_tracing, variables_tracer
    |  
    |  lines_tracer(self, frame: frame, event: str, arg: Any) -> Optional[Callable[[frame, str, Any], Optional[Callable]]]
    |      Trace function to monitor the execution order of lines.
    |      
    |      This trace function is used to monitor and record the order in which lines of code are executed.
    |      It appends the line number of each executed line to the `execution_order` list, capturing the
    |      sequential execution order for later analysis.
    |      
    |      :param self: The instance of the class.
    |      :param frame: The current frame being executed.
    |      :type frame: types.FrameType
    |      :param event: The event type, such as 'call', 'line', 'return', etc.
    |      :type event: str
    |      :param arg: Additional event information.
    |      :type arg: typing.Any
    |      :return: The next trace function to use, or None to stop tracing.
    |      :rtype: typing.Optional[typing.Callable[[types.FrameType, str, typing.Any], typing.Optional[typing.Callable]]]
    |      
    |      :Example:
    |          Tracing and recording the execution order of code lines:
    |      
    |          ```python
    |          tracer = CodeTracer(example_code)
    |          sys.settrace(tracer.lines_tracer)
    |          tracer.trace_lines()  # This populates tracer.execution_order
    |          sys.settrace(None)
    |          print(tracer.execution_order)  # Print the recorded execution order
    |          ```
    |      
    |          The `execution_order` list will contain the line numbers in the order they were executed.
    |  
    |  trace_lines(self)
    |      Gets the order in which the lines are executed
    |      
    |      :param self: The instance of the class.
    |      
    |      :note:
    |          This method sets up a tracing mechanism using `sys.settrace` to track the execution
    |          order of lines within the provided code. It populates the `execution_order` list with
    |          line numbers in the order they are executed. After tracing is complete, the tracing
    |          function is unset using `sys.settrace(None)`.
    |      
    |      :example:
    |          Suppose we have an instance of the CodeTracer class and want to trace the execution order
    |          of the following example code:
    |      
    |          ```python
    |          example_code = '''
    |          x = 10
    |          print("Value of x:", x)
    |          y = x + 5
    |          print("Value of y:", y)
    |          '''
    |      
    |          tracer = CodeTracer(example_code)
    |          tracer.trace_lines()
    |          print("Execution Order:", tracer.execution_order)
    |      
    |          The output will show the order in which the lines were executed:
    |      
    |          '''
    |          Value of x: 10
    |          Value of y: 15
    |          Execution Order: [2, 3, 4, 5]
    |          '''
    |      
    |          :return: None
    |  
    |  variables_tracer(self, frame: frame, event: str, arg: Any) -> Optional[Callable[[frame, str, Any], Optional[Callable]]]
    |      Trace function to monitor and trace the changes in variable values.
    |      
    |      This trace function is used to monitor and record the changes in variable values during code execution.
    |      It captures the values of local variables in the current frame and logs them along with the function name.
    |      The recorded information is then used to build a trace table that displays the values of variables as they
    |      change during the execution of the code.
    |      
    |      :param self: The instance of the class.
    |      :param frame: The current frame being executed.
    |      :type frame: types.FrameType
    |      :param event: The event type, such as 'call', 'line', 'return', etc.
    |      :type event: str
    |      :param arg: Additional event information.
    |      :type arg: typing.Any
    |      :return: The next trace function to use, or None to stop tracing.
    |      :rtype: typing.Optional[typing.Callable[[types.FrameType, str, typing.Any], typing.Optional[typing.Callable]]]
    |      
    |      :Example:
    |          Tracing and recording changes in variable values during code execution:
    |      
    |          ```python
    |          tracer = CodeTracer(example_code)
    |          sys.settrace(tracer.variables_tracer)
    |          tracer.trace_variables()  # This populates tracer.tracer_info with variable values
    |          sys.settrace(None)
    |          print(tracer.tracer_info)  # Print the recorded variable values
    |          ```
    |      
    |          The `tracer_info` list will contain dictionaries representing variable changes in each line.
    |  
    |  ----------------------------------------------------------------------
    |  Data descriptors defined here:
    |  
    |  __dict__
    |      dictionary for instance variables (if defined)
    |  
    |  __weakref__
    |      list of weak references to the object (if defined)

   class OutputLogger(builtins.object)
    |  OutputLogger captures and logs the output produced by print statements during code execution.
    |  
    |  This class is used to capture the output of print statements generated during the execution
    |  of the provided code. The captured output is associated with the line numbers in the code
    |  where the print statements occurred. It achieves this by temporarily redirecting the standard
    |  output stream to an instance of OutputLogger, which logs the output along with the corresponding
    |  line numbers.
    |  
    |  Methods:
    |      __init__(): Initialises an instance of OutputLogger
    |      write(text): Log the provided text along with the current line number.
    |      flush(): Placeholder method; no action is taken.
    |  
    |  Attributes:
    |      output_lines: A dictionary mapping line numbers to captured output text.
    |                    Keys represent line numbers, and values represent the corresponding output.
    |  
    |  Methods defined here:
    |  
    |  __init__(self)
    |      Initialize a new instance of OutputLogger.
    |      
    |      :param self: The instance of the class.
    |  
    |  flush(self)
    |      Placeholder method - no action is taken.
    |      
    |      :param self: The instance of the class.
    |      :return: None
    |  
    |  write(self, text: str)
    |      Log the provided text along with the current line number.
    |      
    |      :param self: The instance of the class.
    |      :param text: The text to be logged.
    |      :type text: str
    |      :return: None
    |  
    |  ----------------------------------------------------------------------
    |  Data descriptors defined here:
    |  
    |  __dict__
    |      dictionary for instance variables (if defined)
    |  
    |  __weakref__
    |      list of weak references to the object (if defined)

DATA ANY_TYPE = typing.Any Special type indicating an unconstrained
type.

::

       - Any is compatible with every type.
       - Any assumed to have all methods.
       - All values assumed to be instances of Any.
       
       Note that all the above statements are true from the point of view of
       static type checkers. At runtime, Any should not be used with instance
       or class checks.

   TRACER_RETURN_TYPE = typing.Optional[typing.Callable[[frame, str, typi...

License
-------

MIT License
