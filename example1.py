from einput import einput


def main():
    autocompletelist = ["hi", "123", "hello", "world"]
    text = einput(
        prompt="> ",
        regex=True,
        req_regex="^[0-9]*$", # only numbers
        error_color="red",
        success_color="green",
        regex_move_cursor_to_end=True,
        raise_error_if_empty=True,
        autocomplete=True,
        autocomplete_list=autocompletelist,
        is_password=False,
        multiple_lines=True,
        multiple_lines_limit=5,
        multiple_lines_array=False
    )

    print(text)


if __name__ == "__main__":
    main()