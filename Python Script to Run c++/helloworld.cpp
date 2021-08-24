#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the Python Script!"};

    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout << endl;
    int num;
    cout << "Please Enter one Number = ";
    cin >> num;
    return num;
}