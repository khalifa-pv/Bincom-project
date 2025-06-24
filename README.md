# 📸 SnapShelf – A Django Image Gallery

SnapShelf is a simple Django-based multimedia image gallery that allows users to:
- View a styled gallery of images 📷
- Upload images (with title) 🖼️
- Delete images (if logged in) ❌
- View and download images in a modern modal view 🔍
- Register and login/logout as a user (with validation) 🔐

---

## 🚀 Deployment Status

I attempted to deploy SnapShelf to **Heroku**. However, I was unable to complete the deployment due to **card verification limitations on Heroku**.

Instead, I have made the source code and setup instructions available via:
- [GitHub Repository](https://github.com/khalifa-pv/Bincom-project.git)
- Google Drive folder (contains project files zipped and ready to run)

---

## 💻 How to Run Locally

Follow the steps below to run SnapShelf on your local machine:

### 1. Clone the Repository

```bash
https://github.com/khalifa-pv/Bincom-project.git
cd multimedia_site

2. (Optional) Create and Activate a Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate     # On Windows

3. Install Requirements
bash
Copy code
pip install -r requirements.txt

4. Run Migrations
bash
Copy code
python manage.py migrate

5. Start the Development Server
bash
Copy code
python manage.py runserver


Authentication Rules;
Uploading or deleting images requires login.

Viewing and downloading images is open to all.

Registration and login forms have field validation and popup messages for incorrect input.


Notes;
The site was designed with a modern interface using Bootstrap.

Heroku-ready files (like Procfile and runtime.txt) are included for future deployment.

No login is required to view or download images.

Registration supports username, email, password, and full validation.

