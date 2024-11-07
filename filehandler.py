# Open a file in read and write mode
with open("example.txt", "w+") as file:
    # write(): Write some content to the file
    file.write("Hello, world!\nThis is a sample text file.")

    # flush(): Flush the internal buffer, forcing a write to disk
    file.flush()

    # writable(): Check if the file is writable
    print("Is the file writable?", file.writable())

    # tell(): Get the current position in the file
    print("Current file position:", file.tell())

    # seek(): Move to the beginning of the file
    file.seek(0)

    # readable(): Check if the file is readable
    print("Is the file readable?", file.readable())

    # read(): Read the entire file content
    content = file.read()
    print("File content:\n", content)

    # readline(): Read the first line from the file
    file.seek(0)
    print("First line:", file.readline())

    # readlines(): Read all lines and return as a list
    file.seek(0)
    lines = file.readlines()
    print("All lines as a list:", lines)

    # writable(): Check if file is writable before attempting write operations
    if file.writable():
        # write(): Write another line to the file
        file.write("\nAppending a new line.")

        # writelines(): Write multiple lines to the file
        file.writelines(["\nLine 1", "\nLine 2", "\nLine 3"])

    # seekable(): Check if file allows changing the file position
    print("Is the file seekable?", file.seekable())

    # seek() again to read the new content from the beginning
    file.seek(0)
    print("Updated file content:\n", file.read())

    # truncate(): Resize the file to 20 bytes
    file.truncate(20)
    file.seek(0)
    print("Truncated file content:\n", file.read())

    # isatty(): Check if the file stream is interactive (usually False for file streams)
    print("Is the file interactive?", file.isatty())

    # fileno(): Get the file descriptor
    print("File descriptor number:", file.fileno())

# detach() and close() can be demonstrated with a different type of file handling in binary mode
import io

with open("example.txt", "wb+") as file:
    # Write binary data to the file
    file.write(b"Binary data example.")

    # detach(): Separate the underlying binary buffer from the TextIOWrapper
    raw = file.detach()
    print("Detached raw stream:", raw)
    pass
# After detach(), the file object is no longer usable for read/write operations.
