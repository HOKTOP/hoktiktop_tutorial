from pytube import Playlist 

urlplaylist = input('Your url plz:')
p= Playlist(urlplaylist)

print(f"your list you want downloded:{p.title}")

downloaded = input(f"if you want contnue inter  y or n for no:")

if(downloaded == "y"):
    for list in p.videos:
        print(f"we download now {list.title}")
        list.streams.filter(progressive=True,file_extension='mp4').order_by("resolution").desc().first().download()
        print("done")
    
