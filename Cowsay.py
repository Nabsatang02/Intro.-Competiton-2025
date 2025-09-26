def cowsay(message):
    bubble = " " + "-" * (len(message) + 2)
    bubble_middle = f"< {message} >"
    cow = r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
    """

    print(bubble)
    print(bubble_middle)
    print(bubble)
    print(cow)
