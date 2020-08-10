#include<iostream>
using namespace std;
int countgroups(int n,int a[],int c)
{
  int count=0;
  int curr=1,maxx=1;
  for(int i=1;i<n;i++)
  {

    if(a[i]!=a[i-1])
    {
      count++;
    }
  }
  if (count==0)
  return 1;
  return count;
}
int flipnumber(int n,int a[])
{
  int one=0,zero=0;
  for(int i=0;i<n;i++)
  {
    if(a[i]==0)
    zero++;
    else
    one++;
  }
  if(zero>=one)
  return 0;
  else
  return 1;
}
int grpflip(int n,int a[])
{
  return 0;
}
int main()
{
  int n=13;
  int a[]={1,0,0,0,1,0,0,1,1,1,1,0,1};
  //int c=flipnumber(n,a);
  int grps=countgroups(n,a,1);
  cout<<grps;

  return 0;
}
