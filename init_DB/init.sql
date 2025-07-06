DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS payments;

----- USERS TABLE
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_id BIGINT UNIQUE NOT NULL,
    username TEXT,
    message_timestamp TIMESTAMP WITH TIME ZONE NOT NULL
);

----- PAYMENTS TABLE 
"CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    telegram_username BIGINT NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    amount NUMERIC(10, 2),
    status TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);"
