#include<iostream>
using namespace std;
int firstoccur(int N,int arr[],int x)
{
	int beg=0,end=N-1;
	while(beg<=end)
	{
		int mid=(beg+end)/2;
		if(arr[mid]>x)
		{
			end=mid-1;
		}
		else if(arr[mid]<x)
		{
			beg=mid+1;
		}
		else
		{
			if(mid==0||arr[mid]!=arr[mid-1])
				return mid;
			else
				end=mid-1;
		}
	}

	return -1;
}
int lastoccur(int n,int a[],int k)
{
	int beg=0,end=n-1;
	while(end>=beg)
	{
		int mid=(beg+end)/2;
		if(a[mid]>k)
		{
			end=mid-1;
		}
		else if(a[mid]<k)
		{
			beg=mid+1;
		}
		else
		{
			if(mid==n-1 || a[mid]!=a[mid+1])
			{
				return mid;
			}
			else
			{
				beg=mid+1;
			}
		}
	}
	return -1;
}
int main()
{
int a[]={1,2,3,4,5,6,7,7,7,7,11,12};
int n=12;
int k=7;
cout<<lastoccur(n,a,k)-firstoccur(n,a,k)+1;
return 0;
}
