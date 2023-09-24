create table users
(
    user_id      integer not null
        constraint user_pk
            primary key autoincrement,
    username     text    not null,
    useremail    text    not null,
    userpassword text    not null
);


create table artists
(
    artist_id   integer not null
        constraint artists_pk
            primary key autoincrement,
    artist_name text    not null,
    hometown    text,
    genre       text,
    description text,
    user_id     integer not null
        constraint artists_fk
            references users
);


create table venues
(
    venue_id          integer not null
        constraint venues_pk
            primary key autoincrement,
    venue_name        text    not null,
    venue_address     text    not null,
    venue_description text,
    max_capacity      integer,
    user_id           integer not null
        constraint venues_fk
            references users
);


create table events
(
    event_id          integer not null
        constraint events_pk
            primary key autoincrement,
    event_name        text    not null,
    event_date        text    not null,
    event_description text,
    venue_id          integer not null
        constraint venue_fk
            references venues,
    artist_id         integer not null
        constraint artists_fk
            references artists,
    user_id           integer not null
        constraint users_fk
            references venues (user_id)
);


