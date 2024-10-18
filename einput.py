import prompt_toolkit
from prompt_toolkit.validation import Validator, ValidationError
import re

def einput(prompt="> ", regex=False, req_regex=".*", autocomplete=False, autocomplete_list=None, error_color="red", success_color="green", error_message=None, regex_move_cursor_to_end=False, raise_error_if_empty=True, style_dict=None):
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
        u_input = session.prompt(
            prompt,
            completer=completer,
            validator=validator,
            style=style
        )
    except Exception as e:
        if raise_error_if_empty:
            raise Exception("Error in einput (if you dont want to see this error then set raise_error_if_empty to False): " + str(e))
        else:
            return None

    return u_input

