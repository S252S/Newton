#include<iostream>
#include<map>
#include<string>
using namespace std;
int main()
{
typedef map<string,int> mapType;

mapType populationMap;

populationMap.insert(pair<string, int>("Maharashtra", 7026357));
populationMap.insert(pair<string, int>("Rajasthan", 6578936));
populationMap.insert(pair<string, int>("Karanataka", 6678993));
populationMap.insert(pair<string, int>("Punjab", 5789032));
populationMap.insert(pair<string, int>("West Bengal", 6676291));

mapType::iterator iter;
cout<<"* * * * * * * * * * * * *Population of states in India * * * * * * * * * * * * *\n";
cout<<"\n Size of populationMap: "<<populationMap.size()<<"\n";
string state_name;
cout<<"\nEnter name of the state :";
cin>>state_name;
iter = populationMap.find(state_name);
if( iter!= populationMap.end())
 cout<<state_name<<"'s population is: "
 <<iter->second <<endl;
else
cout<<"Key is not population Map"<<"\n";
populationMap.clear();
}


