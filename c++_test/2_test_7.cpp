// 2_test_7.cpp

#include <iostream>
#include <type_traits>

using namespace std;

void shown_time(int,int);

int main()
{
	cout << "Enter the number of hours:";
	int number_hours;
	cin >> number_hours;
	cout << "Enter the number of mintes:";
	int number_mintes;
	cin >> number_mintes;
	shown_time(number_hours, number_mintes);
	return 0;
}

void shown_time(int number_hours, int number_mintes)
{
	cout << "Time: " << number_hours << ":" << number_mintes << endl;
}
