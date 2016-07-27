forAuction = {}
participants = []
currentAuctionInfo = {}
passMe = []


def auctionSetup():
    #Initializing a variable that holds the item that'll eventually be auctioned
    auctionItem = raw_input("What would you like to put up for auction? ")
    
    #Initializing a variable that holds the reserved for the item
    itemPrice = raw_input("What is "+auctionItem+" reserved Price? $")
    
    #This try & except statement is used to make sure the user entered a number. If they didn't, it starts over.
    try:
        float(itemPrice)
        itemPrice = float(itemPrice)
    except:
        print "Please enter only numbers"
        auctionSetup()

    #Adds the item to be auctioned and it's price to a dictionary. Item name being the key, and the price the value    
    forAuction[auctionItem] = itemPrice

    #Checks if another item will entered in the auction
    decision = raw_input("Do you want to add another item? (enter y/n)").lower()
    if decision == "y":
        auctionSetup()
    if decision == "n":
        print "T
        participantSetup()
    else:
        print "Please enter 'y' or 'n'"
        decision = raw_input("Do you want to add another item? (enter y/n)").lower()
        if decision == "y":
            auctionSetup()
        if decision == "n":
            participantSetup()


def participantSetup():
    #A loop that collects all the participants, placing them in a list
    while True :
        print "***Type 'done' when there are no other participants***"
        participant = raw_input("If you plan to participate in the auction, Please enter your first and last name or an auction name(Username): ")
        if participant == "done":
            break
        if len(participant) < 3:
            print "Must be atleast 3 characters long..Try again"
            participantSetup()
        else:
            participants.append(participant)
        
    #Goes into the dictionary of auctionable items, and selects the first one (which will still be random). Then sets it to a variable    
    itemBeingAuct = forAuction.keys()[0]
    print itemBeingAuct
    print "Alright, We will now start the auction for the " + itemBeingAuct
    Auction(itemBeingAuct)

def Auction(itemBeingAuct):
    #Gets the starting bid. Then makes sure it isn't higher than the reserved price.  
    highestBid = raw_input("What is the starting bid? $")
    try:
        float(highestBid)
    except Exception, e:
        print "Please enter only numbers"
        print str(e)
        Auction(itemBeingAuct)
    else:
        highestBid = float(highestBid)
    if highestBid > float(forAuction.get(itemBeingAuct)):
        print "Starting bid cannot be higher than reserved price"
        Auction(itemBeingAuct)
    elif highestBid < float(forAuction.get(itemBeingAuct)):
        print "The starting bid is $"+str(highestBid)

     #Just explaining how to pass if you can't bid any higher
    print "***If you cannot bid higher than the Highest Bid at any point, just enter '0' and you will be skipped***"  

    #A loop that basically gets bids. If you skip yourself by enter "0", your name is entered into a list. It does this until everyone skips except the highest bidder of course.
    while True:
        for person in participants:
            bid = raw_input(person + ",please enter your bid amount: $")
            if bid == "0":
                if person not in passMe:
                    passMe.append(person)
                    pass
                elif person in passMe:
                    pass
                if len(passMe) == len(participants)-1:
                    break
            elif float(bid) > highestBid:
                highestBid = float(bid)
                print person + " has made the highest bid with: $"+str(highestBid)

            elif float(bid) < highestBid:
                print "Your bid must be greater than "+"$"+str(highestBid)
                bid = raw_input(person + ", please enter your bid amount: $")
                if float(bid) > highestBid:
                    highestBid = float(bid)
                    print person + " has made the highest bid with: $"+str(highestBid)

                elif bid == "0":
                    if person not in passMe:
                        passMe.append(person)
                        pass
                    if person in passMe:
                        pass
                
                else:
                    print person + "you will now be skipped"
                    passMe.append(person)

        if len(passMe) == len(participants)-1:
            break

    #Letting it be known the auction is over. Also letting us know who the winner is & whether it as success or not.         
    print"The bidding for the "+itemBeingAuct+" is now over!"
    for person in participants:
        if person not in passMe:
            winner = person
    
    print"Sold to " + winner + " for $" +  str(highestBid) + "!!"


    if highestBid > float(forAuction.get(itemBeingAuct)):
        print "The auction was a sucess!"

    else:
        print "The aucion was a failure..."

            

    
        
    










auctionSetup()

print"The bidding for the "+itemBeingAuct+" is now over!"
    for person in participants:
        if person not in passMe:
            winner = person
    
print"Sold to " + winner + " for $" +  str(highestBid) + "!!"


if highestBid > float(forAuction.get(itemBeingAuct)):
    print "The auction was a sucess!"

else:
    print "The aucion was a failure..."

del forAuction[itemBeingAuct]

if len(forAuction) > 0:
    participantSetup()
    
