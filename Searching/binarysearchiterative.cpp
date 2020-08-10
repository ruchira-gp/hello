#include<iostream>
using namespace std;
int binarysearch(int n,int a[],int ele)
{
  int beg=0;
  int end=n-1;
  int mid=(beg+end)/2;
  while(end>=beg)
  {
    mid=(beg+end)/2;
    if(a[mid]==ele)
    return mid;
    else if(ele>a[mid])
    {
      beg=mid+1;
    }
    else if(ele<a[mid])
    {
      end=mid-1;
    }

  }
  return -1;
}
int main()
{
  int a[]={10,20,30,40,50,60,70};
  int n=7;
  cout<<binarysearch(n,a,20);
  return 0;
}
