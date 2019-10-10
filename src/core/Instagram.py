import requests

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
            # links_imgs.append((id_img, link_img))
            links_imgs.append(link_img)

        response = self.get_next_page(self.get_end_cursor())
        while True:
            about = response["data"]["user"]["edge_owner_to_timeline_media"]
            i=0
            while i < 12:
                try:
                    link_img = about["edges"][i]["node"]["display_url"]
                    id_img = about["edges"][i]["node"]["id"]
                except IndexError: break
                # links_imgs.append((id_img,link_img))
                links_imgs.append(link_img)
                i += 1
            if about["page_info"]["has_next_page"]:        
                response = self.get_next_page(about["page_info"]["end_cursor"])
            else: break
        return links_imgs
        


