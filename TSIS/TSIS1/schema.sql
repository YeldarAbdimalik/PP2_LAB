DROP TABLE IF EXISTS phones;
DROP TABLE IF EXISTS contacts;
DROP TABLE IF EXISTS groups;

-- GROUPS
CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- CONTACTS
CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    birthday DATE,
    group_id INTEGER REFERENCES groups(id)
);

-- PHONES
CREATE TABLE phones (
    id SERIAL PRIMARY KEY,
    contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
    phone VARCHAR(20),
    type VARCHAR(10) CHECK (type IN ('home','work','mobile'))
);