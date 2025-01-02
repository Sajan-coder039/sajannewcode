import sqlite3

con=sqlite3.connect("youtubesq.db")

cur=con.cursor()

cur.execute('''
    CREATE TABLE if not EXISTS video(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
    )
''')


def see_all_videos():
    cur.execute("SELECT * FROM video ")
    rows=cur.fetchall()
    if len(rows)==0:
        print("empty video list ")
    for row in rows:
        print(row)
   

def add_videos(name, time):
    cur.execute("INSERT INTO video(name, time) VALUES (?, ?)", (name, time))
    con.commit()


def update_particular_videos(video_id, newname, newtime):
    cur.execute("UPDATE video SET name= ?, time= ? WHERE id = ?", (newname, newtime, video_id))
    con.commit()


def delete_particular_videos(video_id):
    cur.execute("DELETE FROM video WHERE id=? ",(video_id,))
    con.commit()


def main():
    while True:
        print("\n  youtube manager ")
        print("1 for (see_all_videos)")
        print("2 for (add_videos)")
        print("3 for (update_particular_videos)")
        print("4 for (delete_particular_videos)")
        print("5 for (exit from videos)")
        choice=int(input("enter your choice: "))

        if choice==1:
            see_all_videos()
                    
        elif choice==2:
            name=input("enter the video name: ")
            time=input("enter the video time: ")
            add_videos(name,time)
        
        elif choice==3:
            video_id=int(input("enter the video id to update: "))
            name=input("enter the new video name: ")
            time=input("enter the new video time: ")
            update_particular_videos(video_id,name,time)
        
        elif choice==4:
            video_id=int(input("enter the video id to delete: "))
            delete_particular_videos(video_id)
        
        elif choice==5:
            break  
        
        else :
            print("invalid choice selected ")   

   
    con.close()


if __name__=="__main__":
    main()          