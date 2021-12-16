#include <iostream>

using namespace std;

int main()
{
	int tab[2][2];
	for (int x = 0; x < 2; x++)
	{
		for (int y = 0; y < 2; y++)
		{
			cin >> tab[x][y];
		}
	}
	for (int x = 0; x < 2; x++)
	{
		for (int y = 0; y < 2; y++)
		{
			cout << tab[x][y]<<endl;
		}
	}
}
