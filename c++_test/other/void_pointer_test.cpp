#include <cstddef>
#include <iostream>

using namespace std;

int main(){

int array[5]={1,2,3,4,5};
void* pValue = array;
cout<<"pValue指向的数据为"<<*(int *)pValue<<endl;
int* a;
a = (int *)pValue;  // void指针的强制类型转换；

// 两种定义空指针的方法；
void* pv = 0;
void* pv2 = NULL;
cout << "空指针pv的地址值："<< pv<<endl;
cout << "空指针pv2的地址值："<< pv2<<endl;

return 0;
}
