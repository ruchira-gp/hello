#include<iostream>
using namespace std;
int maxdif(int n,int a[])
{
	int minn=a[0];
	int maxx=a[1]-a[0];
	for(int i=1;i<n;i++)
	{
		minn=min(minn,a[i-1]);
		maxx=max(a[i]-minn,maxx);
	}
	return maxx;
}
int main()
{
	int a1[]={2,3,10,6,4,8,1};
	int n1=7;
	int a2[]={7,9,5,6,3,2};
        int n2=6;
	int a3[]={10,20,30};
        int n3=3;
	int a4[]={30,10,8,2};
        int n4=4;



	cout<<maxdif(n1,a1)<<"\n";
	cout<<maxdif(n2,a2)<<"\n";
	cout<<maxdif(n3,a3)<<"\n";
	cout<<maxdif(n4,a4)<<"\n";
	return 0;
}
