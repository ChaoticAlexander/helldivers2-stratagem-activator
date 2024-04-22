from app.constants.config import arrow_keys, function_keys


def filter_event(event):
    is_arrow_key = event.name in arrow_keys
    is_function_key = event.name in function_keys
    is_extended = (
        ((event.is_keypad ^ is_arrow_key) and not event.name.isdigit())
        or is_function_key
        or "right " in event.name
    )
    return {
        "is_arrow_key": is_arrow_key,
        "is_function_key": is_function_key,
        "is_extended": is_extended,
    }
