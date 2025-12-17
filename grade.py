from pyscript import display, document

# function to calculate general weighted average when button clicked
def general_weighted_average(e):
    # get first and last name from input boxes
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

    # get grades from input boxes
    math = float(document.getElementById('math').value)
    sci = float(document.getElementById('sci').value)
    eng = float(document.getElementById('eng').value)
    fil = float(document.getElementById('fil').value)
    ict = float(document.getElementById('ict').value)
    pe = float(document.getElementById('pe').value)

    # list of subjects and units
    subj = ['Math', 'Science', 'English', 'Filipino', 'ICT', 'PE']
    units_subject = (5, 3, 2, 1)

    # make summary text of grades
    summary = f"""{subj[0]}: {math:.0f}
    {subj[1]}: {sci:.0f}
    {subj[2]}: {eng:.0f}
    {subj[3]}: {fil:.0f}
    {subj[4]}: {ict:.0f}
    {subj[5]}: {pe:.0f}
    """

    # calculate weighted average
    weighted_sum = (math * 5 + sci * 5 + eng * 5 + fil * 3 + ict * 2 + pe * 1)
    total_units = (5 * 3) + 3 + 2 + 1
    gwa = weighted_sum / total_units

    # show results in page
    display(f'Name: {first_name} {last_name}', target="student_info")
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')
