
def recurse_access_key(current_val, keys):
    """ Given a list of keys and a dictionary, recursively access the dicionary
    using the keys until we find the key its looking for

    If a key is an integer, it will convert it and use it as a list index

    Example:

        >>> recurse_access_key({'a': 'b'}, ['a'])
        'b'
        >>> recurse_access_key({'a': {'b': ['c', 'd']}}, ['a', 'b', '0'])
        'c'

    Args:
        current_val (dict): current dictionary we have recursed into
        keys (list): list of str/int of subkeys

    Returns:
        str or dict: value of subkey in dict
    """
    if not keys:
        return current_val
    else:
        current_key = keys.pop(0)

        try:
            current_key = int(current_key)
        except ValueError:
            pass

        return recurse_access_key(current_val[current_key], keys)

def save_value(expected, to_check):
    """Save a value in the response for use in future tests

    Args:
    	expected (dict): expected saved dict
        to_check (dict): An element of the response from which the given key
            is extracted
        

    Returns:
        dict: dictionary of save_name: value, where save_name is the key we
            wanted to save this value as
    """
    saved = {}

    if not to_check:
    	pass
        # self._adderr("No %s in response (wanted to save %s)",
        #     key, expected)
    else:
        for save_as, joined_key in expected.items():
            split_key = joined_key.split(".")
            try:
                saved[save_as] = recurse_access_key(to_check, split_key)
            except (IndexError, KeyError) as e:
            	pass
                # self._adderr("Wanted to save '%s' from '%s', but it did not exist in the response",
                #     joined_key, key, e=e)

    if saved:
        # logger.debug("Saved %s for '%s' from response", saved, key)
        return saved

if __name__ == '__main__':
	expected = {
		"user": "context.data.name", => ["context", "data", "name"]
		"age": "context.age"
	}
	context = {
		"context": {
			"name": "ruby",
			"age": 21
		}
	}

	print(save_value(expected, context));


