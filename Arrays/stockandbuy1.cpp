#include<iostream>
using namespace std;
int stock(int n,int a[])
{
  int min=0;
  int max=a[0];
  for(int i=1;i<n-1;i++)
  {
    if(a[i]>a[i-1])
    {
      profit=profit+(a[i]-a[i-1]);
    }
  }
  return profit;
}
int main()
{
  //code here;
}
