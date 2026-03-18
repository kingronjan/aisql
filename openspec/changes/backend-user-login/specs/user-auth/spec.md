## ADDED Requirements

### Requirement: User Registration
The system SHALL allow new users to register with a unique username and a password. Passwords MUST be hashed before storage.

#### Scenario: Successful Registration
- **WHEN** a user provides a unique username and a password
- **THEN** the system SHALL create a new user record and return a success message

#### Scenario: Duplicate Username Registration
- **WHEN** a user provides a username that already exists
- **THEN** the system SHALL return an error message indicating the username is taken

### Requirement: User Login
The system SHALL allow registered users to authenticate with their username and password.

#### Scenario: Successful Login
- **WHEN** a user provides correct username and password
- **THEN** the system SHALL return a valid JWT (JSON Web Token)

#### Scenario: Failed Login with Incorrect Password
- **WHEN** a user provides a correct username but incorrect password
- **THEN** the system SHALL return an authentication failure message

#### Scenario: Failed Login with Non-existent User
- **WHEN** a user provides a username that does not exist
- **THEN** the system SHALL return an authentication failure message

### Requirement: Token Verification
The system SHALL verify the JWT provided in the Authorization header for protected endpoints.

#### Scenario: Successful Token Verification
- **WHEN** a user provides a valid JWT in the Authorization header
- **THEN** the system SHALL allow access to the protected endpoint

#### Scenario: Failed Token Verification with Invalid Token
- **WHEN** a user provides an invalid or expired JWT
- **THEN** the system SHALL return an unauthorized error message
