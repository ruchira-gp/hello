#include<iostream>
using namespace std;
int kadane(int n,int a[])
{
  int maxend=0,maxi=0;
  for(int i=1;i<n;i++)
  {
    maxend=max(maxend+a[i],a[i]);
    maxi=max(maxend,maxi);
  }
  return maxi;
}
int main()
{
  int a[]={-5,1,-2,3,-1,2,-2};
  int n=7;
  cout<<kadane(n,a);
  return 0;
}
