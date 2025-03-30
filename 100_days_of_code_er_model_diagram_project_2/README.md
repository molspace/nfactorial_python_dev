# **Project 2: 100-days-of-code (python), ER model, ER diagram**

## **1) ER Model and ER Diagram**  
Describe the **Entity-Relationship (ER) model** and draw an **ER diagram** for one application from the list below. You should use the listed entities, but you may add additional entities if needed.

### **Applications and Entities**  

#### **Instagram**  
- User  
- Post (Photos/Videos)  
- Comment  
- Like  
- Follow  
- Direct Message  
- Story  
- Tag (Used to categorize content or tag users)  

#### **Netflix**  
- User  
- Movie  
- TV Show  
- Season  
- Episode  
- Genre  
- Watchlist  
- Review  
- Rating  
- Profile (A single Netflix account can have multiple profiles)  

#### **Facebook**  
- User  
- Friend  
- Post (Status, Photos/Videos)  
- Comment  
- Like  
- Message  
- Page  
- Group  
- Event (A calendar-based resource used to notify users of upcoming occasions)  

#### **Twitter**  
- User  
- Tweet  
- Retweet  
- Like  
- Follow  
- Direct Message  
- Hashtag  
- Mention (@user mechanism to refer to or reply to users)  

#### **WhatsApp**  
- User  
- Message  
- Group  
- Call  
- Status  
- Media (Images, Videos, and Documents shared in conversations)  

#### **YouTube**  
- User  
- Video  
- Comment  
- Like  
- Subscription (Channel)  
- Playlist  
- Advertisements (Promotional content that plays before or during a video)  

#### **TikTok**  
- User  
- Video  
- Comment  
- Like  
- Follow  
- Soundtrack (Music)  
- Challenge (A viral trend where users create videos with the same theme or activity)  

#### **Slack**  
- User  
- Workspace  
- Channel  
- Direct Message  
- Reaction  
- File  
- Thread (A series of messages and replies on a specific subtopic)  

#### **Snapchat**  
- User  
- Snap (Photo/Video)  
- Story  
- Chat  
- Friend  
- Filter (Special effects and layers that can be added to Snaps)  

#### **Reddit**  
- User  
- Subreddit  
- Post  
- Comment  
- Upvote/Downvote  
- Direct Message  
- Award (Special recognitions given by users to posts or comments)  

### **How to Draw the ER Diagram**  
You can use any diagramming tool of your choice, such as:  
- [Excalidraw](https://excalidraw.com/)  
- [Lucidchart](https://www.lucidchart.com/)  
- [Draw.io (diagrams.net)](https://www.diagrams.net/)  

### **Example ER Model (Pinterest)**  

Let's assume the main entities in Pinterest are User, Board, Pin, and Comment.

- User: UserID (PK), Username, Email, Password, DateJoined, etc.
    - Each user can create multiple Boards (One-to-Many relation between User and Board).
    - Each user can make several Pins (One-to-Many relation between User and Pin).
    - Each user can post numerous Comments (One-to-Many relation between User and Comment).
- Board: BoardID (PK), BoardName, CreationDate, UserID (FK), etc.
    - Each Board can contain multiple Pins (One-to-Many relation between Board and Pin).
    - Each Board is owned by a single User.
- Pin: PinID (PK), ImageURL, Description, UserID (FK), BoardID (FK), etc.
    - Each Pin can have numerous Comments (One-to-Many relation between Pin and Comment).
    - Each Pin is owned by a single User.
    - Each Pin is contained in a single Board.
- Comment: CommentID (PK), Text, UserID (FK), PinID (FK), etc.
    - Each Comment is associated with a single Pin.
    - Each Comment is posted by a single User.

Using this ER model, you should draw an **ER diagram** for the application you choose.

---

## **2) Python Practice**  
Complete the **100 Days of Python** exercises available at:  
🔗 [Replit - 100 Days of Python](https://replit.com/learn/100-days-of-python)  

These exercises range from **easy** to **more complex** problems.  
- The first half will be simple, reinforcing the basics.  
- The second half will introduce **new concepts** and **challenging problems**.  
- Completing all 100 exercises will give you strong hands-on practice.  

---

## **3) (Optional) SQL Mastery**  
If you have extra time and want to **master SQL queries**, consider taking this practical course:  
🔗 [Stepik - SQL for Beginners](https://stepik.org/course/63054/syllabus)  

This is **optional**, but highly recommended for those who want to become **SQL experts**.  

---

### **Final Notes**  
- The **ER diagram** is a required part of the assignment.  
- **Python exercises** will strengthen your coding skills.  
- **SQL practice** is optional but beneficial for database management.  

Good luck! 🚀  
