#include <stdlib.h>
#include <uniStd.h>
#include <signal.h>
#include <stdio.h>
#define _POSIX_SOURCE
void my_handler (int sig); /* function prototype */
int main()
{
	struct sigaction my_action;
	/* Part I: Catch SIGINT */
	my_action.sa_handler = my_handler;
	my_action.sa_flags = SA_RESTART;
	sigaction (SIGINT, &my_action, NULL);
	printf ("Catching SIGINT\n");
	sleep (3);
	printf (" No SIGINT within 3 seconds\n");
	/* Part II: Ignore SIGINT */
	my_action.sa_handler = SIG_IGN;
	my_action.sa_flags = SA_RESTART;
	sigaction (SIGINT, &my_action, NULL);
	printf ("Ignoring SIGINT\n");
	sleep (3);
	printf (" Sleep is over\n");

	/* Part III: Default action for SIGINT */
	my_action.sa_handler = SIG_DFL;

	my_action.sa_flags = SA_RESTART;
	sigaction (SIGINT, &my_action, NULL);
	sleep (3);
	printf ("No SIGINT within 3 seconds\n");
}
void my_handler (int sig)
{
	printf (" \t I got SIGINT, number %d\n", sig);
exit(0);
}
