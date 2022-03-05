CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
DROP DATABASE IF EXISTS lightchan;
CREATE DATABASE lightchan;

CREATE TABLE comment (
    id uuid DEFAULT uuid_generate_v4 (),
    clean_id TEXT NOT NULL,
    title TEXT,
    content TEXT,
    file_name TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    votes INT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE reply (
    id uuid DEFAULT uuid_generate_v4 (),
    clean_id TEXT NOT NULL,
    title TEXT,
    content TEXT,
    file_name TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    votes INT NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_owner
      FOREIGN KEY(id) 
	    REFERENCES comment(id)
);