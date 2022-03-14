CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
DROP DATABASE IF EXISTS lightchan;
CREATE DATABASE lightchan;

CREATE TABLE Board (
    id TEXT NOT NULL UNIQUE,
    board_name TEXT,
    board_description TEXT,
    nsfw Boolean,
    PRIMARY KEY (id), 
    mnemonic TEXT NOT NULL UNIQUE
);

-- INSERT INTO Board (id, board_name, board_description, nsfw, mnemonic) VALUES ('man', 'main', 'General Discussion', false, 'man');

-- INSERT INTO Board (id, board_name, board_description, nsfw, mnemonic) VALUES ('mus', 'music', 'Music, Bands, Concerts', false, 'mus');

-- INSERT INTO Board (id, board_name, board_description, nsfw, mnemonic) VALUES ('art', 'art', 'Art and Artists', false, 'art');

-- INSERT INTO Board (id, board_name, board_description, nsfw, mnemonic) VALUES ('lit', 'literature', 'All Things Literature', false, 'lit');

-- INSERT INTO Board (id, board_name, board_description, nsfw, mnemonic) VALUES ('tec', 'technology', 'Technology Discussion', false, 'tec');

CREATE TABLE Comment (
    id uuid DEFAULT uuid_generate_v4 () UNIQUE,
    clean_id TEXT NOT NULL,
    title TEXT,
    content TEXT,
    file_name TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    votes INT NOT NULL,
    PRIMARY KEY (id),
    mnemonic TEXT NOT NULL,
    CONSTRAINT fk_owner
      FOREIGN KEY(mnemonic) 
	    REFERENCES board(mnemonic)
);

CREATE TABLE Reply (
    id uuid DEFAULT uuid_generate_v4 () UNIQUE,
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