#include<iostream>
using namespace std;
int maxconsecones(int n,int a[])
{
  int count =0,k=0;
  for(int i=0;i<n;i++)
  {
    if(a[i]==1)
    {
      k++;
    }
    else
    {
      count=max(count,k);
      k=0;
    }
    count=max(count,k);
  }
  return count;
}
int main()
{
  int a[]={0,0,0,0,0,0,0};
  int n=7;
  cout<<maxconsecones(n,a);
  return 0;
}
