from mutagen.flac import FLAC
import os


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


os.system("clear")

path = input("Enter absolute path(~ doesn't work):")
if path[-1] != "/":
    path += "/"

files = os.listdir(path)
ind = 0
for file in files:
    try:
        audio = FLAC('{0}{1}'.format(path, file))
        for i in range(len(audio.pictures)):
            audio.pictures[i].data = b''
        audio.save()
        print("done {}".format(file))
        ind += 1
    except Exception as e:
        print()
        print(colored(255, 0, 0, e))
        print()

print()
if ind != 0:
    print(
        colored(154, 205, 50,
                "Completely removed album arts for {} songs.".format(ind)))
else:
    print(colored(255, 140, 0, "Did not remove any album arts."))

print()