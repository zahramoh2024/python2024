print("welcome")
number_of_song=0
list_of_songs=[]
while 1:
    a=int(input("""
    1.add song
    2.list of songs
    3.delete song
    4.exit
    make a choice:"""))
    if a==4:
        break
    else:
        if a==1:
            name_of_song=input("what is the name of song???")
            name_of_singer=input("what is the name of singer???")
            number_of_song+=1
            list_of_songs.append([name_of_song,name_of_singer,number_of_song])
            print("done :)   ","the number of song is",number_of_song)
        if a==2:
            if len(list_of_songs)==0:
                print("the list of songs is empty")
            else:
                for item in list_of_songs:
                    print(f"num: {item[-1]}   song: {item[0]}   singer: {item[1]}")
        if a==3:
            num_of_song_to_delete=int(input("please enter the number of song:"))
            if num_of_song_to_delete not in range(1,len(list_of_songs)+1):
                print("this song is not available")
            else:
                print("done! this song deleted : ",list_of_songs.pop(num_of_song_to_delete-1))

print("zahra")

