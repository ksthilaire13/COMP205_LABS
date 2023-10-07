-- shows which events artists will be preforming at
select event_name, event_date, artist_name from events
join artists a on events.artist_id = a.artist_id
order by artist_name;

-- shows max capacity at different events
select e.event_name, e.event_date, v.venue_address, v.max_capacity
from events e
join venues v on e.venue_id = v.venue_id
order by e.event_name;

-- shows all billy bakes events and dates
select e.event_name, e.event_date, a.artist_name
from event as e
    join artist_to_event as ae on e.event_id = ae.event_id
    join artist as a on ae.artist_id
where a.artist_name = "Billy Bakes"
order by a.artist_name;