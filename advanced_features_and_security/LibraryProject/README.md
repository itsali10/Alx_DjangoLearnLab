# LibraryProject

This Django application demonstrates advanced backend features with a strong emphasis on security and role-based access control. It was developed for the ALX “Advanced Features and Security” project.

## 🔧 Features Implemented

- **Custom User Model** using `AbstractUser` with additional fields:
  - `date_of_birth`
  - `profile_photo`
- **Role-Based Access Control** using Django groups and custom permissions:
  - `can_view`, `can_create`, `can_edit`, `can_delete`
- **Permission-Restricted Views** with `@permission_required(..., raise_exception=True)`
- **Secure Configuration**:
  - CSRF Protection
  - HTTPS Redirects
  - Secure Headers

## 📁 Setup Instructions

1. **Clone the Repo**  
   ```bash
   git clone https://github.com/<your-username>/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/advanced_features_and_security
