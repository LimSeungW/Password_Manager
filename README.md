# Password_Manager
이 프로젝트는 사용자의 ID와 PW를 저장하고 관리하기 위해 제작되었다. 

사용자로 부터 고유 암호화 코드를 입력받아, 각종 ID와 PW를 암호화 하여 저장하고, 필요시 다시 이것을 복호화하여 사용자에게 보여준다.

This project was created to store and manage user's ID and PW.

It receives a unique encryption code from the user, encrypts and stores various IDs and PWs, and decrypts them again to show them to the user if necessary
*** 
### * 프로젝트 계획 동기(Motivation for project planning)
웹에서 로그인을 할때마다 ID와 PW가 기억이 안나서 따로 저장할 공간이 필요했다.

그런데 notepad어플에 기록하기에는 보안이 걱정되어 내가 이 프로젝트를 만들게 되었다.

Every time I logged in on the web, I couldn't remember my ID and PW, so I needed a separate storage space.

However, I was worried about security to record in the notepad application, so I made this project.

*** 
### * 프로젝트의 목적(purpose of the project)
이 프로젝트는 사용자의 ID와 PW를 관리하는것이 목적이다. 여기서 말하는 ID와 PW는 이 어플리케이션 초기화면의 로그인 단계뿐만아니라, 항목별 ID와 PW 모두 포함된다.

ID와 PW는 사용자로부터 로그인 계정을 만들시 최대 4자리의 정수를 입력받아, 이 정수코드를 통해 암호화를 하여 저장한다.

이후, 비밀번호가 변경되었거나 데이터 삭제를 원할시 데이터 수정을 진행할 수 있고, 필요에 따라 모든데이터를 삭제할 수도 있다.

The purpose of this project is to manage user ID and PW. The ID and PW mentioned here include not only the login stage of the initial screen of this application, but also ID and PW for each item.

The ID and PW receive an integer of up to 4 digits when creating a login account from the user, and are encrypted and stored through the integer code.

After that, if the password has been changed or if you want to delete data, you can proceed with data modification, or delete all data if necessary.
***
### * 프로젝트로 인한 학습효과(Learning effect from the project)
이 프로그램의 암호화 수준은 낮은편이다. 암호화의 기초를 토대로 방법을 생각하여 구현할 수 있었고, 이를  json 파일로 만드는 관리법을 통해 json의 입/출력 및 수정을 공부할 수 있었다.

이러한 틀을 Python에 접목시켜 GUI를 구성하여 유저에게 쉽게 사용할 방법을 제공하는것을 목표로 공부하여 프로젝트를 완성하였다.

The encryption level of this program is low. I was able to think and implement a method based on the basics of encryption, and I was able to study the input/output and modification of json through the management method of making it into a json file.

The project was completed by studying with the goal of providing users with an easy-to-use method by integrating this framework with Python to configure a GUI.
***
### * 프로젝트 세부 사항(project details)
![FlowChart](https://user-images.githubusercontent.com/112800645/222181653-3b60c2e5-9976-45c7-b762-7058e06eec34.png)
프로그램의 FlowChart 는 위 그림과 같다.

The flowchart of the program is shown in the figure above.
  + 계정만들기(Create an account ->account.py)
  
    ![create](https://user-images.githubusercontent.com/112800645/222182707-37190f1a-64ca-4f6e-8ca1-1fbd3b4fbd5b.PNG)
    
    이 화면에서 어플리케이션은 사용자로부터 ID와 PW, 그리고 4자리의 정수코드를 입력받는다.
    
    계정이 성공적으로 만들어지면, 암호화된 data.json 파일이 만들어진다.
    
    On this screen, the application receives ID, PW, and 4-digit integer code from the user.
    
    When an account is created successfully, an encrypted "data.json" file is created.

  + 로그인(Login ->Login.py)
  
    ![login gui](https://user-images.githubusercontent.com/112800645/222177654-ad2095a2-20dd-4ac1-a6eb-bef2738ecc64.PNG)
    
    이 화면은 사용자가 만들었던 계정을 로그인하는 화면이다. 성공적으로 로그인하면 로그인이 성공했다는 알림을 발생시키고 반면에 잘못된 PW를 입력시 다시 입력하라는 에러를 발생시킨다.
    
    This is the screen where you log in to the account you created. If login is successfully, a notification that the login was successful occurs.
    
    On the other hand, an error prompting you to re-enter is generated when you enter an incorrect PW.
   
  + 어플리케이션 메인(Application Main ->Program.py)
    
    ![program gui](https://user-images.githubusercontent.com/112800645/222177743-d23ae72f-38d1-40cd-ae7b-22ff4fa97da7.PNG)
    
    어플리케이션의 메인화면이다. 여기서 사용자는 자신의 항목별 ID,PW를 조회할 수 있다. 조회할때는 저장된 "data.json"파일로 부터 데이터를 복호화 과정을 진행한다.
    
    사용자는 데이터를 추가, 삭제, 수정, 저장 할 수 있다. 
    
    This is the main screen of the application. Here, the user can search for his or her ID and PW for each item. 
    
    When searching, the data is decrypted from the saved "data.json" file.
    
    Users can add, delete, modify, and save data.
    
    + 옵션 (Options)
      
      ![setting gui](https://user-images.githubusercontent.com/112800645/222177791-e2a9e2ed-8f5e-4407-9463-c4b4fdfe3350.PNG)
      
      화면의 우측상단 아이콘을 클릭하면 옵션화면을 디스플레이한다. 
    
      이 화면에서 사용자는 모든 데이터를 삭제하거나, 계정의 ID,PW 혹은 암호화 정수 코드를 변경할 수 있다.
      
      
      Click the icon on the top right of the screen to display the option screen.
    
      On this screen, the user can delete all data or change the ID, PW or encryption integer code of the account.
***
### * 사용 라이브러리 및 기타자료 (Libraries and other materials used)
- IDE : VSCODE (v1.75)

- Laugauge : Python (v3.10.6)

- GUI : tkinter

- Data : json

- Other Library : os, Image & ImageTk, partial(functools)

- Icons : from https://www.flaticon.com/
