---
layout: post
title: "Linux"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["linux"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# Books

* The Linux Programming Interface http://man7.org/tlpi/
* Raymond's The Art of Unix Programming is a good resource for understanding the design philosophy of Unix...and by extension Linux. It explains much of the context and history behind why things are done the way they are done and what good nix programs do to be good nix programs. http://www.catb.org/esr/writings/taoup/html/

# Linux Kernel

https://en.wikipedia.org/wiki/Template:Linux_kernel

# Users and Groups

See Which Groups Your Linux User Belongs To:

* http://www.howtogeek.com/howto/ubuntu/see-which-groups-your-linux-user-belongs-to/
* `groups <username>`

List all groups on you Linux system:

* `cat /etc/group`

# Linux Processes

## Fork

Ref:

* http://man7.org/tlpi/download/TLPI-24-Process_Creation.pdf
* http://unix.stackexchange.com/questions/136637/why-do-we-need-to-fork-to-create-new-processes
* From The Evolution of the Unix Time-sharing System: https://www.bell-labs.com/usr/dmr/www/hist.html
* http://advancedlinuxprogramming.com/alp-folder/alp-ch03-processes.pdf


The `fork()` system call allows one process, the parent, to create a new process, the child. The new child process an (almost) exact duplicate of the parent: the child obtains copies of the parent’s stack, data, heap, and text segments. Then both processes continue execution from right after the fork call in parallel. You'll need to get the PID in order to tell if the program that is currently being executed is the child or parent.

The two processes are executing the same program text, but they have separate copies of the stack, data, and heap segments.

The child’s stack, data, and heap segments are initially exact duplicates of the corresponding parts the parent’s memory.

After the fork(), each process can modify the variables in its stack, data, and heap segments without affecting the other process.

Within the code of a program, we can distinguish the two processes via thevalue returned from fork().

For the parent, fork() returns the process ID of the newly created child. 
This is useful because the parent may create, and thus need to track, several children (via wait() or one of its relatives). For the child, fork() returns 0.

```
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main ()
{
  pid_t child_pid;
  printf ("the main program process ID is %d\n", (int) getpid ());
  child_pid = fork ();
  if (child_pid != 0) {
    printf ("this is the parent process, with id %d\n", (int) getpid ());
    printf ("the child’s process ID is %d\n", (int) child_pid);
  }
  else
    printf ("this is the child process, with id %d\n", (int) getpid ());
  return 0;
}
```

### Fork: file descriptor and file description

* Example: http://stackoverflow.com/questions/11733481/can-anyone-explain-a-simple-description-regarding-file-descriptor-after-fork
* The program does a fork(). The new child process gets a copy of its parent's file descriptor table, but the file description is not copied.
* the file description is shared


#### fork()

ref: http://www.science.unitn.it/~fiorella/guidac/guidac096.html 

  "int fork()" trasforma un singolo processo in due processi identici, 
  riconoscibili come processo padre e processo figlio.
  In caso di successo, fork() ritorna 0 al processo figlio ed il process ID
  del processo figlio al processo padre; in caso di esito negativo, fork()
  ritorna -1 al processo padre, settando errno per indicare l'errore 
  verificatosi, e non viene creato nessun processo figlio.

  NOTA: il processo figlio avra' un suo proprio ed unico PID.

  Il seguente programma illustra un utilizzo semplice di fork(), dove vengono
  create due copie del processo ed eseguite assieme (multitasking):

     main()
     { int return_value;

       printf("Forking process\n");
       fork();
       printf("The process id is %d and return value is %d \n", 
              getpid(), return_value);
       execl("/bin/ls/","ls","-l",0);
       printf("This line is not printed\n");
     }

  L'output risultante sara':

     Forking process
     The process id is 6753 and return value is 0
     The process id is 6754 and return value is 0
     "two lists of files in current directory"

  NOTA: i processi hanno ID unici, che risulteranno diversi ad ogni esecuzione.

  E' anche impossibile stabilire in anticipo quale processo utilizzera' il 
  tempo di CPU (cosi', ogni esecuzione puo' essere diversa dalla successiva).

  Quando vengono generati due processi, possiamo facilmente scoprire (in ogni 
  processo) quale sia il figlio e quale il padre, poiche' fork ritorna 0 al
  figlio. Possiamo catturare qualsiasi errore se fork ritorna un -1, cioe':

     int pid; /* process identifier */

     pid=fork();
     if (pid < 0)
	{printf("Cannot fork!!\n");
         exit(1);
	}
     if (pid == 0)
        {/* child process */ ...}
     else 
 	{/* parent process pid is child's pid */ ...}



## Exec

The exec functions replace the program running in a process with another program.

Because exec replaces the calling program with another one, it never returns unless an error occurs.

A common pattern to run a subprogram within a program is first to fork the process and then exec the subprogram: This allows the calling program to continue execution in the parent process while the calling program is replaced by the subprogram in the child process.

The execve(pathname, argv, envp) system call loads a new program (pathname, with argument list argv, and environment list envp) into a process’s memory.

The existing program text is discarded, and the stack, data, and heap segments are freshly created for the new program.
This operation is often referred to as execing a new program. Later, we’ll see that several library functions are layered
on top of execve(), each of which provides a useful variation in the programming interface.

Where we don’t care about these interface variations, we follow the common convention of referring to these calls generically as exec(), but be
aware that there is no system call or library function with this name.


## Exec and fork togehter

```
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/* Spawn a child process running a new program. PROGRAM is the name
   of the program to run; the path will be searched for this program.
   ARG_LIST is a NULL-terminated list of character strings to be
   passed as the program’s argument list. Returns the process ID of
   the spawned process. */

int spawn (char* program, char** arg_list)
{
  pid_t child_pid;
  /* Duplicate this process. */
  child_pid = fork ();
  if (child_pid != 0)
    /* This is the parent process. */
    return child_pid;
  else {
    /* Now execute PROGRAM, searching for it in the path. */
    execvp (program, arg_list);
    /* The execvp function returns only if an error occurs. */
    fprintf (stderr, “an error occurred in execvp\n”);
    abort ();
  }
}

int main ()
{
  /* The argument list to pass to the “ls” command. */
  char* arg_list[] = {
    “ls”, /* argv[0], the name of the program. */
    “-l”,
    “/”,
    NULL /* The argument list must end with a NULL. */
  };
  /* Spawn a child process running the “ls” command. Ignore the
     returned child process ID. */
  spawn (“ls”, arg_list);
  printf (“done with main program\n”);
  return 0;
}
```


## Wait and Zombie processes

The wait(&status) system call has two purposes. First, if a child of this process
has not yet terminated by calling exit(), then wait() suspends execution of the
process until one of its children has terminated. Second, the termination status
of the child is returned in the status argument of wait().

http://advancedlinuxprogramming.com/alp-folder/alp-ch03-processes.pdf


Suspends the current process until at least one child process terminates.
It is a wrapper around waitpid() which allows you to pause the current process's execution and wait for a change in the state of a child process of the current process (which may be a clone of itself or a new program swapped in by exec)


```
Here is some code demoing waiting and forking (but no exec) from a class I took at University:

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <semaphore.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/wait.h>
const int BUFFER_SIZE = 1000;

void copySegment(int i, int segmentSize, FILE * fin, FILE * fout) {
    // Does not need to be shown to prove point
}

int main(int argc, char * argv[]) {
    int i;
    sem_t * sem;
    pid_t pid;
    FILE * fin, * fout;
    struct stat sbuf;
    int fileSize, fileDescriptor, segmentSize;
    fin = fopen(argv[1], "r");
    fout = fopen("forkcopy.txt", "w");
    fileDescriptor = fileno(fin);
    fstat(fileDescriptor, &sbuf);
    fileSize = sbuf.st_size;
    segmentSize = fileSize / 4;
    sem = sem_open("sem", O_CREAT | O_EXCL, 0644, 4);
    sem_unlink("sem");
    for (i = 0; i < 4; i++) {
        pid = fork();
        if (pid < 0)
            printf("Fork error.\n");
        else if (pid == 0)
            break;
    }
    if (pid != 0) {
        while (pid = waitpid(-1, NULL, 0)) {
            if (errno == ECHILD)
                break;
        }
        sem_destroy(sem);
        fclose(fin);
        fclose(fout);
        exit(0);
    } else {
        sem_wait(sem);
        copySegment(i, segmentSize, fin, fout);
        sem_post(sem);
        exit(0);
    }
}
```


## Signals

http://advancedlinuxprogramming.com/alp-folder/alp-ch03-processes.pdf

* when a signal is directed to a process group, the signal is delivered to each process that is a member of the group.

## Proces group

https://en.wikipedia.org/wiki/Process_group

* a session denotes a collection of one or more process groups.
