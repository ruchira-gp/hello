#include<iostream>
using namespace std;
int main()
{
/*int a[3][2]={{1,2},{3,4},{5,6}};
for(int i=0;i<3;i++)
{
  for(int j=0;j<2;j++)
  {
    cout<<a[i][j]<<" ";
  }
}
*/
int m=3,n=2;
int *arr[m];
for(int i=0;i<m;i++)
arr[i]=new int[n];
for(int i=0;i<m;i++)
{
  for(int j=0;j<n;j++)
  {
    arr[i][j]=i+j;
    cout<<arr[i][j]<<" ";
  }
}

return 0;
}
