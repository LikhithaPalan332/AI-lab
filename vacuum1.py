# Vacuum Cleaner Agent with Location, Status and Percentage

def vacuum_cleaner():
    location = 'A'
    state = {'A': 'Dirty', 'B': 'Dirty'}
    cleaned_count = 0
    total_rooms = 2

    print(f"{'Step':<5}{'Location':<10}{'Status':<15}{'Percent'}")
    print("-" * 45)

    for step in range(1, 5):

        if state[location] == 'Dirty':
            state[location] = 'Clean'
            cleaned_count += 1
        else:
            if location == 'A':
                location = 'B'
            else:
                location = 'A'

        # Overall status
        if state['A'] == 'Clean' and state['B'] == 'Clean':
            status = "Cleaned"
        else:
            status = "Not Cleaned"

        # Performance percentage
        percent = int((cleaned_count / total_rooms) * 100)

        print(f"{step:<5}{location:<10}{status:<15}{percent}%")


vacuum_cleaner()
