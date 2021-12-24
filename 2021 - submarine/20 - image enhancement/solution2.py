import fileinput

from image import Image


def solve(input_file):
    algo = input_file.readline().strip()
    input_file.readline()

    img = Image.from_file(input_file)

    for _ in range(25):
        img.pad(3, ".")
        img.enhance(algo, True)
        img.enhance(algo, False)

    return img.count()


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))
