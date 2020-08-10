#include<iostream>
using namespace std;
int lastocc(int n,int a[],int k)
{
	//hello all
	//namaskara
	int beg=0,end=n-1;
	while(beg<=end)
	{
		int mid=(beg+end)/2;
		if(k>a[mid])
		{
			beg=mid+1;
		}
		else if(k<a[mid])
		{
			end=mid-1;
		}
		else
		{
			if(mid!=n-1 || a[mid]!=a[mid+1])
			{
				return mid;
			}
			else
			{
				beg= mid+1;
			}
		}
	}
	return -1;
}
int main()
{

	int a[]={5,10,10,10,10,20,20};
	int n=7;
	cout<<lastocc(n,a,10);
	return 0;
}
