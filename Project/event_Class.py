import uuid

class Event:
    events = {
        1: "Workshop on Python Programming",
        2: "Web Development Bootcamp",
        3: "Data Science Seminar"
    }
    enrollments = {}


    def display_events(self):
        print("Available Events:")
        for event_id, event_name in self.events.items():
            print(f"{event_id}. {event_name}")

   
    def enroll(self, event_id, name, email):
        if event_id in self.events:
            enrollment_id = str(uuid.uuid4())[:8]  
            self.enrollments[enrollment_id] = {
                "Enrollment ID" : enrollment_id,
                "Event": self.events[event_id],
                "Name": name,
                "Email": email
            }
            return enrollment_id
        else:
            return None