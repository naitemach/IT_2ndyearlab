#include <iostream>
#include <string.h>
#include <stdio.h>
#include <fstream>

using namespace std;
#define N 5


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

void stableMarriage(int prefer[2*N][N])
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
    cout << "man    woman" << endl;
    for(int i=0;i<N;i++)
    {
    	cout << " " << wPatner[i] << "\t" << i+N << endl;
    }
}

int main()
{	

	ifstream inFile;
	inFile.open("input.txt");
    int prefer[2*N][N] = { 
    	{6,5,8,9,7},
        {8,6,5,7,9},
        {6,9,7,8,5},
        {5,8,7,6,9},
        {6,8,5,9,7},
        {4,0,1,3,2},
        {2,1,3,0,4},
        {1,2,3,4,0},
        {0,4,3,2,1},
        {3,1,4,2,0},
    };
    stableMarriage(prefer);
    return 0;
}