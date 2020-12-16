create table users
(
    id         integer primary key NOT NULL,
    first_name varchar(100),
    last_name  varchar(100),
    lang       varchar(2)
);

create table matches
(
    id          integer UNIQUE NOT NULL,
    time        timestamp,
    team_1      varchar(100)   NOT NULL,
    team_2      varchar(100)   NOT NULL,
    liga        varchar(5)     NOT NULL,
    lang        varchar(2)     NOT NULL,
    is_canceled boolean,
    primary key (team_1, team_2, lang)
);


create table match_notifications
(
    user_id  integer,
    match_id integer,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (match_id) REFERENCES matches (id)
);