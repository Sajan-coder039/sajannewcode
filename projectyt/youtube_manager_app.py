import json

def load_data():
    try:
        with open ('youtube.txt','r') as file:
            test= json.load(file)
            print(type(test))
            return test
         
    except FileNotFoundError:
        return []

def save_data_videos(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    for vide in videos:
        print(f"{vide}. ")

def add_video(videos):
    name=input("enter video name:")
    time=input("enter video time:")
    videos.append({'name':name,'time':time})
    save_data_videos(videos)

def update_videos(videos):
    pass

def delete_videos(videos):
    pass




def main()->None:
    videos=load_data()
    while True:
        print("\n youtube manager")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube videos detail")
        print("4. delete a youtube videos")
        print("5. exit the app")
        choice=int(input("Enter your choice"))
        # print(videos)
        
        match choice:
            case 1:
                list_all_videos(videos)
            case 2:
                add_video(videos)
            case 3:
                update_videos(videos)    
            case 4:
                delete_videos(videos)
            case 5:
                break   
            case _:
                print("Invalid choice")

if __name__=="__main__":
    main()