# Mohamed Mahmoud
# Blood Type Compatibility Program

# Start of Program

donor = input("Enter donor blood type: ")
recipient = input("Enter recipient blood type: ")

if donor=="O-": 
    print("Compatible")
elif donor=="O+" and recipient=="AB+":
    print("Compatible")
elif donor=="O+" and recipient=="A+":
    print("Compatible")
elif donor=="O+"and recipient=="B+":
    print("Compatible")
elif donor=="O+" and recipient=="O+":
    print("Compatible")
elif donor=="B-" and recipient=="AB+":
    print("Compatible")
elif donor=="B-" and recipient=="AB-":
    print("Compatible")
elif donor=="B-" and recipient=="B+":
    print("Compatible")
elif donor=="B-" and recipient=="B-":
    print("Compatible")
elif donor=="B+" and recipient=="AB+":
    print("Compatible")
elif donor=="B+" and recipient=="B+":
    print("Compatible")
elif donor=="A-" and recipient=="AB+":
    print("Compatible")
elif donor=="A-" and recipient=="AB-":
    print("Compatible")
elif donor=="A-" and recipient=="A+":
    print("Compatible")
elif donor=="A-" and recipient=="A-":
    print("Compatible")
elif donor=="A+" and recipient=="AB+":
    print("Compatible")
elif donor=="A+" and recipient=="A+":
    print("Compatible")
elif donor=="AB-" and recipient=="AB+":
    print("Compatible")
elif donor=="AB-" and recipient=="AB-":
    print("Compatible")
elif donor=="AB+" and recipient=="AB+":
    print("Compatible")
elif donor=="A-" and recipient=="AB":
    print("Invalid")
elif donor=="a-" and recipient=="AB":
    print("Invalid")
else:
    print("Incompatible") #any other combination would be considered Incompatible
    
# End of Program
