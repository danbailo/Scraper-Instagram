from core import Instagram
import json

if __name__ == "__main__":
    instagram = Instagram("danbailo1")

    print(instagram.username)
    print(instagram.id_user)

    # print(instagram.get_imgs_root().keys())
    # print(json.dumps(instagram.get_imgs_root().keys(), indent=4))

    # print(*instagram.get_imgs_links(), sep="\n")

    with open('links.txt','w') as file:
        for line in instagram.get_imgs_links():
            file.write(line+"\n")