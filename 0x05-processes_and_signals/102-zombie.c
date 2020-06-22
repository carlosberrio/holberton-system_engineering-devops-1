#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Runs an infinite loop
 * Return: always 0
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
 * main - Creates five child processes
 * Return: always 0
 */

int main(void)
{
	int c;

	for (c = 0; c < 5; c++)
	{
		if (fork() == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			return (0);
		}
	}
	infinite_while();
	return (0);
}
