#include <iostream>
#include <stdio.h>
#include <iomanip>


using namespace std;
#define N 4


bool wPrefersM1OverM(int prefer[2*N][N],int w,int m,int m1)
{
	for(int i=0;i<N;i++)
	{
		if(prefer[w][i]==m1)
		{
			return true;
		}
		if(prefer[w][i]==m)
		{
			return false;
		}
	}
}



void stableMarriage(int prefer[2*N][N],char men[N][10],char women[N][10])
{
	int wPatner[N];
	bool mFree[N];
	for(int i=0;i<N;i++)
	{
		wPatner[i] = -1;
		mFree[i] = true;
	}

	int freeCount = N;
	while(freeCount>0)
	{
		int m;
		for(m=0;m<N;m++)
		{
			if(mFree[m] == true)
			{
				break;
			}
		}
		for(int i=0;i<N && mFree[m] == true;i++)
		{
			int w = prefer[m][i];
			if(wPatner[w-N] == -1)
			{
				wPatner[w-N] = m;
				mFree[m] = false;
				freeCount--;
			}
			else
			{
				int m1 = wPatner[w-N];
				if(wPrefersM1OverM(prefer,w,m,m1) == false)
				{
					wPatner[w-N] = m;
					mFree[m] = false;
					mFree[m1] = true;
				}
			}
		}
	}
    cout << " man      woman " << endl;

    for(int i=0;i<N;i++)
    {
    	cout<<left;
    	cout <<setw(8)<< men[wPatner[i]] << "-"<<"  " << women[i] << endl;
    }
}

int main()
{	
    char men[N][10]={"0","1","2","3"};
	char women[N][10]={"4","5","6","7"};

    int prefer[2*N][N] = { 
    	{7,5,6,4},
        {5,4,6,7},
        {4,5,6,7},
        {4,5,7,6},
        {0,1,2,3},
        {0,1,2,3},
        {0,1,2,3},
       
        {3,1,2,0},
   
    };
    stableMarriage(prefer,men,women);
    return 0;
}