def panggil(biodata):
    try:
        with open("biodata.txt", "r") as file:
            print(file.read())

    except ImportError as err:
        print("Tidak ada(file)".format)
