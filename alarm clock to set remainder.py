import datetime

class Alarm:
    def __init__(self, alarm_id, time, message):
        self.alarm_id = alarm_id
        self.time = time
        self.message = message

class AlarmClock:
    def __init__(self):
        self.alarms = []
        self.next_id = 1

    def set_alarm(self):
        try:
            time_str = input("Enter alarm time (YYYY-MM-DD HH:MM:SS): ")
            message = input("Enter alarm message: ")
            alarm_time = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
            alarm = Alarm(self.next_id, alarm_time, message)
            self.alarms.append(alarm)
            self.next_id += 1
            print("Alarm set successfully!")
        except ValueError:
            print("Invalid date format. Please try again.")

    def delete_alarm(self):
        try:
            alarm_id = int(input("Enter alarm ID to delete: "))
            self.alarms = [alarm for alarm in self.alarms if alarm.alarm_id != alarm_id]
            print("Alarm deleted successfully!")
        except ValueError:
            print("Invalid ID format. Please enter a number.")

    def display_alarms(self):
        if not self.alarms:
            print("No alarms set.")
    alarm_clock.run()