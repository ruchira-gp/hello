#include<iostream>
using namespace std;
int rainwater(int n,int a[])
{
    int rmax[n],lmax[n];
  lmax[0]=a[0];
  for(int i=1;i<n;i++)
  {
    lmax[i]=max(lmax[i-1],a[i]);
  }
  rmax[n-1]=a[n-1];
  for(int i=n-2;i>=0;i--)
  {
    rmax[i]=max(rmax[i+1],a[i]);
  }
  int res=0;
  for(int i=0;i<n-1;i++ )
  {
    res=res+(min(rmax[i],lmax[i])-a[i]);
  }
  return res;
}
int main()
{
  int a[]={5,0,6,2,3};
  int n=5;
  cout<<rainwater(5,a);
  return 0;
}
