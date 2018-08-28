def is_number(s):
    try:
        float(s)
        return true
    except ValueError:
        return false
