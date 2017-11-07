#include<stdio.h>
#include<sys/wait.h>  
#include<stdlib.h>
void main()
{
int pid,pid2;
int status;
printf("Hello World!\n");
pid=fork();
printf("%d",pid);
if(pid!=0)
        {

                pid2=fork();
                printf("%d",pid2);
        }
if(pid == -1) 
{
perror("bad fork");
exit(1);
}
if (pid == 0||pid2==0)
printf("I am the child process.\n");
else
{
wait(&status);
printf("I am the parent process.\n");
}
}