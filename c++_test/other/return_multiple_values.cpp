#include <cstdio>
#include <iostream>
#include <string>
#include <tuple>

using namespace std;

//方法一：函数参数传入地址或指针：
void GetUserAge1(const string& user_name, bool& work_status, int& age)
{
	if (user_name.compare("xiaoli")==0)
	{
		work_status = true;
		age = 18;
	}
	else
	{
		work_status = false;
		age = -1;
	}
}

//方法二：使用std:pair(只能返回两个变量)或std:tuple(返回三个或三个以上返回值)；
tuple<bool, int, int> GetUserAge2(const string user_name)
{
	tuple<bool,int,int> result;

	if (user_name.compare("xiaoli")==0)
	{
		result = make_tuple(true, 18,0);
	}
	else {
	result = make_tuple(false ,-1,-1);
	}
	
	return result;
}

int main()
{
	bool work_status;
	int age;
	int user_ID;

	GetUserAge1("xiaoli", work_status, age);
	cout<< "查询结果："<<work_status<<"  "<<"年龄："<<age<<endl;
	cout << "输入一个字符再次查询"<<endl;
	getchar();
	
	tuple<bool, int,int> result = GetUserAge2("xiaoli");
	tie(work_status, age, user_ID) = result;	
	cout<< "查询结果："<<work_status<<"  "<<"年龄："<<age<<endl;
	cout << "输入一个字符结束查询";
	getchar();
	return 0;
}
