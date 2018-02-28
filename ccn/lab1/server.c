#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <errno.h>

main(){
	int serSock;
	struct sockaddr_in server,clientDetail;
	server.sin_family = AF_INET;
	server.sin_port = htons(10000);
	server.sin_addr.s_addr = INADDR_ANY;
	int cli,sentConf;
	unsinged int len = sizeof(struct sockaddr*);
	char mesg[] = "Hello worlld with socket programming";
	if((serSock=socket(PF_INET,SOCK_STREM,0))==-1){
		perror("There are some issues in creating the socket");
		exit(-1);
	}
	if((bind(serSock,(struct sockaddr *) &server,len))==-1){
		perror("Error in binding");
		exit(-1);
	}
	if((listen(serSock,5))==-1){
		perror("Error in Listening");
		exit(-1);
	}
	while(1){

	}	






}