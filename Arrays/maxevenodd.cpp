#include<iostream>
using namespace std;
int maxevenodd(int n,int a[])
{
  int curr=1,maxx=1;
  for(int i=1;i<n;i++)
  {
    if(a[i-1]%2==0 && a[i]%2!=0 )
    {
      curr++;
    }
    else if (a[i-1]%2!=0 && a[i]%2==0)
    {
        curr++;
    }

    maxx=max(curr,maxx);
  }
  return maxx;
}
int main()
{
  int a[]={5,10,20,6,3,8};
  int n=6;
  cout<<maxevenodd(n,a);
  return 0;

}
