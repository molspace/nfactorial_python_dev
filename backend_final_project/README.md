## MVP Leetcode (or any activity) Practice Tracker / Reminder

### Original Proposal:

For my final project I would like to create an application that tracks and reminds a user to practice an activity. For MVP it can be a Leetcode reminder, however ideally I see it as an activity-agnostic (or omni-activity, whatever) app that uses Duolingo-style aggressive approach to user retention. This means the app should have gamified User Experience, simple and understandable User Interface, 

Therefore some of the features that I would like to implement are:
- progress bars to provide visual feedback on how close the user is to completing the unit / chapter etc.
- referral program similar to Uber’s. The reward is a free month of premium subscription
- leaderboard includes a “league” system (bronze, silver, gold)
- “pushy” push notifications
- daily streaks and streak freezes
- friends, friends’ progress tracking

### Project Requirements: meets all four criteria

✅ Database – strorage and processing of data in a database.

✅ CRUD operations – ability to create, read, update and delete entities.

✅ Git and commits – version control usage (GitHub/GitLab).

✅ Docker – containerization of the project.

### What is Not Implemented but Planned:

1. **Push Notifications & Reminders**  
- Send daily push notifications or emails reminding users to complete their activities.  
- Could integrate with a service like OneSignal, Firebase, or just send mock emails for now.

2. **Achievements / Badges**  
- Reward users for hitting milestones (e.g., 7-day streak, 30-day streak).  
- Show badges on user profiles or a dedicated achievements section (Bronze, Silver, Gold).

3. **Weekly/Monthly Progress Tracking**  
- Instead of (or in addition to) daily streaks, track weekly XP or monthly completion rates.  
- Provide progress bars for how close a user is to a weekly or monthly goal.

4. **Friend Requests / Accept/Reject**  
- Right now, adding a friend is immediate. Introduce an optional friend request flow would make it more social:  
    - `POST /api/friends/request` → sends a friend request  
    - `POST /api/friends/accept` → accept or decline

5. **Subscriptions / Premium Membership**  
- Add a simple subscription system (e.g., storing `is_premium`) with special benefits:  
    - More streak freezes, advanced analytics, or custom friend groups.

6. **Leaderboards by Activity or Time Range**  
- Currently there is a single leaderboard for all activities. Possible to add:  
    - **Filters**: “Show top streaks in Leetcode vs. Meditation.”  
    - **Date Range**: “Who has done the most completions this week/month?”

7. **Scheduled Tasks / Background Jobs**  
- `BackgroundTasks` (FastAPI’s built-in) or something like Celery / RQ for deeper scheduling:  
    - Automatic streak resets each day at midnight  
    - Automated push notifications or emails for missed days

### Potential Extension Ideas

1. **AI-Powered Recommendations** *(optional)*  
   - Suggest new activities, personal motivational messages, or analyze usage patterns.  
   - Could integrate an LLM (OpenAI, etc.) or a smaller model for local inference.

2. **Better Avatars**  
   - Currently you support file uploads. You could expand to:  
     - Thumbnails, scaling, or a 3rd-party image host.  
     - Automatic fallback to a user’s old avatar on error.

3. **Additional Security / Rate Limiting**  
    - Add rate limiting or advanced security measures (e.g., 2FA, password reset flows) for a more production-ready environment.