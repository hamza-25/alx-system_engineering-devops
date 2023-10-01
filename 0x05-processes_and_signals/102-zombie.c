#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
/**
 * infinite_while - funtction that ran infinity
 * Return: int 0 success
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point for printing pid
 * Return: int 0 success
*/

int main(void)
{
	int i = 0;
	pid_t pid;

	while (i < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			i++;
		}
		else
			exit(0);

	}

	infinite_while();

	return (0);
}
