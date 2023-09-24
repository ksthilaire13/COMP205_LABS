-- shows which events artists will be preforming at
select event_name, event_date, artist_name from events
join artists a on events.artist_id = a.artist_id
order by artist_name;

-- shows max capacity at different events
select e.event_name, e.event_date, v.venue_address, v.max_capacity
from events e
join venues v on e.venue_id = v.venue_id
order by e.event_name;