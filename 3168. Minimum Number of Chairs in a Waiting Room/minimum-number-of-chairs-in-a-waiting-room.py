class Solution:
    def minimumChairs(self, s: str) -> int:
        chair = 0
        person_in_room = 0
        for event in s:
            if event == 'E':
                person_in_room += 1
            elif event == 'L':
                person_in_room -= 1
            if person_in_room > chair:
                chair += 1
        return chair 
