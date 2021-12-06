def song_decoder(song):
    song = song.split('WUB')
    original_song = []
    for i in song:
        if i != '':
            original_song += [i]
    return ' '.join(original_song)
