#include <iostream>

using namespace std;

int main()
{
	int tab[2][2];

	for (int x=0; x < 2; x++)
	{
		for (int y=0; y < 2; y++)
		{
			cin >> tab[x][y];
		}
	}
	int wynik = (tab[0][0] * tab[1][1]) - (tab[0][1] * tab[1][0]);
	cout << "wynik to "<< wynik <<endl;
}

