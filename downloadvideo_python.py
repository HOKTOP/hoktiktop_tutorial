from pytube import YouTube

print("your url video plz .:")
url = input()
print('we downlod your video now plz wait')
y = YouTube(url).streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download()
