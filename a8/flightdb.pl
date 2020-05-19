:-initialization(main).
main :- write('AIRLINE MANAGEMENT SYSYTEM').

%airport(city,airporttax,minsecuritydelay).

airport(toronto,60,60).
airport(london,75,80).
airport(madrid,75,45).
airport(barcelona,40,30).
airport(valencia,40,20).
airport(malaga,50,30).
airport(paris,50,60).
airport(toulouse,40,30).

%flight(from,airline,to,price,duration).

flight(toronto,aircanada,london,500,360).
flight(toronto,united,london,650,420).
flight(toronto,aircanada,madrid,900,480).
flight(toronto,united,madrid,950,540).
flight(toronto,iberia,madrid,800,480).
flight(madrid,aircanada,barcelona,100,60).
flight(madrid,iberia,barcelona,120,65).
flight(madrid,iberia,valencia,40,50).
flight(madrid,iberia,malaga,50,60).
flight(barcelona,iberia,london,220,240).
flight(barcelona,iberia,valencia,110,75).
flight(valencia,iberia,malaga,80,120).
flight(paris,united,toulouse,35,120).

%To print all flights from city A to city B

toPrintFlight(A,B):- (flight(A,C,B,D,E);flight(B,C,A,D,E)),printFlight(A,C,B,D,E). 

printFlight(From, Airline, To, Price, Duration):-
	write('\nFrom:\n'),
   	write(From),
	write('\nAirline:\n'),
   	write(Airline),
   	write('\nTo:\n'),
   	write(To),
   	write('\nPrice:\n'),
   	write(Price),
   	write('\nDuration:\n'),
   	write(Duration).

%To print airport of city A
   	
toPrintAirport(A):- airport(A,B,C),printAirport(A,B,C). 

printAirport(City,Airporttax,Minsecuritydelay):-
	write('\nCity:'),
   	write(City),
	write('\nAirport Tax:'),
   	write(Airporttax),
   	write('$'),
   	write('\nMin Security Delay:'),
   	write(Minsecuritydelay),
   	write('min').
   

%Is there a flight from Toronto to Madrid?
flightExists(A,B):- flight(A,_,B,_,_);flight(B,_,A,_,_).

%Is it possible to go from Toronto to Paris in two flights?
twoFlightPossible(A,B):- flight(A,_,X,_,_),flight(X,_,B,_,_);flight(B,_,X,_,_),flight(X,_,A,_,_).

%A flight from city A to city B with airline C is cheap if its price is less than $400.
cheap(A,B,C):- (flight(A,C,B,Price,_);flight(B,C,A,Price,_)), Price<400.

%A flight from city A to city B with airline C is preferred if it is cheap or if it is Air Canada
prefer(A,B,C):- cheap(A,B,C);((flight(A,C,B,P,_);flight(B,C,A,P,_)), C = aircanada, P > 400).

%If there is a flight from city A to city B with United, then there is a flight from city A to city B with Air Canada. 
possible(A,B):- flight(A,united,B,_,_)->flight(A,aircanada,B,_,_);flight(B,united,A,_,_)->flight(B,aircanada,A,_,_).






