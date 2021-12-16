#include <iostream>

using namespace std;

int main()
{
	int tab[10][10];
	for (int x = 0; x < 10; x++)
	{
		for (int y=0; y < 10; y++)
		{
			if (y == x)
			{
				tab[x][y] = 1;
			}
			else if(x+y==9)
			{
				tab[x][y] = 1;
			}
			else
			{
				tab[x][y] = 0;
			}
		}
	}
	for (int x = 0; x < 10; x++)
	{
		for (int y=0; y < 10; y++)
		{
			cout << tab[x][y];
		}
		cout << endl ;
	}
}
