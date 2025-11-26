CREATE TABLE IF NOT EXISTS players (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    position TEXT,
    team TEXT,
    rating INT
);

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    passw TEXT,
    roles TEXT[],
    jwt_token INT
);

INSERT INTO players (name, position, team, rating) VALUES
('Kamacho', 'forward', 'Sizam', 95),
('Gabba', 'defendsman', 'Mitino',  93),
('Tugi', 'goalkeeper','Zian',  89);

INSERT INTO users (name, passw, roles) VALUES
('admin', '1111', ARRAY['admin', 'moderator']),
('tugi', '0000', ARRAY[]::TEXT[]);