## 1. Environment and Base Setup

- [ ] 1.1 Add `fastapi`, `uvicorn`, `pyjwt`, `passlib[bcrypt]`, and `sqlalchemy` to `apps/backend/pyproject.toml`.
- [ ] 1.2 Update `apps/backend/aisql/settings.py` to include `jwt_secret` and `algorithm` (default "HS256").
- [ ] 1.3 Create `apps/backend/aisql/database.py` to set up SQLAlchemy engine and session management.

## 2. Data Models and Schemas

- [ ] 2.1 Define the `User` SQLAlchemy model in `apps/backend/aisql/models.py` (id, username, hashed_password).
- [ ] 2.2 Define Pydantic schemas in `apps/backend/aisql/schemas.py` for `UserCreate`, `UserRead`, and `Token`.

## 3. Security and Authentication Utilities

- [ ] 3.1 Implement `get_password_hash` and `verify_password` using `passlib` in `apps/backend/aisql/security.py`.
- [ ] 3.2 Implement `create_access_token` using `PyJWT` in `apps/backend/aisql/security.py`.

## 4. API Implementation

- [ ] 4.1 Create the main FastAPI application instance in `apps/backend/aisql/main.py`.
- [ ] 4.2 Implement the `/auth/register` endpoint to create new users.
- [ ] 4.3 Implement the `/auth/login` endpoint to authenticate users and issue JWTs.
- [ ] 4.4 Implement a `get_current_user` FastAPI dependency to protect routes.

## 5. Verification and Testing

- [ ] 5.1 Create an integration test in `apps/backend/tests/test_auth.py` covering registration, login, and protected route access.
- [ ] 5.2 Verify password hashing is working correctly and tokens expire as expected.
