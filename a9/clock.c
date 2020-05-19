#include<stdio.h>
#include<pthread.h>
#include<time.h>
#include<unistd.h>

int secs, mins, hrs;

void *seconds() {
	while(1) {
		sleep(1);
		secs++;
	}
}

void *minutes() {
	while(1) {
		if(secs == 60){
			secs = 0;
			mins++;			
		}
	}
}

void *hour() {
	while(1) {
		if(mins == 60){
			mins = 0;		
			hrs++;
		}
	}
}

void *print() {
	while(1) {
		printf("\r%02d : %02d : %02d", hrs, mins, secs);
	}
}

int main() {
	pthread_t t1,t2,t3,t4;
	int a, b, c, d;
	
	time_t s; 
	struct tm* current_time; 

	s = time(NULL); // time in seconds 
	current_time = localtime(&s); // to get current time 
	
	hrs = current_time->tm_hour;
	mins = current_time->tm_min;
	secs = current_time->tm_sec;
	
	a = pthread_create(&t1, NULL, seconds, NULL);
	b = pthread_create(&t2, NULL, minutes, NULL);
	c = pthread_create(&t3, NULL, hour, NULL);
	d = pthread_create(&t4, NULL, print, NULL);
	
	
	pthread_join(t2, NULL);
	pthread_join(t3, NULL);
	pthread_join(t4, NULL);
		
	return 0;
}













