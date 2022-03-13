CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
DROP DATABASE IF EXISTS lightchan;
CREATE DATABASE lightchan;

CREATE TABLE board (
    id TEXT NOT NULL
    board_name TEXT,
    board_description TEXT,
    nsfw Boolean,
    mnemonic TEXT
);

INSERT INTO board (id, board_name, board_description, nsfw, mnemonic) VALUES ('man', 'main', 'General Discussion', false, 'man');

INSERT INTO board (id, board_name, board_description, nsfw, mnemonic) VALUES ('mus', 'music', 'Music, Bands, Concerts', false, 'mus');

INSERT INTO board (id, board_name, board_description, nsfw, mnemonic) VALUES ('art', 'art', 'Art and Artists', false, 'art');

INSERT INTO board (id, board_name, board_description, nsfw, mnemonic) VALUES ('lit', 'literature', 'All Things Literature', false, 'lit');

INSERT INTO board (id, board_name, board_description, nsfw, mnemonic) VALUES ('tec', 'technology', 'Technology Discussion', false, 'tec');

CREATE TABLE comment (
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
	    REFERENCES board(id)
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