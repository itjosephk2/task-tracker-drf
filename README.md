
# Task Tracker Front-End

This is the front-end React application for the **Task Tracker** project, built as part of the Advanced Front-End Portfolio Project for the Code Institute Full-Stack Software Development diploma.

[Back-End Repository](https://github.com/itjosephk2/task-tracker-drf)

## Project Purpose

Task Tracker is a productivity application that allows users to:

- Register and log in securely.
- View, create, update, and delete tasks.
- Mark tasks as completed.
- Access a fully responsive, accessible UI built with React and Bootstrap.

---

## Live Site

- Frontend: [Heroku Frontend App](https://task-traker-react-494a1f4ec4cd.herokuapp.com/)
- Backend API: [Heroku API](https://task-tracker-drf-e7e43a44f5b5.herokuapp.com/api/)

---

##  Technologies Used

- React.js
- React Router
- Axios
- Bootstrap 5
- Django REST Framework (Back-End)
- Heroku (Deployment)

---

## Features

- **Authentication**: User signup, login, and logout.
- **Task Management (CRUD)**:
  - Create a task with title, description, and due date.
  - Read/view task details.
  - Update tasks using an edit form.
  - Delete tasks with confirmation.
  - Mark task as completed using a PATCH request.
- **Routing**: Protected routes based on login state.
- **Feedback**: Alerts and validation for form errors and success.
- **Responsive Design**: Mobile-friendly and accessible.
- **UX Enhancements**: Loading indicators, navigation feedback.

---

## UX & UI Design

- Wireframes and mockups designed before implementation.
- Accessible forms and keyboard-navigable UI.
- Buttons and navigation are always visible or accessible on relevant pages.
- Current login state is visible and can log out from any page.

---

##  Manual Testing

Manual testing has been completed for the following:

- Navigation works as expected (Login → Home → View → Edit).
- Login/Logout functionality updates state correctly.
- Form validation triggers on empty submissions.
- All CRUD operations provide expected feedback.
- Invalid actions (e.g., editing another user's task) are blocked via API.
- API data is correctly rendered and updated.

Test cases and results are documented in the [Testing Section](#testing).

---

## Deployment

Deployed using Heroku:

Frontend deployed with static build via Heroku (Node.js buildpack).

## Deployment (Heroku)

1. Create Heroku app:
```bash
heroku create your-app-name
```

2. Deploy to Heroku:
```bash
git push heroku main
```

REACT_APP_API_BASE_URL=https://task-tracker-drf-e7e43a44f5b5.herokuapp.com/api/

---

## File Structure

- `src/components/`: All modular React components (Login, Signup, Home, Tasks).
- `src/api.js`: Central location for API URL and auth header helper.
- `src/App.js`: Route manager using React Router v6.
- `src/index.js`: App entry point.

---

## Testing

| Feature Tested          | Result |
|-------------------------|--------|
| Login/Logout Flow       | ✅ Pass |
| Register New User       | ✅ Pass |
| Create Task             | ✅ Pass |
| Edit Task               | ✅ Pass |
| Delete Task             | ✅ Pass |
| Mark as Completed       | ✅ Pass |
| Navigation/Routes       | ✅ Pass |
| Responsive Design       | ✅ Pass |

---

## Future Enhancements

- Filter/sort tasks by due date and completion.
- Create task list groups and priority
- Follow Users and make tasks list groups private or public

---

## Acknowledgements

Thanks to Code Institute and the React/Django DRF communities for the walkthroughs, guidance, and support throughout this journey.
