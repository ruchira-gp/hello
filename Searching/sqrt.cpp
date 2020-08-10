#include<iostream>
using namespace std;
int sqroot(int n)
{
	int beg=1,end=n,ans=-1;
	while(beg<=end)
	{
		int mid=(beg+end)/2;
		int sq=mid*mid;
		if(sq==n)
		{
			return mid;

		}
		else if(sq>n)
			end=mid-1;
		else
		{
			beg=mid+1;
			ans=mid;
		}
	}
	return ans;
}
int main()
{
	cout<<sqroot(5);
	return 0;
}
