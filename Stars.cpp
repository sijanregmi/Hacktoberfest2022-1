#include <bits/stdc++.h>

#define ll long long
#define f first
#define s second
#define ull unsigned long long int
#define pushb push_back
#define popb pop_back
#define INF 1e18+9
#define endl '\n'
#define Mod 1000000007
#define MAX 1000001

using namespace std;

// Pattern 1
void printPattern1(int n){
	for(int row=1;row<=n;row++){
		for(int col=1;col<=n;col++){
			cout << "*";
		}
		cout << endl;
	}
}

// Pattern 2
void printPattern2(int n){
	for(int row=1;row<=n;row++){
		for(int col=1;col<=row;col++){
			cout << "*";
		}
		cout << endl;
	}
}



int main()
{
   int size=0,choice=0;
   cin >> size >> choice;
   switch(choice){
   	case 1: printPattern1(size);
   	break;
   	case 2: printPattern2(size);
   	break;
   }
   return 0;
}
