#include<iostream>
using namespace std;
int main()
{

	int a[]={7,10,4,3,6,5,2};
	int b[]={7,10,4,3,6,5,2};

	int n=7;
	int maxx=a[n-1];
	for(int i=n-1;i>=0;i--)
	{
		if(a[i]<=maxx)
		{
			a[i]=maxx;
		}
		else
		{
			maxx=max(maxx,a[i]);
		}
	}
/*	for(int k:a)
	{
		cout<<k<<" ";
	}
*/
	int temp=a[0];
	cout<<a[0]<<" ";
	for(int i=1;i<n;i++)
	{
		if(temp!=a[i])
		{
			cout<<a[i]<<" ";
			temp=a[i];
		}
	}
	return 0;
}


