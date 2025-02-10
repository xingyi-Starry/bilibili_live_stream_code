# bilibili_live_stream_code
1. Used to retrieve third-party streaming codes when preparing for a live broadcast, allowing you to bypass the Bilibili Live Assistant and directly stream using software like OBS. The software also provides the ability to define the live broadcast category and title.
2. Suitable for people who want to use third-party streaming software to stream live without using the Bilibili Live Assistant.

## Disclaimer

1. This program is only used to obtain the streaming address and streaming code. It will not result in a ban or any other account-related issues. We are not responsible for any account-related problems.

## Usage Tutorial

### Manually Retrieve Cookie

1. Log in to your Bilibili web client.
2. Enter your live broadcast room.
3. Press ***F12*** to enter developer mode and select the Network tab.
4. Send any barrage message to yourself (you can send messages without starting a live broadcast).
5. Find the entry named ***send*** in the Network tab and click it.
6. In the Headers section, find ***Cookie*** under Request Headers and ***csrf*** in the Form Data under Payload. Copy them respectively.
7. Get your live broadcast room ID (which can be found in Personal Center - My Live Room - Live Settings).
8. Open the program and enter the required values as instructed (the room ID is ***room_id***).
9. Set the title and category.
10. Enter the live broadcast server and streaming code in OBS and start the live broadcast.

### Automatically Retrieve Cookie

1. Scan the QR code to log in.
2. Set the title and category.
3. Enter the live broadcast server and streaming code in OBS and start the live broadcast.

## Precautions

1. **Be sure to use this program to stop the broadcast. Stopping the broadcast in OBS will not stop the broadcast!!! (Very important!!!!)**
2. If you accidentally close the program, just repeat the above steps.
3. The obtained streaming code can only be used once. You need to retrieve it again for the next live broadcast.
4. The saved Cookies can be reused within a certain period (I also don't know how long). If they become invalid, just repeat the above steps.
5. When automatically retrieving Cookies, do not keep the mouse on the webpage for too long. After a successful login, remove it, otherwise, it may fail to retrieve!
6. If there is no response after logging in, please move the mouse to the avatar area.

## Others

1. Author of this program: Chace.  
2. Special thanks for the creation of this program: Qinzi.

## Chinese version
1. https://github.com/ChaceQC/bilibili_live_stream_code/blob/main/README.md
