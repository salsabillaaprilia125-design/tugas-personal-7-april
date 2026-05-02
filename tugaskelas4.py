
class SongNode:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.prev = None
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None
        self.current = None

    def add_song(self, title, artist):
        new_song = SongNode(title, artist)

        if not self.head:
            self.head = new_song
            self.head.next = self.head
            self.head.prev = self.head
            self.current = self.head
            return

        tail = self.head.prev

        tail.next = new_song
        new_song.prev = tail
        new_song.next = self.head
        self.head.prev = new_song

    def remove_song(self, title):
        if not self.head:
            return

        temp = self.head
        while True:
            if temp.title == title:
                if temp.next == temp:
                    self.head = None
                    self.current = None
                    return

                temp.prev.next = temp.next
                temp.next.prev = temp.prev

                if temp == self.head:
                    self.head = temp.next

                if temp == self.current:
                    self.current = temp.next

                return

            temp = temp.next
            if temp == self.head:
                break

    def show_playlist(self):
        if not self.head:
            print("Playlist kosong")
            return

        temp = self.head
        i = 1
        while True:
            print(f"{i}. {temp.title} - {temp.artist}")
            temp = temp.next
            i += 1
            if temp == self.head:
                break

    def play_current(self):
        if self.current:
            print(f"Now Playing: {self.current.title} - {self.current.artist}")

    def next_song(self):
        if self.current:
            self.current = self.current.next
            self.play_current()

    def prev_song(self):
        if self.current:
            self.current = self.current.prev
            self.play_current()


# Testing
playlist = Playlist()

playlist.add_song("Song A", "Artist X")
playlist.add_song("Song B", "Artist Y")
playlist.add_song("Song C", "Artist Z")

playlist.show_playlist()

playlist.play_current()
playlist.next_song()
playlist.next_song()
playlist.next_song()  # loop

playlist.prev_song()

playlist.remove_song("Song B")
print("\nSetelah hapus Song B:")
playlist.show_playlist()