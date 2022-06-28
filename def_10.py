# Ваша задача написать функцию domain_name, которая принимает строку url,
# извлекает из нее доменное имя и возвращает его в качестве строки
#
# domain_name("http://google.com") # возвращает "google"
# domain_name("http://google.co.jp") # возвращает  "google"
# domain_name("www.xakep.ru") # возвращает "xakep"
# domain_name("https://youtube.com") # возвращает "youtube"
# domain_name("https://www.asos.com") # возвращает "asos"
# domain_name("http://www.lenovo.com") # возвращает "lenovo"
# URL может начинаться с протоколов http://  https:// или с www. URL,
# начинающиеся с протоколов http://  https://, могут также содержать www.

def domain_name(url: str) -> str:
    url = url.replace("http://", "").replace("https://", "").replace("www.", "").replace("https://www.", "").replace(
        "http://www.", "")
    url = url.split('.')
    return url[0]


# url = "http://www.lenovo.com"
# print(domain_name(url))
