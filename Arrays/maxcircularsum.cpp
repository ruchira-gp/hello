#include<iostream>
using namespace std;
int kadanes(int n,int a[])
{
  int res=a[0],maxx=a[0];
  for(int i=1;i<n;i++)
  {
    maxx=max(a[i],a[i]+maxx);
    res=max(res,maxx);
  }
  return res;
}
int main()
{
  int n=5,maxi=0;
  int a[]={8,-4,3,-5,4};
  int maxsum=kadanes(n,a);
  if(maxsum<0)
  {
    cout<<maxsum;
    return 0;
  }
  for(int i=0;i<n;i++)
  {
    maxi=maxi+a[i];
    a[i]=-a[i];
  }
  int maxsum1=kadanes(n,a)+maxi;
  cout<<max(maxsum1,maxsum);
  return 0;


}
