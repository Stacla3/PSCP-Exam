"""Phasmophobia"""
def main():
    """Start"""
    ghost = {"Banshee" : {"EMF Level 5", "Fingerprints", "Freezing Temperatures"},\
            "Demon" : {"Ghost Writing", "Spirit Box", "Freezing Temperatures"}\
            , "Jinn" : {"EMF Level 5", "Spirit Box", "Ghost Orb"}, \
            "Mare" : {"Freezing Temperatures", "Spirit Box", "Ghost Orb"}\
            , "Oni" : {"EMF Level 5", "Ghost Writing", "Spirit Box"}\
            , "Phantom" : {"EMF Level 5", "Freezing Temperatures", "Ghost Orb"}\
            , "Poltergeist" : {"Fingerprints", "Spirit Box", "Ghost Orb"}\
            , "Revenant" : {"EMF Level 5", "Ghost Writing", "Fingerprints"}\
            , "Shade" : {"EMF Level 5", "Ghost Writing", "Ghost Orb"}\
            , "Spirit" : {"Fingerprints", "Ghost Writing", "Spirit Box"}\
            , "Wraith" : {"Fingerprints", "Freezing Temperatures", "Spirit Box"}\
            , "Yurei" : {"Ghost Writing", "Freezing Temperatures", "Ghost Orb"}}
    text1, text2, text3 = str(input()), str(input()), str(input())
    list1, list2 = [], []
    if text1 == "No evidence":
        text1 = text1.replace("No evidence", "")
    if text2 == "No evidence":
        text2 = text2.replace("No evidence", "")
    if text3 == "No evidence":
        text3 = text3.replace("No evidence", "")
    for i, j in ghost.items():
        if text1 in j and text2 in j and text3 in j and text1 != "" and text2 != "" and text3 != "":
            list1.append(i)
        elif text2 in j and text3 in j and text1 == "" or text1 in j and text3 in j and text2 == ""\
              or text1 in j and text2 in j and text3 == "" or text2 in j and text3 == "" \
                and text1 == "" or text1 in j and text3 == "" and text2 == "" \
                    or text1 == "" and text2 == "" and text3 in j:
            list1.append(i)
        elif text1 == "" and text2 == "" and text3 == "":
            list2.append(i)
    if len(list1) > 0:
        for i in sorted(list1):
            print(i)
    elif len(list2) > 0:
        for i in sorted(list2):
            print(i)
    else:
        print("Not yet discovered")
main()
