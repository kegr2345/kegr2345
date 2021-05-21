def main():
    ok = False
    # The flag starts out false, so the loop runs at least once.
    while not ok:
        try:
            # Get a filename and try to open it
            fn = input("Enter a file name: ")
            infile = open(fn, "r")
            # If we got here, open succeeded.
            ok = True
        except IOError:
            print("Could not open", fn)
   
    # If we got here, we know it successfully opened.
    # Now fn is the filename and infile the file object.

    # Read the entire contents of the file into a list of lines.
    line_list = infile.readlines()

    # Free the resources associated with the file object.
    # We already read the entire contents into a list,
    # so we can close right away.
    infile.close()

    # Label and print the lines of the file.
    lineno = 1
    for line in line_list:
        # Remove newline (and other trailing whitespace)
        line = line.rstrip()
        print(fn, "line", lineno, ":", line)
        lineno += 1


main()
