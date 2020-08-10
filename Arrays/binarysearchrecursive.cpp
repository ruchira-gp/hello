#include<iostream>
using namespace std;
int binarysearch(int a[],int ele,int beg,int end)
{
  int mid=(beg+end)/2;
  if(a[mid]==ele)
    return mid;
  else if(a[mid]>ele)
  {
    binarysearch(a,ele,beg,mid-1);
  }
  else if(a[mid]<ele)
  {
    binarysearch(a,ele,mid+1,end);
  }
  else{
    return -1;
  }

}
int main()
{
  int a[]={1,2,3,4,5};
  int n=5;
  cout<<binarysearch(a,1,0,4);
  return 0;
}
