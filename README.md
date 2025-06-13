# 🛠️ Alt-school-second-semester-project
### Prepared By Kazeem Asifat: ALT/SOE/024/1821

![AltSchool](https://img.shields.io/badge/AltSchool-Backend-blue)
![Made with FastAPI](https://img.shields.io/badge/FastAPI-0.115.12-green)
![Python ≥ 3.10](https://img.shields.io/badge/Python-3.10%2B-yellow)

## 🧾 Project Description
This is a Python project that allow users to register for events, track attendance, and manage both event information and speaker details.

## ⚙️ Libraries Used
  - Fast API
  - Pydantic
  - UUID4

## ✨ What you can do

[//]: # (🔄)
| Feature                                                     | Routes                            | Status             |
|-------------------------------------------------------------|-----------------------------------|--------------------|
| **List all users**                                          | `GET /users/all`                  | ✅ Tested & Trusted |
| **List specific user**                                      | `GET /users/details/{id}`         | ✅ Tested & Trusted |
| **Create users**                                            | `POST /users/create`              | ✅ Tested & Trusted |
| **Update a user**                                           | `PATCH /users/update/{id}`        | ✅ Tested & Trusted |
| **Deactivate a user**                                       | `PATCH /users/delete/{id}`        | ✅ Tested & Trusted |
| **List all events**                                         | `GET /events/list`                | ✅ Tested & Trusted |
| **Get single event**                                        | `GET /events/details/{id}`        | ✅ Tested & Trusted |
| **Create event**                                            | `POST /events/create`             | ✅ Tested & Trusted |
| **Update an event**                                         | `PATCH /events/update/{id}`       | ✅ Tested & Trusted |
| **Close an event**                                          | `PATCH /events/close/{id}`        | ✅ Tested & Trusted |
| **Assign single/multiple speakers to an event**             | `POST /events/assign-speaker`      |✅ Tested & Trusted|
| **List the speakers of an event**                           | `GET /events/speakers/{event_id}` | ✅ Tested & Trusted |
| **List pre-populated speakers**                             | `GET /speakers/list`              | ✅ Tested & Trusted |
| **Register user for an event, the event must be open**      |                                   | 🔄 In pipeline     |
| **Only active users can register**                          |                                   | 🔄 In pipeline     |
| **Users cannot register more than once for the same event** |                                   | 🔄 In pipeline     |
| **Mark attendance**                                         |                                   | 🔄 In pipeline     |
| **View registration for specific user**                     |                                   | 🔄 In pipeline     |
| **View all regitstrations**                                 |                                   | 🔄 In pipeline     |
| **Filter users who attended at least one event**            |                                   | 🔄 In pipeline     |

---

## 🚀 Setup for local development or testing

```bash
# 1. Clone & move in
git clone https://github.com/Kazeeem/Alt-school-second-semester-project.git
cd Alt-school-second-semester-project
```

```bash
# 2. Create env & install dependencies
python -m venv venv && source .venv/bin/activate
pip install -r requirements.txt
```

```bash
# 3. Run dev server
uvicorn main:app --reload
```

```bash
# 4. Open docs
# 👉 http://127.0.0.1:8000/docs
- Copy and paste the URL below into your browser
```
