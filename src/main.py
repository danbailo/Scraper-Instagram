from core import Instagram
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Por favor, entre com um usuário!")
        exit(-1)
    instagram = Instagram(sys.argv[1])

    print(instagram.username)
    print(instagram.id_user)
    # instagram.get_imgs_links()
    instagram.write_links()
    instagram.download_imgs()