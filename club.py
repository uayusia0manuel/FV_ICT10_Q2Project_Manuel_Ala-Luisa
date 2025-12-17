#import stuff from pyscript
from pyscript import display, document

# dictionary of club short names to full names
clubs = {
    "mb": "Marching Band",
    "gc": "Glee Club",
    "dc": "Dance Club",
    "mc": "Math Club",
    "sc": "Science Club",
    "cac": "Communications Arts Club",
    "cocc": "COCC",
    "ss": "Social Science Club",
    "vb": "Volleyball Varsity",
    "bb": "Basketball Varsity"
}

# dictionary with info for each club
club_info = {
    "Marching Band": {
        "Description": "Develops intrumental music skills and techniques.",
        "Meeting Time": "Tuesday and Wednesday (03:00-04:30 PM)",
        "Location": "Band Room",
        "Club Moderator": "Mr. Emilio Alumno",
        "Number of Members": 30
    },
    "Glee Club": {
        "Description": "Enhances vocal performance and choral singing.",
        "Meeting Time": "Monday (03:00-05:00 PM)",
        "Location": "High School Music Room",
        "Club Moderator": "Mr. Denver Martin",
        "Number of Members": 25
    },
    "Dance Club": {
        "Description": "Enhances dance skills and stage presence.",
        "Meeting Time": "Tuesday (03:00-05:00 PM)",
        "Location": "Teatro Preciosa",
        "Club Moderator": "Mr. Alfred Cases",
        "Number of Members": 27
    },
    "Math Club": {
        "Description": "Teaches techniques in solving mathematical equations.",
        "Meeting Time": "Monday (02:30-03:00 PM)",
        "Location": "Room 404",
        "Club Moderator": "Mr. Nicole Gabuya",
        "Number of Members": 22
    },
    "Science Club": {
        "Description": "Encourages scientific curiosity and experimentation.",
        "Meeting Time": "Tuesday (03:00-04:00 PM)",
        "Location": "Room 404",
        "Club Moderator": "Ms. Jameelyn Maramag",
        "Number of Members": 20
    },
    "Communications Arts Club": {
        "Description": "Develops communication and media skills.",
        "Meeting Time": "Wednesday and Friday (03:00-04:00 PM)",
        "Location": "Room 406",
        "Club Moderator": "Ms. Yannis Fernandez",
        "Number of Members": 20
    },
    "COCC": {
        "Description": "Trains students in leadership and discipline.",
        "Meeting Time": "Wednesday (02:30-04:30 PM)",
        "Location": "Quadrangle / Teatro Preciosa",
        "Club Moderator": "SSgt. Jemima David PA (Res)",
        "Number of Members": 28
    },
    "Social Science Club": {
        "Description": "Explores social studies and current events.",
        "Meeting Time": "Tuesday (03:00-04:00 PM)",
        "Location": "Room 409",
        "Club Moderator": "Mr. Roberto Lim",
        "Number of Members": 21
    },
    "Volleyball Varsity": {
        "Description": "Develops volleyball skills and teamwork.",
        "Meeting Time": "Wednesday (03:00-04:00 PM)",
        "Location": "Quadrangle",
        "Club Moderator": "Mr. Adrian Ruiz",
        "Number of Members": 24
    },
    "Basketball Varsity": {
        "Description": "Develops basketball skills and teamwork.",
        "Meeting Time": "Monday (03:00-04:00 PM)",
        "Location": "Quadrangle",
        "Club Moderator": "Mr. Adrian Ruiz",
        "Number of Members": 24
    }
}

# function to show info about selected club
def get_club(e):
    # get selected club short name from dropdown
    yours = document.querySelector("select").value

    # check if selection is valid
    if yours in clubs:
        club_name = clubs[yours] # get full name
        info = club_info[club_name] # get info for that club

        # show info on page
        display(f"Club Name: {club_name}", target="output")
        display(f"Description: {info['Description']}", target="output")
        display(f"Meeting Time: {info['Meeting Time']}", target="output")
        display(f"Location: {info['Location']}", target="output")
        display(f"Club Moderator: {info['Club Moderator']}", target="output")
        display(f"Number of Members: {info['Number of Members']}", target="output")
    
    # if no club was selected
    else:
        display("Please select a club.", target="output")
