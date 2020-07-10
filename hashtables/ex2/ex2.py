#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route = []

    # Hash Tickets
    hash = {}

    for ticket in tickets:
        hash[ticket.source] = ticket.destination

    # Add Origin ticket
    route.append(hash["NONE"])

    # Add ticket to route according to value of last ticket
    for ticket in hash:
        if ticket == "NONE":
            continue
        route.append(hash[route[-1]])
    return route
