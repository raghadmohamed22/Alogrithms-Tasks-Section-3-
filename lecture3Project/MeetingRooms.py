import heapq


def min_meeting_rooms(meetings):
    if not meetings:
        return 0

    meetings.sort(key=lambda x: x[0])

    end_times_heap = []


    heapq.heappush(end_times_heap, meetings[0][1])

   
    for start, end in meetings[1:]:
        if start >= end_times_heap[0]:
            heapq.heappop(end_times_heap) 

        
        heapq.heappush(end_times_heap, end)

    return len(end_times_heap)


meetings_1 = [(0, 30), (5, 10), (15, 20)]
meetings_2 = [(7, 10), (2, 4)]
meetings_3 = [(1, 5), (2, 6), (4, 8), (9, 12)]

print("Example 1 minimum rooms:", min_meeting_rooms(meetings_1)) 
print("Example 2 minimum rooms:", min_meeting_rooms(meetings_2))  
print("Example 3 minimum rooms:", min_meeting_rooms(meetings_3))  