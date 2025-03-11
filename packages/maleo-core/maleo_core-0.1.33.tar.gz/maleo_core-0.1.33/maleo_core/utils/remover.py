def remove_excluded_fields(data:dict, excluded_fields:set[str]):
    def remove_fields(target, keys):
        """ Recursively remove fields based on dot-separated keys. """
        if not keys:
            return

        key = keys[0]
        remaining_keys = keys[1:]

        if isinstance(target, dict):
            if key in target:
                if remaining_keys:
                    remove_fields(target[key], remaining_keys)
                else:
                    del target[key]
        elif isinstance(target, list):
            for item in target:
                remove_fields(item, keys)

    for field in excluded_fields:
        remove_fields(data, field.split("."))