import json

def load_videos():
    try:
        with open("sajanyt.txt",'r')as file:
            test=json.load(file)
            return test
    except FileNotFoundError:
        return []    

def save_data(videos):
    with open ("sajanyt.txt",'w') as file :
        json.dump(videos,file)

def see_all_videos(videos):
    print("\n")
    print("*"*95)
    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video["name"]},    duration: {video['time']}")
    print("\n")
    print("*"*95)    



def add_videos(videos):
    name=input("enter name of the video to add: ")
    time=input("enter duration of the video to add: ")
    videos.append({'name':name,'time':time})
    save_data(videos)


def update_particular_videos(videos):
    see_all_videos(videos)

    index=int(input("enter index number to update: "))
    if 1<=index<=len(videos):
        name=input("enter new name of the video: ")
        time=input("enter new duration of the video: ")
        videos[index-1]={'name':name,'time':time}
        save_data(videos)
        




def delete_particular_videos(videos):
    see_all_videos(videos)
    index=int(input("enter index number to update: "))
    if 1<=index>=len(videos):
        del videos[index-1]
        save_data(videos)
    else:
        print("invalid index selected ")

def main()->None:
    videos=load_videos()
    while True:
        print("\n 'yt manager'")
        print("1 for (see_all_videos)")
        print("2 for (add_videos)")
        print("3 for (update_particular_videos)")
        print("4 for (delete_particular_videos)")
        print("5 for (exit from videos)")
        choice=int(input("enter your choice"))
        
        match choice:
            case 1:
                see_all_videos(videos)
            case 2:
                add_videos(videos)
            case 3:
                update_particular_videos(videos)
            case 4:
                delete_particular_videos(videos)
            case 5:
                break                
            case _:
                print("enter valid choice")

if __name__=="__main__":
    main()
else:
        print("invalid index selected ")