

⚡ Fast Track Setup

Step 1: Clone and Navigate

```bash
git clone https://github.com/<your-username>/post-conversation-analysis.git
cd post-conversation-analysis
```

Step 2: Run Setup Script (Linux/Mac)

```bash
chmod +x setup.sh
./setup.sh
```

### Step 3: Configure Environment

Edit `.env` file:

```env
DB_NAME=conversation_analysis
DB_USER=postgres
DB_PASSWORD=your_password
SECRET_KEY=your-django-secret-key
```

Step 4: Start Server

```bash
python manage.py runserver
```

---

Windows Setup

 Step 1: Create Virtual Environment

```cmd
python -m venv venv
venv\Scripts\activate
```

 Step 2: Install Dependencies

```cmd
pip install -r requirements.txt
python -m textblob.download_corpora
```

Step 3: Setup Database

For SQLite (easiest):

Edit `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Step 4: Run Migrations

```cmd
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

 Step 5: Start Server

```cmd
python manage.py runserver
```

---

Testing the API

Option 1: Use the Test Script

```bash
python test_api.py
```

Option 2: Manual Testing with cURL

Create a conversation:

```bash
curl -X POST http://127.0.0.1:8000/api/conversations/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Test Chat",
    "messages": [
      {"sender": "user", "message": "Hello"},
      {"sender": "ai", "message": "Hi! How can I help?"},
      {"sender": "user", "message": "I need support"},
      {"sender": "ai", "message": "I understand. Let me help you with that."}
    ]
  }'
```

Analyze the conversation:

```bash
curl -X POST http://127.0.0.1:8000/api/analyse/ \
  -H "Content-Type: application/json" \
  -d '{"conversation_id": 1}'
```
 Get the report:

```bash
curl http://127.0.0.1:8000/api/reports/
```

Option 3: Use Postman

1. Import the API endpoints
2. Create a conversation (POST)
3. Analyze it (POST)
4. View reports (GET)

---

 Setting Up Cron Jobs

Linux/Mac

```bash
# Add cron jobs
python manage.py crontab add

# Verify they're added
python manage.py crontab show

# Test manually
python manage.py analyze_conversations
```

Windows (Task Scheduler)

1. Open Task Scheduler
2. Create Basic Task
3. Set trigger: Daily at 12:00 AM
4. Action: Start a program
5. Program: `C:\path\to\venv\Scripts\python.exe`
6. Arguments: `C:\path\to\manage.py analyze_conversations`

---

 📊 Accessing the Admin Panel

1. Visit: http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. View and manage:
   - Conversations
   - Messages
   - Analysis Results

---

🔍 Project Structure

```
your-project/
├── conversation_project/     # Main Django project
│   ├── settings.py          # Configure here
│   └── urls.py
├── analysis/                # Main app
│   ├── models.py           # Database models
│   ├── views.py            # API endpoints
│   ├── analyzer.py         # Analysis logic
│   ├── serializers.py      # Data serializers
│   └── management/
│       └── commands/
│           └── analyze_conversations.py  # Cron command
├── requirements.txt        # Dependencies
├── manage.py              # Django CLI
└── README.md             # Full documentation
```

---

Key Files to Customize

1. `analysis/analyzer.py`
- Add your own analysis parameters
- Customize scoring logic
- Integrate with external APIs

2. `settings.py`
- Database configuration
- Cron schedule
- Security settings

3. `analysis/models.py`
- Add more analysis fields
- Change data structure

---

Common Tasks

Run analysis manually
```bash
python manage.py analyze_conversations
```

Force re-analyze everything
```bash
python manage.py analyze_conversations --force
```
Check cron logs
```bash
tail -f /tmp/cron_analysis.log
```

 Create sample data
```bash
python manage.py shell
>>> from analysis.models import Conversation, Message
>>> # Create test conversations
```

---

Troubleshooting

"Module not found" error
```bash
pip install -r requirements.txt
```

Database connection error
- Check PostgreSQL is running: `sudo systemctl status postgresql`
- Verify `.env` credentials

Cron not running
```bash
# Check if cron service is active
sudo systemctl status cron

# Re-add cron jobs
python manage.py crontab remove
python manage.py crontab add
```

 Port already in use
```bash
# Use a different port
python manage.py runserver 8001
```
📈 Next Steps

1. **Customize Analysis**: Modify `analyzer.py` to add
2. **Add Authentication**: Implement JWT or OAuth
3. **Deploy**: Use Gunicorn + Nginx for production
4. **Add Celery**: For heavy processing tasks
5. **Create Dashboard**: Build a frontend with React/Vue

 Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [TextBlob Documentation](https://textblob.readthedocs.io/)
- [Cron Syntax](https://crontab.guru/)

Submission Checklist

- [ ] Code pushed to GitHub
- [ ] README.md complete with setup instructions
- [ ] requirements.txt included
- [ ] .env.example provided
- [ ] All API endpoints working
- [ ] Cron job configured and tested
- [ ] Sample data tested
- [ ] Admin panel accessible
- [ ] Optional: Loom video recorded



**Need Help?** Open an issue on GitHub or contact the team.

**Good luck with your internship! 🎉**
