# Project 2: 100-days-of-code (python), ER model, ER diagram

1) Describe ER model and draw ER diagram of 1 application from the list of projects and their entities. You should use these entities, but if you want, you can add more entities of that application:

Instagram:
User
Post (Photos/Videos)
Comment
Like
Follow
Direct Message
Story
Tag (Used to categorize content or tag users)
Netflix:
User
Movie
TV Show
Season
Episode
Genre
Watchlist
Review
Rating
Profile (A single Netflix account can have multiple profiles)
Facebook:
User
Friend
Post (Status, Photos/Videos)
Comment
Like
Message
Page
Group
Event (A calendar-based resource which can be used to notify users of upcoming occasions)
Twitter:
User
Tweet
Retweet
Like
Follow
Direct Message
Hashtag
Mention (@user mechanism to refer to or reply to users)
WhatsApp:
User
Message
Group
Call
Status
Media (Images, Videos, and Documents shared in conversations)
YouTube:
User
Video
Comment
Like
Subscription (Channel)
Playlist
Advertisements (Promotional content that plays before or during a video)
TikTok:
User
Video
Comment
Like
Follow
Soundtrack (Music)
Challenge (A viral trend where users create videos with the same theme or activity)
Slack:
User
Workspace
Channel
Direct Message
Reaction
File
Thread (A series of messages and replies on a specific subtopic)
Snapchat:
User
Snap (Photo/Video)
Story
Chat
Friend
Filter (Special effects and layers that can be added to Snaps)
Reddit:
User
Subreddit
Post
Comment
Upvote/Downvote
Direct Message
Award (Special recognitions given by users to posts or comments)
You can draw in redactor that is comfortable for you, some examples:
a) https://excalidraw.com/
b) lucidchart.com
c) ...

Here is example of ER model of Pinterest:
"""

Let's assume the main entities in Pinterest to be User, Board, Pin, and Comment.
Attributes: UserID (Primary Key), Username, Email, Password, DateJoined, etc.
Each user can create multiple Boards (One-to-Many relation between User and Board).
Each user can make several Pins (One-to-Many relation between User and Pin).
Each user can post numerous Comments (One-to-Many relation between User and Comment).
Attributes: BoardID (Primary Key), BoardName, CreationDate, UserID (Foreign Key), etc.
Each Board can contain multiple Pins (One-to-Many relation between Board and Pin).
Each Board is owned by a single User.
Attributes: PinID (Primary Key), ImageURL, Description, UserID (Foreign Key), BoardID (Foreign Key), etc.
Each Pin can have numerous Comments (One-to-Many relation between Pin and Comment).
Each Pin is owned by a single User.
Each Pin is contained in a single Board.
Attributes: CommentID (Primary Key), Text, UserID (Foreign Key), PinID (Foreign Key), etc.
Each Comment is associated with a single Pin.
Each Comment is posted by a single User.
""""
and on top of this ER-model you would draw ER-diagram

2) Python practice - complete this list https://replit.com/learn/100-days-of-python
Here is the list of exercises, from easy to more complex ones.
Complete all 100 exercises, so you will have a robust practice upon topics we covered.
The first half of exercises would be a piece of cake, but other half will be more interesting with some new concepts.

3) This is completely optional, but if you have time and want to be a ninja of sql queries, here is very good and practical course:
 https://stepik.org/course/63054/syllabus
