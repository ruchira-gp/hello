#include<iostream>
using namespace std;
void snake(int **arr,int r,int c)
{
  int x=2;
  for(int i=0;i<r;i++)
  {
    if(x%2==0)
    {
      for(int j=0;j<c;j++)
      {
        cout<<arr[i][j]<<" ";
        if(j==c-1)
        {
          x++;
        }
      }
    }
    else
    {
      for(int j=c-1;j>=0;j--)
      {
        cout<<arr[i][j]<<" ";
        if(j==0)
        {
          x++;
        }
      }

    }
  }

}
int main()
{
  int m=4,k=0;
  int **arr;
  arr=new int *[m];
  for(int i=0;i<m;i++)
  {
  arr[i]=new int[m];
  for(int i=0;i<m;i++)
  {
    for(int j=0;j<m;j++)
    {
      arr[i][j]=k;
      k++;
    }
  }
}
  snake(arr,m,m);
  return 0;
}
