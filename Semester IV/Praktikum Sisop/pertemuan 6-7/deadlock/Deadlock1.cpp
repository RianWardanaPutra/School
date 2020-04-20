#include <iostream>
#include <thread>
#include <exception>
using namespace std;

bool doNot = 1;
thread *fn1;
thread *fn2;

void func1 (bool x)
{
	while(doNot){;} 
	::fn2->join();
}

void func2(bool x)
{
	while(doNot) {;}
	::fn1->join();
}

int main()
{
	thread t1(func1, 1);
	thread t2(func2, 1);

	::fn1 = &t1;
	::fn2 = &t2;
	::doNot = 0;
	t1.join();
	t2.join();
	cout << "Hello";
}