# ⌨️einput

The `einput` is a customizable input prompt utility built using the `prompt_toolkit` library. It provides features such as input validation using regular expressions, autocomplete suggestions, and customizable styles for the prompt interface.

## Features

- **Regular Expression Validation**: Validate user input against a specified regular expression pattern.
- **Autocomplete**: Provide a list of suggestions for autocompletion as the user types.
- **Customizable Styles**: Customize the appearance of the prompt interface using a style dictionary.
- **Error Handling**: Display error messages for invalid input and handle empty input scenarios.

## Installation

To use the `einput` function, you need to have `prompt_toolkit` installed. You can install it via pip:

```bash
pip install prompt_toolkit
```

## Usage

See in examples.

### Parameters

- `prompt`: The prompt message displayed to the user.
- `regex`: Boolean indicating whether to use regular expression validation.
- `req_regex`: The regular expression pattern to validate input against.
- `autocomplete`: Boolean indicating whether to enable autocomplete.
- `autocomplete_list`: List of words for autocomplete suggestions.
- `error_color`: Color for error messages (not currently used in the function).
- `success_color`: Color for success messages (not currently used in the function).
- `error_message`: Custom error message for validation failure (not currently used in the function).
- `regex_move_cursor_to_end`: Boolean indicating whether to move the cursor to the end on regex validation failure.
- `raise_error_if_empty`: Boolean indicating whether to raise an error if input is empty.
- `style_dict`: Dictionary defining custom styles for the prompt interface.
- `is_password`: Masks text with *
- `timeout`: The number of seconds to wait before timing out. (None means no timeout, means infinite timeout) (if users not input anything then it will be None)
- `multiple_lines`: Boolean indicating whether to allow multiple lines of input.
- `multiple_lines_limit`: Integer specifying the maximum number of lines allowed when `multiple_lines` is True.
- `multiple_lines_array`: Boolean indicating whether to return the input as an array of lines when `multiple_lines` is True.

### Example

```python
user_input = einput(
    prompt="Enter your name: ",
    regex=True,
    req_regex="^[A-Za-z]+$",
    autocomplete=True,
    autocomplete_list=["Hello", "world"],
    style_dict={
        "completion-menu.completion": "bg:#00ff00 #000000",
        "completion-menu.completion.current": "bg:#0000ff #ffffff",
        "completion-menu": "bg:#ffffff #000000",
    }
)
print(f"User input: {user_input}")
```

This example sets up a prompt asking for a name, validates that the input contains only letters, provides autocomplete suggestions, and customizes the style of the prompt interface.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions
Contributions are welcome! If you have ideas for improvements or bug fixes, please feel free to make a pull request or open an issue.