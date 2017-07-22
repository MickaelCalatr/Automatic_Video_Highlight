# Video_Automatic_Highlight

## Update my API:

When an update is available, I will send you a message on Wechat.  
To update the repository you just need to connect to the server, go in the folder Video_Automatic_Highlight and execute the file *Update*.

```
./Update
```

You will need to enter your Github login and password. After that the update will start.


## Launch my API V1.\*.\* (actual version):

To execute my API, go in folder Source and execute the file *main.py* and specify your videos, and the teams colors. For exemple you have __*0.mp4 1.mp4 2.mp4*__ and __*3.mp4*__ and the colors of the teams are __*blue*__ and __*red*__, the line will be this:

```
python3 ./main.py -tc1 blue -tc2 red -i O.mp4 1.mp4 2.mp4 3.mp4
```

If you need to change the name of the final video you can add *-n* , like this:

```
python3 ./main.py -tc1 blue -tc2 red -i O.mp4 1.mp4 2.mp4 3.mp4 -n name_of_final_video
```

## Launch my API V2.\*.\* (In progress):

To execute my API it's very simple you just need to execute the file *Start* and specify your videos. For exemple you have *0.mp4 1.mp4 2.mp4* and *3.mp4*, the line will be this:

```
python3 ./Start -i O.mp4 1.mp4 2.mp4 3.mp4
```

If you need to change the name of the final video you can add *-n* , like this:

```
python3 ./Start -i O.mp4 1.mp4 2.mp4 3.mp4 -n name_of_final_video
```
