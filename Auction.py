forAuction = {}
participants = []
currentAuctionInfo = {}
passMe = []


def auctionSetup():
    auctionItem = raw_input("What would you like to put up for auction? ")
    itemPrice = raw_input("What is "+auctionItem+" reserved Price? $")
    try:
        float(itemPrice)
        itemPrice = float(itemPrice)
    except:
        print "Please enter only numbers"
        auctionSetup()
    forAuction[auctionItem] = itemPrice
    decision = raw_input("Do you want to add another item? (enter y/n)").lower()
    if decision == "y":
        auctionSetup()
    if decision == "n":
        participantSetup()


def participantSetup():
    
    while True :
        print "***Type 'done' when there are no other participants***"
        participant = raw_input("If you plan to participate in the auction, Please enter your first and last name or an auction name(Username): ")
        if participant == "done":
            break
        if len(participant) < 3:
            print "Must be atleast 3 characters long..Try again"
        else:
            participants.append(participant)
        
        
    itemBeingAuct = forAuction.keys()[0]
    print itemBeingAuct
    print "Alright, We will now start the auction off with a " + itemBeingAuct
    Auction(itemBeingAuct)

def Auction(itemBeingAuct):
      
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

 
    print "***If you cannot bid higher than the Highest Bid at any point, just enter '0' and you will be skipped***"  
    
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
                
    print"The bidding for the "+itemBeingAuct+" is now over!"
    for person in participants:
        if person not in passMe:
            winner = person
    
    print"Sold to " + winner + " for $" +  str(highestBid) + "!!"

            

    
        
    









decision = raw_input("Would you like to add a new item to the auction?""**Just press Enter**")
if len(decision) < 1:
    auctionSetup()
