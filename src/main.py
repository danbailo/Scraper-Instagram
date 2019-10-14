from core import Instagram
import json

if __name__ == "__main__":
    instagram = Instagram("danbailo1")

    print(instagram.username)
    print(instagram.id_user)
    # print(*instagram.get_imgs_links(), sep="\n")
    instagram.get_imgs_links()

    # instagram.write_links()

    # instagram.download_imgs()
    # print(instagram.get_root())