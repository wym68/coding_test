// limits.cpp -- some integer limits

#include <iostream>
#include <climits>

int main()
{
	using namespace std;
	int n_int = INT_MAX;
	short n_short = SHRT_MAX;
	long n_long = LONG_MAX;
	long long n_llong = LLONG_MAX;

	cout << "size" << endl<< sizeof(n_int)<< endl<<sizeof(n_short)<< endl<<sizeof(n_long)<< endl<<sizeof(n_llong)<< endl;
	cout << "maximun values" << endl<< n_int<< endl<<n_short<< endl<<n_long<< endl<<n_llong<< endl;


}
