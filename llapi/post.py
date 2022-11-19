class Post:
    
    def __init__(self, header: str = None, text: str = None, image_url: str = None, video_url: str = None) -> None:
        self.__header = header
        self.__text = text
        self.__image_url = image_url
        self.__video_url = video_url

        self.__post_data = {
            'header' : self.__header,
            'text': self.__text,
            'image_url': self.__image_url,
            'video_url': self.__video_url
        }


    async def update_field(self, field_name: str, value) -> None:
        self.__post_data[field_name] = value

    async def get_data(self) -> dict:
        return self.__post_data

    async def get_post(self) -> super:
        return self

    async def post_text(self) -> str:
        return f"{self.__post_data['header']} {self.__post_data['text']}"

    async def post_photo(self) -> str:
        return f"{self.__post_data['image_url']}"

    async def post_video(self) -> str:
        return f"{self.__post_data['video_url']}"



class PostQueue:

    def __init__(self) -> None:
        self.__posts = list()
        self.__cursor = 0


    async def make(self, data: list) -> None:
       self.__posts = data

    @property
    async def count(self) -> int:
        return len(self.__posts)

    @property
    async def empty(self) -> bool:
        return bool(len(self.__posts))

    async def list_of(self) -> list:
        return self.__posts

    async def get_post(self) -> Post:
        return self.__posts[self.__cursor]

    async def accept(self) -> None:
        self.__posts.pop(self.__cursor)


