from pytube import Playlist


p = Playlist(input('inter your url playlist:'))

y = input(f"this your playlist ? yes = y no =n")

if y== 'y':
    for vidoes in p.videos:
        print(f"strart download .. {vidoes.title}  ")
        try:
            vidoes.streams.filter(file_extension="mp4").get_by_itag('140').download(filename=f'{vidoes.title}.mp3')
            print('done')
        except:
            print('skip')

            continue
