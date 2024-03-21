

"""
Welcome to the PyTracerTool Module

This module provides a versatile tool, PyTracerTool, for tracing the execution of Python code, capturing variable changes,
and logging print statements. PyTracerTool helps you gain insights into the sequence of code execution, variable values, and
output generated during runtime.

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

"""

import sys
import copy
import tabulate
import types
import typing
import io

TRACER_RETURN_TYPE = typing.Optional[
    typing.Callable[
        [types.FrameType, str, typing.Any], typing.Optional[typing.Callable]
    ]
]
FRAME_TYPE = types.FrameType
ANY_TYPE = typing.Any


class OutputLogger(object):
    """
    OutputLogger captures and logs the output produced by print statements during code execution.

    This class is used to capture the output of print statements generated during the execution
    of the provided code. The captured output is associated with the line numbers in the code
    where the print statements occurred. It achieves this by temporarily redirecting the standard
    output stream to an instance of OutputLogger, which logs the output along with the corresponding
    line numbers.

    Methods:
        __init__(): Initialises an instance of OutputLogger
        write(text): Log the provided text along with the current line number.
        flush(): Placeholder method; no action is taken.

    Attributes:
        output_lines: A dictionary mapping line numbers to captured output text.
                      Keys represent line numbers, and values represent the corresponding output.
    """

    def __init__(self):
        """
        Initialize a new instance of OutputLogger.

        :param self: The instance of the class.
        """
        self.output_lines = {}

    def write(self, text:str):
        """
        Log the provided text along with the current line number.

        :param self: The instance of the class.
        :param text: The text to be logged.
        :type text: str
        :return: None
        """

        frame = sys._getframe(1)
        line_number = frame.f_lineno

        if str(line_number) in self.output_lines:
            self.output_lines[str(line_number)] += str(text)
        else:
            self.output_lines[str(line_number)] = str(text)


    def flush(self):
        """
        Placeholder method - no action is taken.

        :param self: The instance of the class.
        :return: None
        """
        pass


class CodeTracer(object):
    """
    CodeTracer provides a versatile tool for tracing code execution, capturing variable changes, and logging print outputs.

    This class enables tracing the execution of Python code, capturing variable changes, and logging print outputs
    for later analysis. It offers methods to trace the execution order, capture variable values, and generate a formatted
    trace table that displays the sequence of code execution, variable changes, and print outputs.

    Methods:
        __init__(python_code): Initialize a new instance of CodeTracer with the provided Python code.
        __str__(): Returns the trace table in a string format
        format_code_for_tracing(): Format the Python code for tracing by encapsulating it in a main() function.
        capture_print_statements(): Capture print outputs during code execution and associate them with line numbers.
        trace_lines(): Trace and record the order in which lines are executed.
        variables_tracer(): Trace and record the changes in variable values during code execution.
        generate_trace_table(): Trace execution order, variable changes, and print outputs to generate a trace table.

    Attributes:
        code: The Python code to be traced.
        execution_order: A list to store the order in which lines of code are executed.
        tracer_info: A list to store information about variable values during execution.
        trace_table: A list to store a formatted trace table.
        calls_log: A list to log function calls during execution.
        output_lines: A dictionary to store captured print statement outputs.
        context: A dictionary to store the execution context.
    """

    def __init__(self, python_code: str, user_input: str):
        """
        Initialize a new instance of CodeTracer.

        :param python_code: The Python code to be traced.
        :type python_code: str

        :note:
            This constructor initializes an instance of the CodeTracer class with the provided Python code.
            The code will be traced to capture execution order, variable values, and print outputs.

        """

        self.code = python_code
        self.execution_order = []
        self.tracer_info = []
        self.trace_table = []
        self.calls_log = []
        self.output_lines = []
        self.context = {}
        self.user_input = user_input

    def __str__(self) -> str:
        """
        Generate a formatted trace table for display.

        This method generates a formatted trace table from the captured information
        about code execution, variable changes, and print outputs. It uses the tabulate
        library to create a grid representation of the trace table and returns it as a string.

        :param self: The instance of the class.
        :return: Formatted trace table as a string.
        :rtype: str

        :Example:
            Suppose you have an instance of the CodeTracer class and have already
            generated a trace table using the generate_trace_table method:

            ```python
            example_code = '''
            x = 1
            y = 1
            x = x + y
            print(x)
            tracer = CodeTracer(example_code)
            tracer.generate_trace_table()
            trace_table_str = str(tracer)
            print(trace_table_str)
            ```

            The trace_table_str will contain a formatted table as a string, which you can print:


        :seealso: generate_trace_table
        """

        return tabulate.tabulate(self.trace_table, headers="firstrow", tablefmt="grid")

    def format_code_for_tracing(self) -> str:
        """
        Formats the Python code, so that it can be traced.

        :param self: The instance of the class.
        :return: Formatted code provided by user; code provided by user placed inside a main() def
        :rtype: str

        :note:
            - This method puts all of the code given into a function called main(), by indenting all the lines by 1 tab
            - It also adds a line called _finished = True at the end of the method, because the trace functions only
              work until the second to last line.

        :example:

            This is an example of how to use this method:

                code = '''a = 1
                b = 1
                c = a + b'''

                python_code = CodeTracer(code)
                python_code.format_code_for_tracing()

            The result would be:

                def main()
                    a = 1
                    b = 1
                    c = a + b
                    _finished = True

        """

        lines = ["\t" + line for line in self.code.split("\n")]
        code_start = "def main():\n"

        return code_start + "\n".join(lines) + "\n\t" + "_finished = True"

    def lines_tracer(
        self, frame: FRAME_TYPE, event: str, arg: ANY_TYPE
    ) -> TRACER_RETURN_TYPE:
        """
        Trace function to monitor the execution order of lines.

        This trace function is used to monitor and record the order in which lines of code are executed.
        It appends the line number of each executed line to the `execution_order` list, capturing the
        sequential execution order for later analysis.

        :param self: The instance of the class.
        :param frame: The current frame being executed.
        :type frame: types.FrameType
        :param event: The event type, such as 'call', 'line', 'return', etc.
        :type event: str
        :param arg: Additional event information.
        :type arg: typing.Any
        :return: The next trace function to use, or None to stop tracing.
        :rtype: typing.Optional[typing.Callable[[types.FrameType, str, typing.Any], typing.Optional[typing.Callable]]]

        :Example:
            Tracing and recording the execution order of code lines:

            ```python
            tracer = CodeTracer(example_code)
            sys.settrace(tracer.lines_tracer)
            tracer.trace_lines()  # This populates tracer.execution_order
            sys.settrace(None)
            print(tracer.execution_order)  # Print the recorded execution order
            ```

            The `execution_order` list will contain the line numbers in the order they were executed.
        """

        if event == "line":
            line_num = frame.f_lineno
            self.execution_order.append(line_num)
        return self.lines_tracer

    def variables_tracer(
        self, frame: FRAME_TYPE, event: str, arg: ANY_TYPE
    ) -> TRACER_RETURN_TYPE:
        """
        Trace function to monitor and trace the changes in variable values.

        This trace function is used to monitor and record the changes in variable values during code execution.
        It captures the values of local variables in the current frame and logs them along with the function name.
        The recorded information is then used to build a trace table that displays the values of variables as they
        change during the execution of the code.

        :param self: The instance of the class.
        :param frame: The current frame being executed.
        :type frame: types.FrameType
        :param event: The event type, such as 'call', 'line', 'return', etc.
        :type event: str
        :param arg: Additional event information.
        :type arg: typing.Any
        :return: The next trace function to use, or None to stop tracing.
        :rtype: typing.Optional[typing.Callable[[types.FrameType, str, typing.Any], typing.Optional[typing.Callable]]]

        :Example:
            Tracing and recording changes in variable values during code execution:

            ```python
            tracer = CodeTracer(example_code)
            sys.settrace(tracer.variables_tracer)
            tracer.trace_variables()  # This populates tracer.tracer_info with variable values
            sys.settrace(None)
            print(tracer.tracer_info)  # Print the recorded variable values
            ```

            The `tracer_info` list will contain dictionaries representing variable changes in each line.
        """

        if event == "call":
            function_name = frame.f_code.co_name
            self.calls_log.append(f"Calling function: {function_name}")

        elif event == "line":
            local_variables = frame.f_locals
            local_variables_deepcopy = copy.deepcopy(local_variables)


            vars_in_context = {
                f"({frame.f_code.co_name}){var}".replace('<','&lt;').replace('>','&gt;'): (
                    (tabulate.tabulate([vars(value).keys(), vars(value).values()], tablefmt="grid")).replace("\n","<br>")
                    if "object" in str(value) and var != "self"
                    and "_iterator object at 0x" not in str(value)
                    else str(value).replace('<','&lt;').replace('>','&gt;')
                )
                for var, value in local_variables_deepcopy.items()
                if (
                    "<module>" not in frame.f_code.co_name
                    and "function" not in str(value)
                    and not (str(var).startswith("__") and str(var).endswith("__"))
                )
            }

            self.tracer_info.append(copy.deepcopy(vars_in_context))

        return self.variables_tracer

    def trace_lines(self):
        """
        Gets the order in which the lines are executed

        :param self: The instance of the class.

        :note:
            This method sets up a tracing mechanism using `sys.settrace` to track the execution
            order of lines within the provided code. It populates the `execution_order` list with
            line numbers in the order they are executed. After tracing is complete, the tracing
            function is unset using `sys.settrace(None)`.

        :example:
            Suppose we have an instance of the CodeTracer class and want to trace the execution order
            of the following example code:

            ```python
            example_code = '''
            x = 10
            print("Value of x:", x)
            y = x + 5
            print("Value of y:", y)
            '''

            tracer = CodeTracer(example_code)
            tracer.trace_lines()
            print("Execution Order:", tracer.execution_order)

            The output will show the order in which the lines were executed:

            '''
            Value of x: 10
            Value of y: 15
            Execution Order: [2, 3, 4, 5]
            '''

            :return: None
        """

        self.execution_order = []
        sys.settrace(self.lines_tracer)

        input_stream = io.StringIO(self.user_input)

        sys.stdin = input_stream
        exec(self.code)
        sys.settrace(None)

    def capture_print_statements(self) -> dict:
        """
        Capture and associate print statements with line numbers during code execution.

        This method captures the output of print statements generated during the execution
        of the provided code. The captured output is associated with the line numbers in the
        code where the print statements occurred. It achieves this by temporarily redirecting
        the standard output stream to an instance of OutputLogger, which logs the output along
        with the corresponding line numbers.

        :param self: The instance of the class.
        :return: A dictionary mapping line numbers to captured output text.
        :rtype: dict

        :Example:
            Capturing print statements and their associated line numbers:

            ```python
            example_code = "print('Hello, World!')\nprint('Line 2 output')"
            tracer = CodeTracer(example_code)
            output_lines = tracer.capture_print_statements()
            print(output_lines)
            ```

            The output_lines dictionary will contain:
            ```
            {
                '1': 'Hello, World!',
                '2': 'Line 2 output'
            }
        """

        output_logger = OutputLogger()
        original_stdout = sys.stdout

        sys.stdout = output_logger

        input_stream = io.StringIO(self.user_input)

        sys.stdin = input_stream

        exec(self.code)

        sys.stdout = original_stdout

        return output_logger.output_lines

    def generate_trace_table(self):
        """
        Trace the execution order and capture variable values and print outputs.

        This method traces the execution order of lines in the provided code and captures
        the values of variables at each step. It creates a table that displays variable values,
        print outputs, and the execution order.

        :param self: The instance of the class.

        :note:
            This method builds upon the `trace_lines` method to track the execution order
            and captures print outputs using `capture_print_statements`. It then prepares
            the code for execution by formatting it and appending a call to `main()`.
            The `variables_tracer` tracing mechanism is set up using `sys.settrace`, and
            the formatted code is executed. After execution is complete, the tracing function
            is unset using `sys.settrace(None)`.

        :return: None

        :Example:
            # Define an instance of CodeTracer and example code
            example_code = '''
            x = 10
            print("Value of x:", x)
            y = x + 5
            print("Value of y:", y)
            '''
            tracer = CodeTracer(example_code)

            # Trace variables and print captured trace table
            tracer.trace_variables()
            trace_table = tracer.trace_table

            # Print the formatted trace table
            print(tracer)

            Running the example will display a table with variable values, outputs, and execution order:

            Trace Table:
            +-------+----+----+-------------------+
            | Line  | x  | y  | OUTPUT            |
            +-------+----+----+-------------------+
            | 2     | 10 |    | Value of x: 10    |
            | 3     | 10 | 15 | Value of y: 15    |
            +-------+----+----+-------------------+

        :seealso: trace_lines, capture_print_statements, format_code_for_tracing, variables_tracer
        """


        formatted_code = self.format_code_for_tracing()

        formatted_code += "\n" + "main()"
        print(formatted_code)


        sys.settrace(self.variables_tracer)

        input_stream = io.StringIO(self.user_input)

        sys.stdin = input_stream
        exec(formatted_code)
        sys.settrace(None)

        self.trace_lines()

        self.output_lines = self.capture_print_statements()

        variables = set()
        for entry in self.tracer_info:
            variables.update(entry.keys())

        variables = sorted(variables)
        header = ["Line"] + variables + ["OUTPUT"]
        print(self.output_lines)
        self.trace_table = [header]
        for index, entry in enumerate(self.tracer_info[3:]):
            currLine = self.execution_order[index]
            output = ""

            if str(currLine) in self.output_lines:
                output = self.output_lines[str(currLine)]
            #if self.trace_table[-1][0] != currLine:
            values = [currLine] + [entry.get(var,'') for var in variables] + [output]
            self.trace_table.append(values)


