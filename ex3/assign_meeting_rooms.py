def assign_meeting_rooms(meetings):
    if not meetings:
        return {
            "rooms_needed": 0,
            "rooms_assigned": {}
        }

    meetings.sort()

    rooms = {}

    for meeting in meetings:
        start, end = meeting
        assigned = False

        for room in rooms:
            last_end = rooms[room][-1][1]

            if start >= last_end:
                rooms[room].append(meeting)
                assigned = True
                break

        if not assigned:
            room_id = len(rooms)
            rooms[room_id] = [meeting]

    return {
        "rooms_needed": len(rooms),
        "rooms_assigned": rooms
    }


meetings = [
    [9, 10],
    [9, 12],
    [11, 13]
]

result = assign_meeting_rooms(meetings)

print(result)

meetings = [
    [9, 10],
    [9, 12],
    [11, 13]
]

result = assign_meeting_rooms(meetings)

print(result)
meetings = [
    [9, 10],
    [9, 12],
    [11, 13]
]

result = assign_meeting_rooms(meetings)

print("Rooms needed:", result["rooms_needed"])

for room, schedule in result["rooms_assigned"].items():
    print(f"Room {room}: {schedule}")