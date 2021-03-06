from pydub import AudioSegment
import os
import shutil

song_path = r"C:\Users\pravi\Desktop\music4all\rock_music"
save_path = r"C:\Users\pravi\Desktop\music4all\audios"

song_path_list = os.listdir(song_path)

for songs in song_path_list:
    song_play = AudioSegment.from_mp3(song_path + "/" + songs)

    start_sec = 60 * 1000
    stop_sec = 105 * 1000
    song_slice = song_play[start_sec:stop_sec]
    sstring = '.mp3'
    if songs.endswith(sstring):
        song = songs[:-(len(sstring))]
    song_slice.export(save_path + "/" +song+'.wav', format='wav')

# if you are using google colab, you can save it in the 75GB disk provided by the colab server and then copy it in a file in your drive
# 1st remove all other file directory from contents in colab and then copy it to the location you want in your colab
# FOR GOOGLE COLAB you will not specify "save_path" 
save_song_list = "/content"
song_save_list = os.listdir(save_song_list)
song_save_list.remove('.config')
song_save_list.remove('sample_data')
song_save_list.remove('drive')
songs_save_list = song_save_list
songs_save_list 
loc = '/content/drive/MyDrive/HSP_datasets'
for i in songs_save_list:
      shutil.copy(i, loc + "/" + i)
