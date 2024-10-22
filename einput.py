import prompt_toolkit
from prompt_toolkit.validation import Validator, ValidationError
import re
from threading import Thread

class einputthread:

    def __init__(self, prompt="> ", regex=False, req_regex=".*", autocomplete=False, autocomplete_list=None, error_color="red", success_color="green", error_message=None, regex_move_cursor_to_end=False, raise_error_if_empty=True, style_dict=None,
           is_password=False, timeout=None, multiple_lines=False, multiple_lines_limit=10):

        self.prompt = prompt
        self.regex = regex
        self.req_regex = req_regex
        self.autocomplete = autocomplete
        self.autocomplete_list = autocomplete_list
        self.error_color = error_color
        self.success_color = success_color
        self.error_message = error_message
        self.regex_move_cursor_to_end = regex_move_cursor_to_end
        self.raise_error_if_empty = raise_error_if_empty
        self.style_dict = style_dict
        self.is_password = is_password
        self.timeout = timeout
        self.multiple_lines = multiple_lines
        self.multiple_lines_limit = multiple_lines_limit
        
        self.stop_flag = False

        self.t = Thread(target=self.run)
        self.t.daemon = True
        self.t.start()
        if timeout != None: self.t.join(timeout=timeout)
        else: self.t.join()


    def run(self):
        self.result = einput(
            prompt=self.prompt,
            regex=self.regex,
            req_regex=self.req_regex,
            autocomplete=self.autocomplete,
            autocomplete_list=self.autocomplete_list,
            error_color=self.error_color,
            success_color=self.success_color,
            error_message=self.error_message,
            regex_move_cursor_to_end=self.regex_move_cursor_to_end,
            raise_error_if_empty=self.raise_error_if_empty,
            style_dict=self.style_dict,
            is_password=self.is_password,
            timeout=None,
            multiple_lines=self.multiple_lines,
            multiple_lines_limit=self.multiple_lines_limit,
            stop_flag=self.stop_flag
        )
    
    def stop(self):
        self.stop_flag = True

    def get_result(self):
        return self.result

def einput(prompt="> ", regex=False, req_regex=".*", autocomplete=False, autocomplete_list=None, error_color="red", success_color="green", error_message=None, regex_move_cursor_to_end=False, raise_error_if_empty=True, style_dict=None,
           is_password=False, timeout=None, multiple_lines=False, multiple_lines_limit=10, multiple_lines_array=False, stop_flag=False):
    """
    `prompt` - The prompt message displayed to the user.\n
    `regex` - Boolean indicating whether to use regular expression validation.\n
    `req_regex` - The regular expression pattern to validate input against.\n
    `autocomplete` - Boolean indicating whether to enable autocomplete.\n
    `autocomplete_list` - A list of suggestions for autocompletion as the user types.\n
    `error_color` - The color of the error message.\n
    `success_color` - The color of the success message.\n
    `error_message` - The error message to display if validation fails.\n
    `regex_move_cursor_to_end` - Boolean indicating whether to move the cursor to the end on regex validation failure.\n
    `raise_error_if_empty` - Boolean indicating whether to raise an error if input is empty.\n
    `style_dict` - Dictionary defining custom styles for the prompt interface.\n
    `is_password` - Boolean indicating whether to mask input with asterisks.\n
    `timeout` - The number of seconds to wait before timing out. (None means no timeout, means infinite timeout) (if users not input anything then it will be None)\n
    `multiple_lines` - Boolean indicating whether to use multiple lines for input.\n
    `multiple_lines_limit` - The maximum number of lines to allow for input.\n
    `multiple_lines_array` - Boolean indicating whether to use array for multiple lines for input.\n
    `stop_flag` - Boolean indicating whether to stop the input thread.\n
    
    """

    if timeout != None:
        z = einputthread(prompt, regex, req_regex, autocomplete, autocomplete_list, error_color, success_color, error_message, regex_move_cursor_to_end, raise_error_if_empty, style_dict, is_password, timeout)
        return z.get_result()

    validator = None
    if regex:
        if req_regex == None:
            raise Exception("req_regex cannot be None if regex is True")
        regex = re.compile(req_regex)
        validator = Validator.from_callable(
            lambda text: bool(regex.match(text)),
            error_message='Input does not match the required pattern.',
            move_cursor_to_end=regex_move_cursor_to_end
        )
    
    completer = None
    if autocomplete:
        if autocomplete_list != None:
            completer = prompt_toolkit.completion.WordCompleter(autocomplete_list)
        else:
            raise Exception("autocomplete_list cannot be None if autocomplete is True")
    
    if style_dict == None: style_dict = {
        "completion-menu.completion": "bg:#ffffff #000000",
        "completion-menu.completion.current": "bg:#ffffff #000000",
        "completion-menu": "bg:#ffffff #000000",
    }
    
    style = prompt_toolkit.styles.Style.from_dict(style_dict)

    session = prompt_toolkit.PromptSession()

    try:
        if multiple_lines:
            lines = []
            for i in range(multiple_lines_limit):
                if stop_flag: return None
                u_input = session.prompt(
                    prompt,
                    completer=completer,
                    validator=validator,
                    style=style,
                    is_password=is_password
                )
                lines.append(u_input)
                if u_input == "":
                    break
            if multiple_lines_array:
                u_input = lines
            else:
                u_input = "\n".join(lines)
        else:
            if stop_flag: return None
            u_input = session.prompt(
                prompt,
                completer=completer,
                validator=validator,
                style=style,
                is_password=is_password
            )
    except Exception as e:
        if raise_error_if_empty:
            raise Exception("Error in einput (if you dont want to see this error then set raise_error_if_empty to False): " + str(e))
        else:
            return None

    return u_input

