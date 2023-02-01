// arrayone.cpp -- small arrays of integers

#include <iostream>

int main()
{
	using namespace std;
	int yams[3];
	yams[0]=7;
	yams[1]=8;
	yams[2]=6;

	int yamcosts[3]={20,30,5};

	cout << "Total yams = ";
	cout << yams[0]+yams[1]+yams[2]<<endl;
	cout << "Total yamcosts = ";
	cout << yamcosts[0]+yamcosts[1]+yamcosts[2]<<endl;
}
