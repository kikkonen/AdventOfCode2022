import string

PRIORITY_BY_ITEM = {
    item: i + 1
    for i, item in enumerate(string.ascii_lowercase + string.ascii_uppercase)
}
