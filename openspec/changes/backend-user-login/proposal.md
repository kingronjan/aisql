## Why

Currently, the system lacks user authentication. We need to implement a secure backend login to protect sensitive data and provide personalized experiences. This is a foundational step for multi-user support and API security.

## What Changes

- Implement a new login endpoint (`/auth/login`) that accepts username and password.
- Implement user password hashing and verification using `passlib`.
- Use JWT (JSON Web Tokens) for stateless session management.
- Update the database schema to include a `users` table.

## Capabilities

### New Capabilities
- `user-auth`: Covers user registration, login, and token verification. Provides secure access to the API.

### Modified Capabilities
<!-- No existing capabilities listed in openspec/specs/. -->

## Impact

- **Backend**: New modules for authentication and user management.
- **Database**: New `users` table required in the database specified by `db_conn_str`.
- **Dependencies**: Added dependencies for JWT (e.g., `PyJWT` or `python-jose`) and password hashing (e.g., `passlib[bcrypt]`).
