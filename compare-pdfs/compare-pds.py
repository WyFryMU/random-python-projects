#Compare PDFs
#Sample pdf from https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf
#Honestly this was my first time seeing hashlib so had no idea what to do. This is just the copied solution from https://www.geeksforgeeks.org/python/check-if-two-pdf-documents-are-identical-with-python/
#I just updated the argument names and added a random pdf

import hashlib


def hash_file(file_name_1, file_name_2):
    # Use hashlib to store the hash of a file
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    with open(file_name_1, "rb") as file:

        # Use file.read() to read the size of file
        # and read the file in small chunks
        # because we cannot read the large files.
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h1.update(chunk)

    with open(file_name_2, "rb") as file:

        # Use file.read() to read the size of file a
        # and read the file in small chunks
        # because we cannot read the large files.
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h2.update(chunk)

        # hexdigest() is of 160 bits
        return h1.hexdigest(), h2.hexdigest()


msg1, msg2 = hash_file("sample-local-pdf.pdf", "sample-local-pdf.pdf")

if (msg1 != msg2):
    print("These files are not identical")
else:
    print("These files are identical")