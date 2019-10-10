from PIL import Image
import requests
import io

class Instagram:

    def __init__(self, username):
        self.BASE_URL = r"https://www.instagram.com"
        self.QUERY_HASH = "58b6785bea111c67129decbe6a448951"
        self.FIRST = 12

        self.username = username
        self.__response = requests.get('https://www.instagram.com/'+self.username+'/', params=(('__a', '1'),))
        self.__instagram = self.__response.json()
        self.__response.close()
        self.__instagram = self.__instagram["graphql"]["user"]
        self.id_user = self.__instagram["id"]

    def get_end_cursor(self):
        page_info = self.__instagram["edge_owner_to_timeline_media"]["page_info"]
        if page_info["has_next_page"]:
            return page_info['end_cursor']

    def get_next_page(self,end_cursor):
        params = (
            ('query_hash', '58b6785bea111c67129decbe6a448951'),
            ('variables', '{"id":'+'"'+self.id_user+'"'+',"first":12,"after":'+'"'+end_cursor+'"'+'}'),)
        response = requests.get(self.BASE_URL+'/graphql/query/', params=params)
        response_json = response.json()
        response.close()
        return response_json

    def get_imgs_links(self):
        links_imgs = []

        for i in range(self.FIRST):
            node = self.__instagram["edge_owner_to_timeline_media"]["edges"][i]["node"]
            link_img = node["display_url"]
            id_img = node["id"]
            # links_imgs.append((id_img,link_img))
            links_imgs.append(link_img)

        response = self.get_next_page(self.get_end_cursor())
        while True:
            for i in range(self.FIRST):
                page_info = response["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]
                try:
                    node = response["data"]["user"]["edge_owner_to_timeline_media"]["edges"][i]["node"]
                    link_img = node["display_url"]
                    id_img = node["id"]
                except IndexError: break
                # links_imgs.append((id_img, link_img))
                links_imgs.append(link_img)
            if page_info["has_next_page"]: response = self.get_next_page(page_info["end_cursor"])
            else: break
        return links_imgs
    
    def write_links(self):
        with open('links.txt','w') as file:
            for link_img in self.get_imgs_links():
                file.write(link_img +"\n")
    
    def download_imgs(self):
        with open('links.txt','r') as file:
            i = 0
            for line in file:
                response = requests.get(line)
                img = Image.open(io.BytesIO(response.content))
                img.save("../imgs/"+str(i)+".png")
                i += 1





