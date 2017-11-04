#include <bits/stdc++.h>
using namespace std;
typedef pair<int,int> ii;
typedef vector<int>   vi;
typedef vector<long long> vll;
typedef vector<pair<int,int> > vii;
#define ll long long
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define pq priority_queue
#define mii map<int,int>
#define sf1(x) scanf("%d",&x)
#define sf2(x,y) scanf("%d %d",&x,&y)
#define sf3(x,y,z) scanf("%d %d %d",&x,&y,&z)
int inf = (1e9) + 7;
int mod = 998244353;




int main(){


	
	FILE* fp;
	FILE* output;
	int cont = 0;
	char file_name[100];
	fp =   fopen("input.csv","a+");
	char s[100005];
	output = fopen("output0.csv","a+");
	while(!feof(fp)){

		fread(s,100000,1,fp);
		fwrite(s,100000,1,output);
		if(ftell(output) >= 200000000)
		{
			cont++;
			sprintf(file_name,"output%d.csv",cont);
			fclose(output);
			output = fopen(file_name,"a+");
		}
	}
	
	printf("\n");
	fclose(fp);	
	fclose(output);	


}