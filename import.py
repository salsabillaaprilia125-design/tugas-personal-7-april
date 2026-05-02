import random
import json

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

    # ========================
    # BASIC OPERATIONS
    # ========================
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

    # ========================
    # HELPER: Convert to List
    # ========================
    def to_list(self):
        songs = []
        if not self.head:
            return songs

        temp = self.head
        while True:
            songs.append({"title": temp.title, "artist": temp.artist})
            temp = temp.next
            if temp == self.head:
                break

        return songs

    def rebuild_from_list(self, song_list):
        self.head = None
        self.current = None
        for song in song_list:
            self.add_song(song["title"], song["artist"])

    # ========================
    # SHUFFLE
    # ========================
    def shuffle_playlist(self):
        songs = self.to_list()
        random.shuffle(songs)
        self.rebuild_from_list(songs)
        print("Playlist telah di-shuffle.")

    # ========================
    # SORTING (by title)
    # ========================
    def sort_playlist(self):
        songs = self.to_list()
        songs.sort(key=lambda x: x["title"].lower())
        self.rebuild_from_list(songs)
        print("Playlist telah diurutkan berdasarkan judul lagu.")

    # ========================
    # SAVE & LOAD
    # ========================
    def save_to_file(self, filename="playlist.json"):
        songs = self.to_list()
        with open(filename, "w") as f:
            json.dump(songs, f, indent=4)
        print(f"Playlist disimpan ke {filename}")

    def load_from_file(self, filename="playlist.json"):
        try:
            with open(filename, "r") as f:
                songs = json.load(f)
                self.rebuild_from_list(songs)
                print(f"Playlist berhasil dimuat dari {filename}")
        except FileNotFoundError:
            print("File tidak ditemukan!")


# ========================
# TESTING PROGRAM
# ========================
if __name__ == "__main__":
    playlist = Playlist()

    playlist.add_song("Song C", "Artist Z")
    playlist.add_song("Song A", "Artist X")
    playlist.add_song("Song B", "Artist Y")

    print("\n=== Playlist Awal ===")
    playlist.show_playlist()

    print("\n=== Shuffle ===")
    playlist.shuffle_playlist()
    playlist.show_playlist()

    print("\n=== Sorting ===")
    playlist.sort_playlist()
    playlist.show_playlist()

    print("\n=== Simpan ke File ===")
    playlist.save_to_file()

    print("\n=== Load dari File ===")
    new_playlist = Playlist()
    new_playlist.load_from_file()
    new_playlist.show_playlist()

    print("\n=== Playback ===")
    new_playlist.play_current()
    new_playlist.next_song()
    new_playlist.prev_song()