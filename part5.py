# class Book():
#     def read(self):
#         print("Читаем интересную историю")
#
# class StoryReader():
#     def __init__(self):
#         self.book = Book()
#
#     def read_story(self):
#         self.book.read()
#
#
from abc import ABC, abstractmethod

class StorySource(ABC):
    @abstractmethod
    def get_story(self):
        pass

class Book(StorySource):
    def get_story(self):
        print("Читаем интересную историю")

class AudioBook(StorySource):
    def get_story(self):
        print("Слушаем интересную историю")

class StoryReader():
    def __init__(self, story_source: StorySource):
        self.story_source = story_source

    def read_story(self):
        self.story_source.get_story()

book = Book()

audio_book = AudioBook()

read_book = StoryReader(book)

read_audio_book = StoryReader(audio_book)

read_book.read_story()

read_audio_book.read_story()


