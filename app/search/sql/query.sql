SELECT
    event.name event_name,
    event.text event_text,
    event.place event_place,
    event.image event_image,
    event.id event_id,
    event.period event_period,
    event."startDate" event_start_date,
    event."endDate" event_end_date,
    channel.name channel_name,
    (SELECT
        COUNT(sub_event_assignations."eventId") counter
    FROM
        "EventAssignations" sub_event_assignations, "Event" sub_event
    WHERE
        sub_event_assignations."createdAt" > (now() - interval '1 day')
        AND sub_event_assignations."eventId" = sub_event.id) counter,
    array_agg(tags.name) tags_names
FROM
    "Event" event
LEFT OUTER JOIN "Channel" channel ON
    event."channelId" = channel.id
LEFT OUTER JOIN "EventTags" event_tags ON
    event.id = event_tags."eventId"
LEFT OUTER JOIN "Tags" tags ON
    tags.id = event_tags."tagId"
GROUP BY
    event.name,
    event.text,
    event.place,
    event."startDate",
    event.id,
    channel.name