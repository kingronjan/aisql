## Context

The system currently exists as a backend service/library without an external API layer. To support user interactions and protect data, we need an authentication layer. This design introduces a web API framework and a robust authentication system.

## Goals / Non-Goals

**Goals:**
- Introduce FastAPI as the web framework for the backend.
- Implement `/auth/register` and `/auth/login` endpoints.
- Securely hash and store user passwords.
- Use JWT for stateless session management.
- Provide a dependency/middleware for verifying JWTs on protected routes.

**Non-Goals:**
- Implementing a frontend UI (will be handled separately).
- Complex Role-Based Access Control (RBAC) - focus on basic user identification.
- Support for multiple authentication providers (e.g., Google OAuth).

## Decisions

- **FastAPI**: Selected for its performance, ease of use with Pydantic, and automatic OpenAPI documentation.
- **JWT (PyJWT)**: Standard for stateless authentication. Simple to implement and scale.
- **Passlib[bcrypt]**: Industry-standard library for password hashing.
- **SQLAlchemy**: Will be used as the ORM to manage the `users` table and handle database interactions securely.
- **Database Schema**:
    - `users` table: `id` (int), `username` (str, unique), `hashed_password` (str), `created_at` (datetime).

## Risks / Trade-offs

- **[Risk] JWT Secret Compromise** → **[Mitigation]** The JWT secret MUST be stored in the `.env` file and never committed to version control. Rotatable keys can be supported in the future.
- **[Risk] SQL Injection** → **[Mitigation]** Use SQLAlchemy ORM or parameterized queries for all database interactions.
- **[Trade-off] Statelessness** → Using JWT means we cannot easily revoke tokens before they expire without a blacklist (not planned for now to keep it simple).
